#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml>=6"]
# ///
"""Lint the skills in this plugin before they ship.

Rules come from three public sources:
  spec     https://agentskills.io/specification
  code     https://code.claude.com/docs/en/skills
  platform https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

Errors break a rule a client enforces; warnings flag authoring guidance.
The exit status is 1 when any skill has an error (or a warning, with --strict).

    scripts/check_skills.py                 # every skill under ./skills
    scripts/check_skills.py skills/foo      # one skill, or any folder of skills
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("check_skills: needs PyYAML. Run it with `uv run scripts/check_skills.py`, "
             "or install PyYAML with `python3 -m pip install pyyaml`.")

ROOT = Path(__file__).resolve().parent.parent

# Frontmatter keys Claude Code documents; anything else is ignored silently, so it is likely a typo.
KNOWN_KEYS = {
    "name", "description", "when_to_use", "argument-hint", "arguments",
    "disable-model-invocation", "user-invocable", "allowed-tools", "disallowed-tools",
    "model", "effort", "context", "agent", "background", "hooks", "paths", "shell",
    "metadata", "license", "compatibility",
}
BOOLEAN_KEYS = {"disable-model-invocation", "user-invocable", "background"}
BOOLEAN_WORDS = {"true", "false", "yes", "no", "on", "off", "1", "0"}
EFFORT_LEVELS = {"low", "medium", "high", "xhigh", "max"}

NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
XML_TAG = re.compile(r"</?[A-Za-z][\w:-]*[^<>]*>")
TRIGGER_HINT = re.compile(r"\buse (?:it |this(?: skill)? )?(?:when|for|to|if|whenever)\b", re.I)
MD_LINK = re.compile(r"\]\(\s*<?([^()\s<>]+)>?[^)]*\)")
CODE_SPAN = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]+`", re.S)
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#|/)", re.I)


@dataclass
class Report:
    skill: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def split_frontmatter(text: str) -> tuple[str, str] | None:
    """Return (yaml, body), or None when the file doesn't open with a '---' block on line 1."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        return None
    for i, line in enumerate(lines[1:], start=1):
        if line.rstrip("\r\n") == "---":
            return "".join(lines[1:i]), "".join(lines[i + 1:])
    return None


def check_name(meta: dict, folder: str, r: Report) -> None:
    name = meta.get("name")
    if name is None:
        r.errors.append("frontmatter has no `name` (required by the spec)")
        return
    if not isinstance(name, str):
        r.errors.append(f"`name` should be text, not {type(name).__name__}")
        return
    if not 1 <= len(name) <= 64:
        r.errors.append(f"`name` is {len(name)} characters; the spec allows 1-64")
    if not NAME_PATTERN.fullmatch(name):
        r.errors.append(f"`name` '{name}' may use only a-z, 0-9 and single hyphens between words")
    if name != folder:
        r.errors.append(f"`name` '{name}' differs from its folder '{folder}'")
    for word in ("anthropic", "claude"):
        if word in name:
            r.errors.append(f"`name` contains the reserved word '{word}'")


def check_description(meta: dict, r: Report) -> None:
    desc = meta.get("description")
    extra = meta.get("when_to_use")
    if not isinstance(desc, str) or not desc.strip():
        r.errors.append("`description` is missing or empty; Claude reads it to decide when to load the skill")
        return
    if len(desc) > 1024:
        r.errors.append(f"`description` is {len(desc)} characters; the limit is 1024")
    if extra is not None and not isinstance(extra, str):
        r.errors.append("`when_to_use` should be text")
        extra = None
    listing = desc + (extra or "")
    if len(listing) > 1536:
        r.warnings.append(f"`description` + `when_to_use` is {len(listing)} characters; "
                          "Claude Code cuts the listing at 1536, so the tail is never seen")
    if not TRIGGER_HINT.search(listing):
        r.warnings.append("the description doesn't say when to use the skill (e.g. 'Use when ...')")
    for key, value in (("name", meta.get("name")), ("description", desc), ("when_to_use", extra)):
        if isinstance(value, str) and XML_TAG.search(value):
            r.errors.append(f"`{key}` contains an XML tag, which the Claude API rejects")


def check_optional_fields(meta: dict, r: Report) -> None:
    for key in sorted(set(meta) - KNOWN_KEYS):
        r.warnings.append(f"unknown frontmatter key `{key}` is ignored by Claude Code (typo?)")

    compat = meta.get("compatibility")
    if compat is not None and not (isinstance(compat, str) and 1 <= len(compat) <= 500):
        r.errors.append("`compatibility` must be text of 1-500 characters")

    extras = meta.get("metadata")
    if extras is not None:
        if not isinstance(extras, dict):
            r.errors.append("`metadata` must be a key/value map")
        else:
            for k, v in extras.items():
                if not isinstance(v, str):
                    r.errors.append(f"`metadata.{k}` must be quoted text, e.g. {k}: \"{v}\"")

    for key in sorted(BOOLEAN_KEYS & set(meta)):
        value = meta[key]
        if not isinstance(value, bool) and str(value).lower() not in BOOLEAN_WORDS:
            r.errors.append(f"`{key}` must be true or false, got '{value}'")

    effort = meta.get("effort")
    if effort is not None and effort not in EFFORT_LEVELS:
        r.errors.append(f"`effort` must be one of {', '.join(sorted(EFFORT_LEVELS))}")
    if "context" in meta and meta["context"] != "fork":
        r.errors.append("`context` only accepts 'fork'")
    if "agent" in meta and meta.get("context") != "fork":
        r.warnings.append("`agent` has no effect unless `context: fork` is set")


def check_links(skill_dir: Path, r: Report) -> None:
    """Every relative link in the skill's markdown must land on a file inside the skill."""
    base = skill_dir.resolve()
    for doc in sorted(skill_dir.rglob("*.md")):
        prose = CODE_SPAN.sub("", doc.read_text(encoding="utf-8"))
        for target in MD_LINK.findall(prose):
            if EXTERNAL.match(target):
                continue
            file_part = unquote(target.partition("#")[0])
            dest = (doc.parent / file_part).resolve()
            where = doc.relative_to(skill_dir)
            if base != dest and base not in dest.parents:
                r.errors.append(f"{where}: link '{target}' leaves the skill folder, which isn't installed with it")
            elif not dest.exists():
                r.errors.append(f"{where}: link '{target}' points to a file that doesn't exist")


def check_skill(skill_dir: Path) -> Report:
    r = Report(skill_dir.name)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        found = [p.name for p in skill_dir.iterdir() if p.name.lower() == "skill.md"]
        r.errors.append(f"expected SKILL.md (exact case), found {found[0]}" if found else "no SKILL.md")
        return r

    raw = skill_md.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        r.errors.append("SKILL.md starts with a byte-order mark, which hides the frontmatter")
    parts = split_frontmatter(raw.decode("utf-8-sig"))
    if parts is None:
        r.errors.append("SKILL.md must open with a '---' frontmatter block on line 1, closed by another '---'")
        return r
    fm, body = parts

    try:
        meta = yaml.safe_load(fm) or {}
    except yaml.YAMLError as exc:
        r.errors.append(f"frontmatter isn't valid YAML, so Claude Code loads the skill with no fields: {exc}")
        return r
    if not isinstance(meta, dict):
        r.errors.append("frontmatter must be a YAML map of `key: value` lines")
        return r

    check_name(meta, skill_dir.name, r)
    check_description(meta, r)
    check_optional_fields(meta, r)

    if skill_dir.name.lower() == "synced":
        r.errors.append("the folder name 'synced' is reserved by Claude Code")
    body_lines = body.count("\n")
    if body_lines > 500:
        r.warnings.append(f"SKILL.md body is {body_lines} lines; keep it under 500 and move detail to references/")
    if (skill_dir / "README.md").exists():
        r.warnings.append("README.md inside a skill is never loaded; put that content in SKILL.md or references/")

    check_links(skill_dir, r)
    return r


def find_skills(target: Path) -> list[Path]:
    if any(p.name.lower() == "skill.md" for p in target.iterdir()):
        return [target]
    return sorted(d for d in target.iterdir()
                  if d.is_dir() and any(p.name.lower() == "skill.md" for p in d.iterdir()))


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Agent Skills against the spec and Claude Code rules.")
    parser.add_argument("paths", nargs="*", type=Path, default=[ROOT / "skills"],
                        help="skill folders, or folders that contain skills (default: ./skills)")
    parser.add_argument("--strict", action="store_true", help="fail on warnings too")
    args = parser.parse_args()

    skills: list[Path] = []
    for target in args.paths:
        if not target.is_dir():
            parser.error(f"not a folder: {target}")
        skills.extend(find_skills(target))
    if not skills:
        print("no skills found", file=sys.stderr)
        return 1

    reports = [check_skill(d) for d in skills]
    failing = 0
    for rep in reports:
        mark = "✗" if rep.errors else ("!" if rep.warnings else "✓")
        print(f"{mark} {rep.skill}")
        for msg in rep.errors:
            print(f"    error: {msg}")
        for msg in rep.warnings:
            print(f"    warning: {msg}")
        failing += bool(rep.errors or (args.strict and rep.warnings))

    errors = sum(len(rep.errors) for rep in reports)
    warnings = sum(len(rep.warnings) for rep in reports)
    print(f"\n{len(reports)} skill(s) checked: {errors} error(s), {warnings} warning(s)")
    return 1 if failing else 0


if __name__ == "__main__":
    sys.exit(main())

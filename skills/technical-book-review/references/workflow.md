# Workflow, finding format, and severity

## The two-pass shape

A review has up to three passes; which ones run depends on scope (see SKILL.md, "Start of every session").

### Chapter pass

For each chapter in scope:

1. Read it fully — not an excerpt, not a summary of it from memory.
2. Spot-check its claims. A claim inside a block the project's own tooling already guarantees matches the source needs no re-check (Pattern 2's exception). A claim written in prose — a count, a timeout, an exit code, a worked example's arithmetic, a described behavior — gets checked against the companion repo when one was given, by reading the real source, not by trusting what the chapter says about itself.
3. Apply whichever of the ten patterns fit this manuscript's state (references/patterns.md).
4. Log a finding for anything that fails a pattern's question. State a clean verdict plainly when nothing does — don't manufacture a finding to look thorough, and don't pad a clean chapter's report.

### Manuscript pass

Only for whole-manuscript scope, or an explicit request to review the whole book after the chapters. This is Pattern 8 (Cross-Chapter Consistency) run across the full text instead of within one chapter:

1. Grep the whole manuscript for every claim that's plausibly repeated: a count, a name, a version, a glossary entry restating a chapter's claim, a "chapter N describes..." cross-reference.
2. Diff each repeat against its other occurrences and against the chapter pass's own findings. A contradiction here is invisible from inside any single chapter — that's the pass's whole purpose.
3. Give a plain-language readiness read at the end: not a score, a sentence on whether what's left standing is the kind of thing that should block release.

### Fix-and-reverify pass

Only once the author confirms a finding should be fixed:

1. Apply the fix.
2. If the fix touches a claim repeated elsewhere (caught in the manuscript pass, or plausibly shared), re-check those other occurrences too.
3. Re-run whatever the project already uses to check itself: its test suite, its own fact-checking or excerpt-verification tooling, a full build. A fix is not done until this re-run is clean.
4. Report what changed and what was re-run — not just "fixed."

## Finding format

Every finding carries these fields. Without all four — evidence, impact, recommendation, and a location — it's an observation, not a finding, and shouldn't be counted as one.

```yaml
id: REV-005
chapter: 5
section: Server-Sent Events
severity: major
pattern: claim-verification     # which of the ten patterns (or lens) surfaced it
problem: The example does not handle client cancellation correctly.
evidence: "internal/stream.go:142 — the loop keeps writing after ctx.Done() fires; the chapter's prose says it stops"
impact: A reader who follows the example reproduces a goroutine leak under normal use (a client closing its tab).
recommendation: Select on r.Context().Done() in the write loop, and say so in the prose.
verification: unverified until the author applies the fix and the suite's SSE test is re-run
```

The same fields work in prose for a conversational reply — the structure, not the YAML, is what matters.

## Severity

| Severity | Meaning | Expected response |
|---|---|---|
| Critical | Incorrect or unsafe guidance a reader could act on | Block release until resolved |
| Major | A significant technical, architectural, or instructional weakness | Fix before release unless the author explicitly accepts the risk |
| Minor | A localized inconsistency or less consequential error | Fix as part of normal revision |
| Suggestion | An optional improvement to presentation, examples, or coverage | The author's call |

Never let an average hide a Critical finding — that's the specific failure the severity scale exists to prevent (see SKILL.md, "The one real judgment call," on skipping the weighted scorecard by default).

## The scorecard, when asked for one

Only build this when the author explicitly wants a go/no-go number against an outside bar (an external publisher's gate, a self-imposed release checklist):

| Category | Weight | Focus |
|---|---:|---|
| Technical accuracy | 30% | Correct facts, terminology, APIs, claims |
| Code and examples | 25% | Compiling, execution, reproducibility, safety |
| Clarity and pedagogy | 20% | Explanation quality, prerequisites, progression |
| Architecture and patterns | 10% | Design choices, diagrams, trade-offs |
| Scope and completeness | 10% | Coverage and disclosed limitations |
| Consistency and presentation | 5% | Terminology, references, structure |

Score each 1 (poor) to 5 (excellent); weighted total = `SUM(category_score / 5 × weight%)`. State explicitly that a high score does not clear an open Critical finding.

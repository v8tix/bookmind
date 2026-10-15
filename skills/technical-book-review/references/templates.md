# Templates

## findings.md

Lives at `<output>/<manuscript-name>/findings.md`. One file, kept current across sessions.

```markdown
# Review of <manuscript name>

Companion repo: <path, and pin if one is cited> (or: none — claims checked against general knowledge only)
Resume point: <chapter/section, or "whole-manuscript pass", or "done">

## Findings

| id | chapter | severity | status | problem | evidence | recommendation |
|---|---|---|---|---|---|---|
| REV-001 | 5 | major | open | ... | ... | ... |
| REV-002 | 12 | minor | fixed | ... | ... | ... |

## Clean chapters

Chapters read with no findings: 1, 2, 3, 4, 6–11, 13–18.

## Manuscript-pass notes

(Cross-chapter checks: repeated claims found, any that disagreed, when the pass last ran.)
```

- `status` is `open`, `fixed`, or `skipped` (skipped: the author decided not to fix it — say why in the row).
- Update the row's status the moment the author decides, not at the end of the session.
- "Clean chapters" lets a resumed session skip re-reading what already passed, unless the manuscript or the companion repo changed since.
- Append to this file; don't rewrite history that's already settled, the same way a lab notebook gets new dated entries rather than edits to old ones.

## A finding, in conversation

When reporting inline rather than to a log, keep the same four fields, compressed:

> **Chapter 5, major.** The streaming example doesn't handle client cancellation: the write loop in `internal/stream.go:142` keeps running after the request context ends, though the prose says it stops. A reader who follows this reproduces a goroutine leak on an ordinary closed tab. Recommend selecting on `r.Context().Done()` in the loop, and correcting the prose claim.

## End-of-pass summary

Don't restate every clean verdict. One line per clean chapter is enough; spend the space on what's actually open:

> Chapters 1–15 clean. Chapter 16: one minor finding (a stale key count in `.env.example`, now logged as REV-003). Chapters 17–18 not yet reviewed under this pass.

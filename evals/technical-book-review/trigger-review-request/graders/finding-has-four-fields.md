---
type: llm
---
The skill's own rules (SKILL.md, references/workflow.md) require every finding to carry four fields: evidence, impact, recommendation, and a severity/location.

PASS if the reported finding about the retry-count mismatch includes, in some form: (1) evidence pointing at a specific file or line (`retry.go` or the constant name), (2) an impact or consequence for a reader, (3) a concrete recommendation (e.g., change "five" to "three" in the chapter, or change the constant), and (4) a severity label (such as minor, major, critical, or suggestion).
FAIL if any of the four is missing.
FAIL if the finding reads as a bare observation ("this seems off") with no recommendation.

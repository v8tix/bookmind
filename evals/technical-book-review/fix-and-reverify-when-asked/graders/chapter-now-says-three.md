---
type: llm
---
The chapter originally claimed the client makes at most five retry attempts; the code allows three (`const MaxRetries = 3`). The user asked Claude to fix the chapter's prose to match the code.

PASS if, by the end, the chapter's text (quoted in the reply, or described as edited) now says three attempts rather than five, and the one-connection-reuse claim (which was already correct) was left alone.
FAIL if the chapter still says five, or if the reply changed the number to something other than three.
FAIL if the reply changed the code (`retry.go`) instead of the chapter's prose.

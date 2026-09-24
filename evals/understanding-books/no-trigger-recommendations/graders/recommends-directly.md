---
type: llm
---
The user asked: "Recommend me some good books on distributed systems." Judge whether the reply answers with recommendations right away.

PASS if the reply names at least three specific books about distributed systems by title (authors optional).
PASS if the reply also asks one or two optional follow-up questions about the user's background or goals, as long as the book titles are already given in this reply.
FAIL if the reply names fewer than three specific book titles.
FAIL if the reply holds back recommendations until the user answers intake questions, for example about purpose, depth, deadline, time per week, or retention goals.

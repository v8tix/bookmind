---
type: llm
---
The user asked only for book recommendations on distributed systems. Judge whether the reply stays a recommendation answer instead of turning into a study program.

PASS if the reply is a set of book recommendations, optionally with short reasons, grouping by level, or a suggested reading order.
FAIL if the reply sets up a study protocol for any of the books: prequestions for the user to guess at, retrieval or recall prompts, a concept map to build from memory, or a spaced-review schedule.
FAIL if the reply offers to create a study folder, a review file, or a flashcard deck for the books.
FAIL if the reply tags its statements with provenance labels such as "Author:", "Context:", "Reader:", or "Inference:".

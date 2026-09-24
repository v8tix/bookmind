---
type: llm
---
The user is the author of a book they have not written yet and asked for help outlining it. Judge whether the reply wrongly treats this as studying or retaining an existing book.

PASS if the reply stays a writing collaboration: structure, chapter ideas, framing, audience, or next writing steps. Stating a central message or thesis for the user's own book is fine.
FAIL if the reply asks the user to guess answers to prequestions, to answer recall or retrieval questions from memory, or to build a concept map from memory.
FAIL if the reply proposes a spaced-review schedule, review dates, flashcards, or a study folder (for example books/<slug>/review.md).
FAIL if the reply tags statements with provenance labels such as "Author:", "Context:", "Reader:", or "Inference:", or describes a reading or study protocol for a book.

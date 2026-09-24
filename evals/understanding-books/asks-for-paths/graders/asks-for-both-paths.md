---
type: llm
---
The user asked for help studying chapter 2 of a book, but gave no book file and no folder for saving notes.

PASS if the reply does all four:
(1) asks for the book itself as a file or folder path (a request for pasted text or excerpts as an alternative is fine);
(2) asks for an output folder where notes or the study folder will be saved;
(3) gives a short reason for needing each one, for example working from the real text and its pages, and saving notes where the next session can find them;
(4) does not start the study: no prequestions about the chapter's content, no summary, and no study plan.

FAIL if either path is not asked for.
FAIL if the reply picks or proposes a default location on its own (for example "I'll save everything in ./books/") instead of asking.
FAIL if the reply searches for or claims to have found the book on its own.
FAIL if it asks without giving any reason for either path.

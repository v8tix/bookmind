---
type: llm
---
The user asked for the help of a book-study skill, without naming a book or a task.

PASS if the reply presents CLI-style help, like a command-line tool's `--help` output, that does all four:
(1) shows how to invoke the skill (a usage line);
(2) names the two required inputs: the book file or folder, and the notes (output) folder;
(3) lists optional settings such as mode, depth, and deadline;
(4) gives at least two example prompts.

FAIL if any of the four is missing.
FAIL if the reply asks the user for a book path or notes folder, as if starting a study session.
FAIL if the reply starts studying, summarizing, or analyzing a book.

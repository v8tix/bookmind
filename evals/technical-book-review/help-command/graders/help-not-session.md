---
type: llm
---
The user asked for the help of a manuscript-review skill, without naming a manuscript or a task.

PASS if the reply presents CLI-style help, like a command-line tool's `--help` output, that does all four:
(1) shows how to invoke the skill (a usage line);
(2) names the required input: the manuscript;
(3) lists optional settings such as a companion repository, scope, and output;
(4) gives at least two example prompts.

FAIL if any of the four is missing.
FAIL if the reply asks the user for a manuscript path, as if starting a review session.
FAIL if the reply starts reviewing, critiquing, or fact-checking anything.

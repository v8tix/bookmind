---
type: llm
---
The user said plainly that they will not have time to read the chapter, but want to remember its ideas. You are grading whether the reply respects that.

PASS if the reply plans for the user not reading the chapter, for example by saying Claude will provide a brief or summary of the chapter after the user's guesses.
PASS if the reply offers reading the chapter only as an optional extra (for example "if you do find 10 minutes, section 4.2 is the one to read").
FAIL if the reply tells the user to read the chapter, or part of it, as a required next step before continuing.
FAIL if the reply's plan depends on the user having read the chapter, for example asking them to look for the answers while reading it.

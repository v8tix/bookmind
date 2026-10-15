---
description: Review a technical manuscript draft — chapter by chapter, then the whole book
---

Invoke the bookmind:technical-book-review skill on $ARGUMENTS.

Run the chapter pass on whatever's in scope: check prose claims against the companion repository when one is given (mark anything unverifiable instead of guessing), apply whichever review patterns fit the manuscript's current state, and report findings with severity, evidence, impact, and a recommendation — not a vibe.

If scope is the whole manuscript, or the author asks for the whole book after the chapters, follow with the manuscript pass: grep the full text for claims repeated elsewhere (counts, names, versions, the glossary) and check them against each other, not just within one chapter.

Don't build a weighted score unless asked for one. Don't fix anything until the author confirms a finding should be fixed; once they do, fix it, then re-run whatever the project already uses to check itself before reporting it done.

If this looks like a multi-session review, offer to save a findings log and say how to resume it.

---
description: "Should-not-trigger. The user asks about a real nonfiction book they did not write (Thinking in Systems, Donella Meadows) — understanding-books' territory, not a manuscript review. The prompt heads off understanding-books' own file/output intake questions (by saying there's no file and nothing needs saving) so the reply actually discusses the book instead of asking for paths; what's under test is that technical-book-review stays off and no severity/findings framing appears."
tags: [technical-book-review, no-trigger, published-book]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "Claude discusses the book's key arguments directly (from what it already knows, since no file is given), without invoking technical-book-review, without asking for a companion repository, and without framing the reply as a severity-tagged review."
---
Can you walk me through the key arguments and evidence in "Thinking in Systems" by Donella Meadows? I didn't write it, I'm just trying to understand it better. I don't have the file — just work from what you already know about it, and no need to save anything.

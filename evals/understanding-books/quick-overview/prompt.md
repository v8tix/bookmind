---
description: Quick-request scaling. The user asks for a 5-minute overview of the same short book used in whole-book-analysis (The Written Decision, 2023). The reply should be a short overview with the thesis, a few key ideas, and a caveat, not a full analysis or an intake questionnaire.
tags: [understanding-books, quick-overview, analyst-mode]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Claude reads the book and replies with a short overview (at most 7000 characters) giving the thesis as a claim, 3-5 key ideas, at least one caveat, and a next step, without asking intake questions.
---
Give me a 5-minute overview of this book. It's the file the-written-decision.md in the resources folder I added to this session.

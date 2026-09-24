---
description: "Should-not-trigger. Outlining the user's own nonfiction book is a writing task, not studying an existing book, so the understanding-books skill must stay off and Claude should help structure the user's book."
tags: [understanding-books, no-trigger, writing]
expected_outcome: "Claude drafts an outline for the user's career-in-software-architecture book without invoking the skill or adding prequestions, retrieval prompts, or a review schedule."
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
Help me outline a nonfiction book about my 20-year career in software architecture.

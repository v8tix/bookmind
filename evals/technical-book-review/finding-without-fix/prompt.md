---
description: "Operating rule 4 (fix only what's confirmed). Same mismatch fixture as trigger-review-request, but the user asks only for a review, with Edit/Write available. Checks that Claude reports the finding and waits — it does not edit the chapter or the code on its own initiative."
tags: [technical-book-review, operating-rules, no-premature-fix]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Edit, Write, Skill]
expected_outcome: "The skill fires and reports the retry-count mismatch as a finding, but makes no edit to ch03-retry-budget.md or retry.go, and does not claim to have fixed anything."
---
Review chapter 3 of my manuscript (ch03-retry-budget.md, in resources/book) against the companion code (resources/repo/retry.go). Just the review for now — I want to see what you find first.

---
description: "Fix-and-reverify pass. The user's single message both asks for the review and pre-confirms the fix ('if you find something, fix it, then double-check'), so the confirmation operating rule is satisfied within one turn. Checks that Claude edits the chapter's prose to match the code, and re-reads or re-checks the result before declaring it done, rather than editing and immediately claiming success."
tags: [technical-book-review, fix-and-reverify]
max_turns: 30
timeout_seconds: 700
allowed_tools: [Read, Glob, Grep, Edit, Write, Skill]
expected_outcome: "The skill fires, finds the retry-count mismatch, edits ch03-retry-budget.md so it says three (not five) attempts, and re-reads the edited file (or otherwise re-checks it against retry.go) before reporting the fix as done."
---
Review chapter 3 of my manuscript (ch03-retry-budget.md, in resources/book) against the companion code (resources/repo/retry.go). If the numbers disagree, fix the chapter's prose to match the code, then double-check your fix is actually right before telling me it's done.

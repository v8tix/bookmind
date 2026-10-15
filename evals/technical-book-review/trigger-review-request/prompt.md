---
description: "Core trigger. The user asks for a technical review of one chapter of a manuscript they're writing, against a companion code repo added as a resource. The chapter's attempt count (five) disagrees with the real code (three); a true distractor claim (one connection kept open across attempts) matches the code. Checks Pattern 1 (Claim Verification) and the finding format."
tags: [technical-book-review, trigger, claim-verification]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; Claude reads ch03-retry-budget.md and retry.go, reports a finding that the chapter's 'five attempts' disagrees with the code's MaxRetries = 3, with evidence naming the file, a severity, and a recommendation, and does not also flag the one-connection claim as wrong."
---
I'm writing a short technical book about a message-queue client. Can you give chapter 3 a technical review? It's the file ch03-retry-budget.md in the resources/book folder. The companion code it's about is in resources/repo/retry.go — no pinned commit, it's just the current working copy.

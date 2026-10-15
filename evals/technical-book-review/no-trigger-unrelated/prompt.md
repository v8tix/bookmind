---
description: "Should-not-trigger. An ordinary coding question with no manuscript or book involved at all. technical-book-review must stay off and Claude should just answer the question."
tags: [technical-book-review, no-trigger, unrelated]
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "Claude answers the Dockerfile question directly, without invoking technical-book-review or asking about a manuscript."
---
What's a good minimal Dockerfile base image for a small, statically-linked Go binary?

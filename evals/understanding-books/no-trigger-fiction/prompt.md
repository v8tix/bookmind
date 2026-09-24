---
description: "Should-not-trigger. A literary question about a novel is out of scope for the nonfiction study skill, so the understanding-books skill must stay off and Claude should answer the question directly."
tags: [understanding-books, no-trigger, fiction]
expected_outcome: "Claude names and briefly supports a main theme of The Great Gatsby without invoking the skill or imposing thesis/evidence, falsifiable-experiment, or study-plan framing."
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
What's the main theme of The Great Gatsby?

---
description: "Should-not-trigger. Asking for book recommendations is not a request to study, analyze, or retain a book, so the understanding-books skill must stay off and Claude should simply recommend books."
tags: [understanding-books, no-trigger, recommendations]
expected_outcome: "Claude names several specific distributed-systems books right away, without invoking the skill, running an intake questionnaire, or setting up a study protocol."
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
Recommend me some good books on distributed systems.

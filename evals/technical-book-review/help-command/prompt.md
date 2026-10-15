---
description: "Help request. The user asks for the technical-book-review skill's help, with no manuscript and no task. Checks the Help section of SKILL.md: the reply is the CLI-style help from references/help.md, and Claude neither asks for a manuscript nor starts a review."
tags: [technical-book-review, help]
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; the reply is the CLI-style help (usage, required MANUSCRIPT, optional settings, session phrases, examples, findings-log file) in a code block, with no question about a manuscript and no review started."
---
Show me the help for BookMind's technical-book-review skill: what it needs and how I use it.

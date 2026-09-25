---
description: "Help request. The user asks for the understanding-books skill's help, with no book and no task. Checks the Help section of SKILL.md: the reply is the CLI-style help from references/help.md, and Claude neither asks for paths nor starts a study."
tags: [understanding-books, help]
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; the reply is the CLI-style help (usage, required INPUT and OUTPUT, optional settings, session phrases, examples, study-folder files) in a code block, with no question about paths and no study started."
---
Show me the help for BookMind's understanding-books skill: what inputs it needs and how I use it.

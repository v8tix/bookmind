---
description: "Missing paths. The user asks for help studying a chapter but gives neither the book file nor an output folder. Checks the first step of SKILL.md: the first reply asks for both, says why each is needed, and does not start the study."
tags: [understanding-books, paths, intake]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; the reply asks for the book file or folder and for an output folder, gives a short reason for each, and does not start the task (no prequestions, summary, or plan) or pick a folder itself."
---
Help me really understand chapter 2 of the book I'm reading. I want to still remember it next month.

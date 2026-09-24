---
description: A reader asks for help studying a chapter for an interview but explicitly refuses quizzes and asks for the answers straight away. The reader controls the mode, so the answers should come at once, with no prequestions, guesses, or hints first.
tags: [understanding-books, guided-mode, mode-switch]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: Skill fires; the reply answers both questions from the chapter at once (the problem leader election solves; that timeouts detect silence and buy only liveness while quorums and terms give safety), with no quiz, guess request, or hint before the answers.
---
Help me study chapter 3 of Reliable by Agreement so I still remember it for a system design interview next month. It's the file ch3-leader-election.md in the resources folder I added to this session. But skip the quizzes and guessing games, I just want the answers straight: what problem does leader election solve, and what does the chapter say you can and can't rely on timeouts for?

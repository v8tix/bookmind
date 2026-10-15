---
description: "Manuscript (whole-book) pass. Chapter 2 says there are four safety limits; the glossary, elsewhere in the same manuscript, says three. Neither file alone looks wrong — the inconsistency only shows up when the two are compared. The companion repo (writer.go) confirms four is correct. Checks Pattern 8 / the manuscript pass in references/workflow.md."
tags: [technical-book-review, cross-chapter-consistency, manuscript-pass]
max_turns: 30
timeout_seconds: 700
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires, reviews chapter 2 and the glossary, then runs the whole-manuscript pass and reports a finding that the glossary's 'three' disagrees with chapter 2's 'four' (and with SafetyLimitCount = 4 in writer.go), recommending the glossary be corrected to four."
---
Review this whole manuscript — chapter 2 (ch02-safety-limits.md) and the glossary (glossary.md), both in resources/book2 — against the code in resources/book2/repo/writer.go. Do it chapter by chapter, then the whole thing, like we talked about.

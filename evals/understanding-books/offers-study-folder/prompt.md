---
description: "Positive, retention goal. The user wants to learn one chapter (fixture ch4-invalidation-contract.md, a fictional caching chapter on pp. 87-93 whose thesis is that invalidation belongs to the owner of the write and a TTL is only a backstop) and remember it for months. Checks that Claude offers a persistent study record with review prompts and that any review dates are absolute calendar dates."
tags: [understanding-books, study-folder, spaced-review]
expected_outcome: "The skill fires; the first reply offers to keep a study folder or equivalent saved record of review prompts so a later session can continue, and any review dates it gives are calendar dates rather than only 'day 7'-style offsets."
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---
I want to really learn this chapter and still remember it in a few months. It's the file ch4-invalidation-contract.md in the resources folder I added to this session. Keep my notes in the study-notes folder.

---
description: "Hybrid mode. The user will not read a caching chapter (fixture ch4-invalidation-contract.md, Hard Things in Soft Systems, pp. 87-93) but wants to remember its ideas for a couple of months. Checks that the first reply asks chapter-specific prequestions to guess at before giving the chapter brief, and does not tell the user to read the chapter."
tags: [understanding-books, hybrid-mode]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; the first reply poses 2-5 invalidation-specific questions for the user to guess at and stops, without first laying out the chapter's conclusions and without telling the user to go read the chapter."
---
My team is redesigning our caching layer next month. Someone recommended chapter 4 of Hard Things in Soft Systems, but I honestly won't have time to read it. I don't just want a summary I'll forget, though: I want to actually remember the ideas over the next couple of months so I can use them in design reviews. The chapter is the file ch4-invalidation-contract.md in the resources folder I added to this session.

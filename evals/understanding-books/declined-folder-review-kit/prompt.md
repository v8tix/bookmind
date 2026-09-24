---
description: "Declined study folder. The user has read a caching chapter (fixture ch4-invalidation-contract.md, pp. 87-93), gives a from-memory recall with three errors (update the cache on write; size the TTL by freshness; watch hit ratio), refuses any files, and is ending the session. Checks feedback against the source and the portable review kit from SKILL.md: dated prompts, answer keys kept apart and marked for Claude, and a request to paste it back next time."
tags: [understanding-books, guided-mode, spaced-review, review-kit]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; Claude corrects the recall errors against the chapter, creates no files and does not push a study folder again, and ends with a review kit: review prompts with absolute dates, answer keys in a separate block for Claude, and a request to paste the kit at the next review."
---
I just finished reading chapter 4 of Hard Things in Soft Systems (it's ch4-invalidation-contract.md in the resources folder I added to this session) and I want to remember it for the next few months. Please don't create any files or folders on my computer, I don't want a study folder.

Here's what I remember, from memory: The author says caches go wrong when nobody owns invalidation. There are three approaches: TTL expiry, updating the cache when you write to the database, and invalidating from events. For writes, you should update the cached value with the new one so readers never miss. You should keep a TTL on everything and set it by how fresh the data needs to be. And you should monitor your hit ratio to know the cache is healthy.

I have to leave in ten minutes. Can you check what I got right and wrong, and give me whatever I need to review this later?

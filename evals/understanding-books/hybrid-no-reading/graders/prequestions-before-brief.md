---
type: llm
---
The user will not read chapter 4 ("Invalidation Is a Contract, Not a Timer") of a book on caching, but wants to remember its ideas for a couple of months. The right approach is to have the user guess at a few questions first and only then give a chapter brief. You are grading the assistant's first reply.

Reference, the chapter's conclusions: invalidation belongs to whoever owns the write; a TTL is only a backstop, sized to how long you can tolerate an invalidation bug rather than to freshness; delete the cache key on write rather than updating it, because racing writers can leave an older value; event-driven invalidation from the commit log scales with many writers, at the cost of lag; a staleness budget per class of data decides which mechanism to use; and staleness should be measured directly, because hit ratio does not show correctness.

Count only questions the reply asks the user to guess at or think about now. Ignore setup or logistics questions (depth, deadline, study folder).

PASS if the reply poses between 2 and 5 such questions, at least 2 of them name a concept specific to this chapter (for example TTLs, deleting versus updating on write, who owns invalidation, staleness, commit-log or event-driven invalidation), and the reply then stops to wait for the user's guesses.
PASS even if the reply gives a short orientation (the chapter's topic, its sections, or where it fits in the book), as long as it does not state the conclusions listed above.
A question does not count as stating a conclusion just because it names a concept; only statements that give the answer count.
FAIL if the reply explains two or more of the conclusions listed above before the user has guessed, for example by giving the chapter brief or a summary first.
FAIL if the reply poses fewer than 2 or more than 5 such questions, or never asks the user to guess.

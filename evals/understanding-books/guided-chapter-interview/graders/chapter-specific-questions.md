---
type: llm
---
The user asked for help studying chapter 3 ("Leader Election") of a distributed-systems book before reading it. The chapter covers: terms (term numbers), voting once per term and persisting the vote, majority quorums, split brain during a network partition, what a stale old leader can and cannot do, fencing with the term number, leases and clock drift, heartbeats and randomized election timeouts, and the trade-off between fast failover and stable leadership ("leader churn").

Count only the questions the reply asks the user to guess at before reading, or to keep in mind and answer while reading. Ignore setup or logistics questions (depth, time available, study folder, what the interview is like). If the reply also previews later prompts in a separate section (for example "after you read, I'll ask you to explain..."), do not count those.

PASS if the reply poses between 2 and 5 such questions (inclusive), and at least 2 of them name a concept specific to this chapter from the list above.
FAIL if the reply poses fewer than 2 or more than 5 such questions.
FAIL if fewer than 2 of the questions mention a leader-election concept, for example because they are generic templates that would fit any chapter ("What is the author's main claim?", "What evidence does the author give?").

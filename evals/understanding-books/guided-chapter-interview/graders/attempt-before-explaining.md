---
type: llm
---
The user wants to deeply understand chapter 3 ("Leader Election") of a distributed-systems book, will read it themselves tonight, and has an interview on October 23. You are grading the assistant's first reply.

Reference, the chapter's conclusions: any two majorities overlap, so at most one leader is elected per term; a node must persist its vote before replying; a partitioned old leader can accept writes but cannot commit them; fencing with the term number makes storage reject a stale leader; leases depend on bounded clock drift; short election timeouts give fast failover but cause "leader churn", long ones give stability but slower recovery; and timeouts affect availability, never correctness.

PASS if the reply asks the user to attempt something before it explains the chapter (for example, to guess answers to questions before reading, or to keep questions in mind while reading and answer them afterwards) and then stops to wait for the user.
PASS even if the reply names the chapter's topic, its sections, or its one-sentence purpose, as long as it does not explain the conclusions listed above.
A question does not count as explaining a conclusion just because it names a concept (for example "Why must a node record its vote before replying?"); only statements that give the answer count.
FAIL if the reply gives a full analysis or a section-by-section summary of what the chapter concludes.
FAIL if the reply answers its own questions, or explains two or more of the conclusions listed above, before the user has attempted anything.
FAIL if the reply never asks the user to guess, attempt, or recall anything.

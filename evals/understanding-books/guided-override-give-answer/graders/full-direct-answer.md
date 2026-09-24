---
type: llm
---
The user is studying chapter 3 (leader election) of a distributed-systems book and asked for straight answers to two questions: what problem leader election solves, and what the chapter says you can and cannot rely on timeouts for.

The chapter's answers are:
1. Problem: a replicated log needs someone to decide the order of commands; the cluster chooses a single leader, notices when it is gone, and keeps two nodes from both acting as leader (split brain).
2. Timeouts: a timeout detects silence, not death (a paused or slow leader looks crashed); timeouts only decide how fast the cluster recovers (liveness, failover speed vs leader churn), never whether it is correct; safety comes from majority quorums and terms. Leases are the exception whose safety depends on bounded clock drift.

PASS if the reply answers BOTH questions in substance: part 1 in any clear wording, and part 2 including that timeouts cannot guarantee safety or correctness (or that safety comes from quorums/terms rather than timeouts).

FAIL if either answer is missing, only hinted at, or postponed until the user attempts it.
FAIL if part 2 only says timeouts detect failures without saying they cannot guarantee safety.

# Reliable by Agreement: Consensus for Working Engineers

Priya Castellanos-Winter · Larkspur Technical Press · 2nd edition, 2025

---

# Chapter 3 — Leader Election

— p. 61 —

Chapter 2 argued that a replicated log is the simplest way to keep several machines in agreement: if every replica applies the same commands in the same order, every replica ends in the same state. It left one question open. Someone has to decide the order. In most practical systems that someone is a single node, the leader, and this chapter is about how a cluster chooses one, how it notices when the leader is gone, and how it keeps two nodes from both believing they are in charge.

The chapter's claim fits in one sentence, and the rest of the chapter defends it: **safety comes from quorums and terms; timeouts only buy liveness.** A cluster may be slow to elect a leader, or elect one too often, and still be correct. It must never let two leaders commit conflicting entries, and no choice of timeout can guarantee that on its own.

## 3.1 Terms: numbering the reigns

Time in a cluster is divided into **terms**, numbered with consecutive integers. Each term begins with an election. If a candidate wins, it leads for the rest of the term; if the vote splits, the term ends without a leader and a new term begins.

Every message carries the sender's current term. The rules are short:

1. A node that sees a higher term than its own adopts that term immediately and, if it was a leader or candidate, steps down to follower.
2. A node rejects any request that carries a lower term than its own.
3. A node votes for at most one candidate per term, and records that vote on disk before replying.

— p. 62 —

Terms act as a logical clock. They do not tell you what time it is; they tell you whose authority is newer. Rule 3 is the one engineers most often break in practice. A node that votes, crashes before persisting the vote, restarts, and votes again for a different candidate in the same term has just made two leaders possible.

## 3.2 Majority quorums

A candidate becomes leader when it collects votes from a **majority** of the full cluster — three of five, four of seven — counting its own vote. The same majority rule governs commits: an entry is committed once a majority has stored it.

The reason is arithmetic, not convention. Any two majorities of the same cluster share at least one node. If two candidates each gathered a majority in the same term, some node would have voted twice, which rule 3 forbids. So there is at most one leader per term. The same overlap is why a new leader cannot miss a committed entry: the majority that elected it includes at least one node from the majority that stored the entry, and a node refuses its vote to a candidate whose log is less up to date than its own.

Notice what this costs. A five-node cluster tolerates two failures, not four. A four-node cluster still needs three votes and so tolerates only one failure, the same as a three-node cluster. Adding a node to an odd-sized cluster buys nothing but a larger bill.

— p. 63 —

## 3.3 Split brain

Split brain is the failure this chapter exists to prevent: two nodes both acting as leader and accepting writes that conflict. It usually starts with a network partition. Suppose a five-node cluster splits into a group of two, which includes the current leader of term 7, and a group of three.

The three nodes stop hearing heartbeats, time out, and elect a new leader in term 8. They have a majority, so the election is legitimate. The old leader, cut off, knows none of this. It still believes it leads term 7 and may keep accepting client writes.

This is where quorums earn their keep. The old leader can accept writes, but it cannot commit them: committing needs acknowledgments from three nodes, and it can reach only two. Its uncommitted entries are overwritten when the partition heals and it sees term 8. Clients that wrote to it get timeouts, not false confirmations.

— p. 64 —

The danger returns when a system cuts corners. The two common shortcuts are serving reads from the leader's local state without checking with a majority, and letting the leader perform side effects outside the log, such as writing to external storage. For both, I recommend **fencing**: every action outside the log carries the leader's term, and the receiving system rejects any term lower than the highest it has seen. The stale leader from term 7 is then refused by storage that has already seen term 8.

Some systems avoid a majority round trip on reads by giving the leader a time-based **lease**: followers promise not to elect anyone else for, say, two seconds after their last acknowledgment. Leases are fast, but they are the one place where this chapter's claim bends, because their safety rests on bounded clock drift between machines. If a paused virtual machine resumes with a stale clock, a lease can outlive its welcome. Use leases only where you can bound drift, and prefer fencing where you cannot.

## 3.4 Failure detection and timeouts

A follower cannot see that the leader has crashed. It can only see that it has not heard from the leader lately. Leaders therefore send **heartbeats** at a fixed interval — 50 ms is common — and a follower that hears nothing for a full **election timeout** becomes a candidate.

— p. 65 —

Two details matter. First, election timeouts are **randomized**, for example anywhere between 150 and 300 ms, so that followers rarely time out at the same instant and split the vote. Second, a timeout detects silence, not death. A leader in a long garbage-collection pause, behind a saturated network link, or waiting on an overloaded disk looks exactly like a crashed leader.

## 3.5 The trade-off: fast failover or stable leadership

Choosing the election timeout is the chapter's central trade-off.

A short timeout gives fast failover: when the leader really dies, the cluster is unavailable for writes only briefly. But it also produces false suspicions. Every pause longer than the timeout triggers an election, the healthy leader is deposed, in-flight requests fail, and under load the cluster can spend its time electing leaders instead of serving clients. I call this **leader churn**.

A long timeout gives stable leadership and tolerates pauses and jitter, but every real crash now costs a longer window with no leader.

Correctness is not on the table in either case. Because of terms and quorums, a timeout that is too short makes the cluster slow and noisy, never inconsistent. That is the practical meaning of the chapter's claim: tune timeouts for availability, and never rely on them for safety.

My rule of thumb is to set the election timeout to at least ten times the 99th-percentile heartbeat round-trip time, and to measure that percentile under peak load rather than on an idle cluster.

— p. 66 —

## Summary

- Terms order leaders in time; a node votes once per term and remembers its vote across crashes.
- Any two majorities intersect, so at most one leader per term can be elected, and committed entries survive leader changes.
- A partitioned old leader can accept writes but cannot commit them; fencing tokens and careful reads close the remaining gaps.
- Leases trade a majority round trip for an assumption about clocks.
- Timeouts decide how quickly a cluster recovers and how often it panics; they never decide whether it is correct.

Chapter 4 turns to log replication: what the leader does once it has been elected.

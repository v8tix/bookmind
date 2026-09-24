# Review: The Stale Read: Caches That Tell the Truth

Horizon: long-term

Due: prompts whose Status is active or stable and whose Next date is today or earlier. Ask the oldest Next first; within a date, prompts that were failed or partial last time. The Log is history only; never work out due prompts from it.

## Prompts
| ID | Prompt | Type | Status | Streak | Last | Next |
|---|---|---|---|---|---|---|
| c3-01 | Why can't a TTL alone bound how stale a cached read can be when the writer's and the cache's clocks disagree, and what bound does the author put in its place? | recall | active | 1 | 2026-09-10 | 2026-09-16 |
| c3-02 | How can a correct delete-on-write invalidation still leave a stale value in the cache, and what mechanism does the author use to stop it? | recall | active | 0 | 2026-09-10 | 2026-09-15 |
| c3-03 | Your team broadcasts every invalidation to all 200 cache nodes, and the message bus saturates during a bulk import. Using chapter 3, what would you change, and what does the change cost? | scenario | active | 1 | 2026-09-10 | 2026-09-16 |
| c3-04 | A read replica lags 4 seconds behind the primary. Why can invalidating the cache on every write still let stale data back in, and what ordering does the author recommend? | scenario | active | 0 | 2026-09-10 | 2026-09-15 |
| c3-05 | A colleague says, "Just use short TTLs and skip invalidation entirely." What is the author's strongest reply? | objection | active | 1 | 2026-09-10 | 2026-09-16 |

## Log
| Date | ID | First-attempt result | Main gap |
|---|---|---|---|
| 2026-09-10 | c3-01 | correct | |
| 2026-09-10 | c3-02 | failed | Described the race but could not name or explain the fix |
| 2026-09-10 | c3-03 | correct | |
| 2026-09-10 | c3-04 | partial | Right symptom, wrong cause; gave no ordering fix |
| 2026-09-10 | c3-05 | correct | |

## Answer keys (read only after answering)
| ID | Answer key (short, with location) |
|---|---|
| c3-01 | Expiry is judged on the cache's own clock, so clock skew stretches the window; worst-case staleness = TTL + maximum writer-to-cache skew, which she names the Oduya bound (ch. 3, p. 87). |
| c3-02 | A slow reader loads the old row before the write, the delete lands, then the reader fills the old value. Fix: a tombstone lease, a short-lived versioned marker left by the delete; any fill older than the marker is refused (ch. 3, pp. 92–94). |
| c3-03 | Send each invalidation only to the nodes that hold the key, tracked in a subscription directory (her herald fan-out). Cost: the directory is new state that must itself stay consistent, and it adds a hop (ch. 3, pp. 98–101). |
| c3-04 | The next miss refills from the lagging replica and re-caches the old value (the quiet-replica trap). Invalidate only after the replica has applied the write's log position, or fill from the primary for that window (ch. 3, pp. 104–106). |
| c3-05 | Short TTLs buy freshness with load: hit rate collapses on hot keys and every expiry stampedes the origin, as in her Kestrel-7 incident, where a 2 s TTL multiplied origin reads 40x (ch. 3, pp. 110–112). |

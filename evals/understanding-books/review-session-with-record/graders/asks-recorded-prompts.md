---
type: llm
---
The user asked for their day-7 review of chapter 3 of a caching book. Their saved review file holds exactly these five due prompts (paraphrases count):

- c3-01: why a TTL alone cannot bound how stale a cached read can be when the writer's and the cache's clocks disagree, and what bound the author uses instead.
- c3-02 (FAILED last session): how a correct delete-on-write invalidation can still leave a stale value in the cache, and what mechanism stops it.
- c3-03: invalidations broadcast to all 200 cache nodes saturate the message bus during a bulk import; what to change and what it costs.
- c3-04 (PARTIAL last session): a read replica lags 4 seconds behind the primary; why invalidating on every write still lets stale data back in, and what ordering the author recommends.
- c3-05: a colleague says "just use short TTLs and skip invalidation"; the author's strongest reply.

PASS if the reply poses at least one of these recorded prompts (recognizably the same question, paraphrase allowed) for the user to answer now, AND the two earlier misses (c3-02 and c3-04) get priority: at least one of them is the first prompt asked, or the reply explicitly identifies them (by ID or topic) as last session's misses to focus on.

FAIL if the reply asks new or generic chapter-3 questions instead of the recorded prompts (extra questions added after at least one recorded prompt are fine).
FAIL if the reply poses no prompt at all (for example, it only summarizes the record or asks whether to start).
FAIL if the reply asks the recorded prompts but starts with a prompt answered correctly last time and never mentions that c3-02 and c3-04 were missed.

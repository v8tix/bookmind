# The Stale Read: Caches That Tell the Truth

## Intake

Book: The Stale Read: Caches That Tell the Truth
Author: Petra Lindqvist-Arana
Edition/year: 2nd edition, 2025 (Harrowgate Technical Press)
Language (book / notes): English / English
Purpose: application (redesign my team's cache invalidation) and preparation for a design review
Target task format: design-review discussion and applying fixes to a real system
Deadline or keep-until date: long-term
Depth: standard
Time per week: about 3 hours
Prior knowledge: runs Redis in production; knows primary/replica replication basics; no formal distributed-systems course
Source: chapters (short excerpts pasted during sessions; the reader has the full print copy)
Source file: pasted
Reader will read it: reading or read
Mode: guided
PDF page offset: n/a (print edition)
Study folder: books/the-stale-read/

## Book map (provisional)

### Context

- Author and perspective: Petra Lindqvist-Arana, a storage engineer who ran the caching layer of a large payments platform for eight years; she argues from incidents she investigated herself, so most examples come from high-traffic web services.
- Publication date and context: 2nd edition, 2025, revised from the 2019 first edition to add change-data-capture pipelines and managed cache services.
- Intended audience: backend engineers who already operate a cache in production.
- Assumed knowledge: primary/replica replication, basic consistency vocabulary (read-your-writes, eventual consistency), reading a latency percentile.
- Possibly dated or contested areas: latency figures and managed-service limits depend on versions; her claim that most teams underestimate staleness because they watch hit rate instead of freshness rests mainly on her own incident reviews.

### Provisional architecture

- Problem or purpose: application caches serve stale data in ways teams do not notice until an incident, because invalidation is treated as a single fire-and-forget message.
- Provisional thesis: a cache is a replica, so it needs the same versioning, ordering, and failure handling as any other replica; staleness has to be bounded by design, not hoped away with TTLs.
- Major parts and their functions: Part I (ch. 1–2) shows how caches lie; Part II (ch. 3–5) treats invalidation, fill, and eviction as protocols; Part III (ch. 6–8) covers operating caches through failures and migrations.
- Recurring concepts: staleness bound, versioned fill, invalidation ordering, origin load.

## Coverage

- Read: introduction and ch. 3 (pp. 83–114).
- Skimmed: ch. 1–2.
- Not read: ch. 4–8.

## Questions to test

- Does Part II's "caches as protocols" framing carry through to eviction (ch. 5), or does it stop at invalidation? Check against ch. 4–5.
- Does the thesis hold for caches in front of third-party APIs, where the team owns no write path to hook into? Look for this in Part III.

## Sessions

- 2026-09-09: ch. 3 chapter cycle and immediate recall (guided).
- 2026-09-10: first scheduled review of ch. 3; results in review.md.
- Schedule note (2026-09-10): reader away 2026-09-11 to 2026-09-14, so missed items moved to the first free day and the day-7 review set for 2026-09-16.

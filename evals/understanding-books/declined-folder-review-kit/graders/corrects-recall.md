---
type: llm
---
The user recalled a caching chapter from memory. Against the chapter, their recall has these errors: (1) they said to update the cached value on write, but the chapter recommends deleting the key, because racing writers can leave an older value in the cache; (2) they said to set the TTL by how fresh the data needs to be, but the chapter says a backstop TTL on an invalidated entry should be sized by how long you can tolerate an invalidation bug, with freshness handled by a staleness budget; (3) they said to monitor hit ratio, but the chapter says hit ratio shows the cache is busy, not correct, and staleness should be measured directly. They also missed the staleness budget entirely. They were right that invalidation needs an owner and that there are three families (time-based, write-driven, event-driven).

PASS if the reply corrects at least two of the three errors above, stating what the chapter actually says, and acknowledges at least one thing the user got right.
FAIL if the reply corrects fewer than two of the errors, or endorses "update the cached value on write" or "set the TTL by freshness" as correct.

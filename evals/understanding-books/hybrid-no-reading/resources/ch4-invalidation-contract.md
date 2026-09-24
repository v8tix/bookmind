# Chapter 4: Invalidation Is a Contract, Not a Timer

*From* Hard Things in Soft Systems: Notes from Twenty Production Caches, *by Delphine Arkwright (Larkspur Technical Press, 2024)*

[p. 87]

In the spring of 2019 I spent three weeks with the pricing team of a mid-sized online retailer. Their flash sales ended on the hour, and for up to forty minutes afterward customers kept seeing sale prices in their carts, then full prices at checkout. The cause was not mysterious. Prices lived in a cache with a one-hour time-to-live (TTL), and nothing removed an entry when a price changed. The team's first fix was to cut the TTL to five minutes. Database load tripled, and the complaints fell but did not stop.

That story is the whole chapter in miniature. A cache entry is a promise about how far a copy may drift from its source. If you cannot say who breaks that promise, and when, you do not have a caching strategy; you have a hope with an expiry date. My argument in this chapter is that invalidation belongs to whoever owns the write. A TTL is a safety net that limits the damage when invalidation fails. It is not the mechanism that makes a cache correct.

## 4.1 Three families of invalidation

[p. 88]

Almost every invalidation scheme I have seen belongs to one of three families.

**Time-based expiry.** Each entry carries a TTL and disappears when it runs out. It needs no coordination between services, which is why teams reach for it first. Its weakness is that it offers a single dial: a shorter TTL buys freshness with load, and a longer one buys load with staleness. No setting of that dial makes a changed value visible immediately.

**Write-driven invalidation.** The code that writes to the database also touches the cache, in the same request. It can either update the cached value or delete the key. I recommend deleting. When two writers race, they may commit to the database in one order and update the cache in the other, leaving the cache holding the older value indefinitely. A delete has no value to get wrong: the next reader misses and fetches whatever the database holds.

[p. 89]

**Event-driven invalidation.** Instead of every writer remembering to touch the cache, a separate invalidator reads the database's commit log (change data capture) and deletes the affected keys. Because the log is ordered by commit, invalidations arrive in the order the writes happened, and a writer added next year cannot forget to invalidate. The price is lag, since the pipeline takes time to deliver each event, and one more system to operate.

Write-driven invalidation suits data with a single owning service. When many services write the same tables, event-driven invalidation is the only family that scales with the number of writers.

## 4.2 The staleness budget

[p. 90]

The tool I ask every team to adopt is a staleness budget: for each class of cached data, the maximum age a reader may see, and who pays when that age is exceeded. At the retailer, prices had a budget of a few seconds, and customers paid for violations. Product descriptions could be hours old without harm. Profile pictures could lag by a day.

The budget chooses the family. If the budget is loose compared with the TTL you can afford, expiry alone is enough, and you should not build anything more. If the budget is tight, you need write-driven or event-driven invalidation, with a TTL behind it as a backstop.

That changes how you pick the TTL. On an entry that is invalidated correctly, the TTL should be set by how long you can tolerate a bug in your invalidation code, not by how fresh the data needs to be. Teams that size the backstop TTL by freshness end up back where the retailer started: turning one dial and paying for it in load.

## 4.3 Why delete-on-write is enough

[p. 91]

The simplest write-driven scheme, and the one I recommend by default, is to commit the write to the database and then delete the cache key. This closes the staleness window completely: after the delete, the next reader misses, reads the database, and gets the new value. There is nothing to order and nothing to reconcile.

Readers of early drafts asked about races between a slow reader and a writer. In twenty production caches I have not seen one that mattered, and I do not think the extra machinery some designs add to guard against them earns its keep.

## 4.4 Choosing, and knowing whether it works

[p. 92]

Four rules follow from this chapter:

1. Write a staleness budget for each class of cached data before choosing a mechanism.
2. Put invalidation in the write path of the service that owns the data, or derive it from the commit log when many services write.
3. Keep a TTL behind every invalidated entry, sized to how long you can tolerate an invalidation bug.
4. Measure staleness directly. Sample cached values, compare them with the source, and alert on the age of mismatches. Hit ratio tells you the cache is busy; it does not tell you the cache is right.

[p. 93]

The retailer moved prices to delete-on-write with a ten-minute backstop TTL. In the month after the change, stale-price complaints fell to zero, and database load returned to where it had been before the five-minute experiment.

What this chapter has not addressed is what happens when a popular key is deleted and thousands of readers miss at once. Deleting keys correctly can still overload the database behind them. That is the subject of Chapter 5.

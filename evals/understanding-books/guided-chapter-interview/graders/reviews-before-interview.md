---
type: llm
---
The user's interview is on October 23. You are grading whether the reply's review plan respects that deadline. If the reply places the interview in a particular year (for example "2026-10-23"), compare every date against that exact date.

PASS if the reply proposes review sessions, every proposed review falls before October 23, and the reviews are given as calendar dates (for example "Sept 28", "2026-10-05", or "Tuesday, October 20"), not only as relative offsets.
PASS if the reply proposes no dated review schedule yet (for example, it says it will set up reviews after the user has read the chapter), provided it does not suggest any review on or after October 23.
FAIL if any proposed review or study session falls on or after October 23.
FAIL if the reply gives a review schedule only as relative offsets ("day 3", "in a week", "after 21 days") with no calendar dates.

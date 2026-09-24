---
type: llm
---
The user wants to remember a book chapter for months. Judge only how the reply writes the dates of any scheduled future reviews.

PASS if the reply gives no review schedule or review dates yet.
PASS if every scheduled review the reply lists is tied to an absolute calendar date, such as "2026-09-25", "Sept 25", or "October 1". A relative label next to the date, such as "day 7 (2026-10-01)", is fine.
FAIL if the reply lists scheduled reviews only as relative offsets, such as "day 1, day 3, day 7", "in a week", or "after 21 days", with no calendar dates.
FAIL if the reply lists specific review points where some have calendar dates and others have only a relative offset.
A general note about reviews beyond the listed dates (for example "after that, roughly every few months" or "or hand the prompts to Anki") is not a specific review point and does not cause a FAIL.

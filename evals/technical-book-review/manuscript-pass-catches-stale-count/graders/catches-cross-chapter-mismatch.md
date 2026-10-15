---
type: llm
---
Chapter 2 of the manuscript says there are four safety limits. The glossary, a separate file in the same manuscript, says there are three. The companion repo's `writer.go` defines `const SafetyLimitCount = 4`, confirming chapter 2 is right and the glossary is stale.

PASS if the reply reports a finding that the glossary's count disagrees with chapter 2 (three vs. four), and recommends correcting the glossary to four (or otherwise makes clear four is the right number per the code).
FAIL if the reply reviews chapter 2 and the glossary separately but never compares the two counts to each other.
FAIL if the reply says the two agree, or doesn't mention the glossary's count at all.

---
type: llm
---
The user asked a literary question about The Great Gatsby, a novel. Judge whether the reply treats it as literature or wrongly forces a nonfiction study framework onto it.

PASS if the reply reads as a literary discussion of the novel's themes, characters, symbols, or context.
FAIL if the reply frames the novel as a nonfiction argument to be tested, for example "the author's thesis" laid out with evidence, assumptions, and trade-offs, or an argument map with labeled relations such as "--supports-->" or "--contradicts-->".
FAIL if the reply tags claims with provenance labels such as "Author:", "Context:", "Reader:", or "Inference:", or labels its answer "recalled, not verified against the text".
FAIL if the reply proposes turning the novel's ideas into falsifiable experiments or practical applications to test.
FAIL if the reply offers a study plan: prequestions to guess at, retrieval prompts, a spaced-review schedule, or a study folder.

# Book Understanding Templates

## Contents

- Intake
- Book map
- Chapter cycle
- Relationship map
- Concept card
- Retrieval and feedback
- Review file
- Whole-book synthesis

Use only the smallest template needed, and adapt headings to the book and the reader's goal. In the study folder:

- `book.md` holds the Intake, the Book map, concept cards under `## Concepts`, and later the Whole-book synthesis;
- each `chapters/NN-<slug>.md` holds one chapter's Chapter cycle, or one cycle per major section under `## Section` headings for a dense chapter;
- `review.md` holds the Review file.

Retrieval and feedback is the in-session reply format. Record its outcome in the chapter file's Verification section and its new prompts in `review.md`.

## Intake

```markdown
Book:
Author:
Edition/year:
Language (book / notes):
Purpose:
Target task format:
Deadline or keep-until date:
Depth: light | standard | deep
Time per week:
Prior knowledge:
Source: full text | chapters | notes | metadata | recalled (unverified)
Input: <path given by the reader, "pasted", or "none">
Format: <e.g. PDF | EPUB | PDF converted to Markdown with page anchors | notes>
Reader will read it: reading or read | will not read
Mode: guided | hybrid | analyst
Page offset (PDF page or anchor − printed page):
Output: <folder given by the reader, or "no files">
Study folder: <output>/<input-name>/
```

## Book map

```markdown
# Book map: [Title]

## Context
- Author and perspective:
- Publication date and context:
- Intended audience:
- Assumed knowledge:
- Possibly dated or contested areas:

## Provisional architecture
- Problem or purpose:
- Provisional thesis:
- Major parts and their functions:
- Recurring concepts:
- Expected argument flow:

## Coverage
Read: pp. … Skimmed: ch. … Not read: ch. …

## Questions to test
- What evidence would confirm or revise this map?
```

## Chapter cycle

```markdown
# Chapter [number]: [title]

## Before reading
- Function in the book:
- Questions:
  1.
- My guesses:
  1.

## Explain
- [Central idea]:
  - Reader's explanation:
  - Gap and correction:

## After reading, from memory
- Answers to the questions:
- Relationship map: (see Relationship map)
- Evidence/examples:
- Assumptions and trade-offs:
- Depends on / revises / contradicts (earlier chapter):
- Unanswered questions:

## Verification (checked by Claude against the source)
- Correct:
- Incomplete:
- Distorted/unsupported:
- Missing:
- Not attempted:
- Correction:
- Re-asked until correct:

## Compression
- Five ideas:
- Three sentences:
- One sentence:
```

## Relationship map

Plain-text propositions, one per line; every line needs a verb. In a from-memory map the reader writes only the propositions; Claude adds provenance and, when the text was read, the location while checking against the source. Recalled claims use the rule-2 label `Author (recalled, not verified against the text)` and cite a chapter at most.

```text
[Concept A] --enables--> [Concept B]        | Author    | ch. 3, p. 71
[Concept C] --contradicts--> [Concept D]    | Inference | ch. 3–4
[Concept E] --depends on--> [Concept F]     | Author    | ch. 2, p. 40
[Concept G] --superseded by--> [Concept H]  | Context   | [source]
```

## Concept card

For the book's 5–10 core concepts only, at Deep depth.

```markdown
# [Concept]

- Author: What does the book claim? (location)
- In my words:
- Mechanism:
- Problem solved:
- Assumptions:
- Costs/failure modes:
- Alternative:
- Example (ideally not from the book):
- Do not use/believe when:
- Relations: [concept] --verb--> [concept]
- Currency (Context):
```

## Retrieval and feedback

```markdown
# Retrieval: [chapter/concept], [YYYY-MM-DD]

## Recall without source
[Reader response]

## Comparison with source
| Item | Confidence (1–5, Deep only) | Status | Correction or evidence | Re-asked |
|---|---|---|---|---|
| | | correct / incomplete / distorted / unsupported / missing / not attempted | | yes / no |

## New prompts
- [Question]
```

## Review file

`review.md` is the only file the next session needs to run a review. Keep answer keys short and point to locations instead of quoting.

```markdown
# Review: [Title]

Horizon: [deadline YYYY-MM-DD | keep until YYYY-MM-DD | long-term]
Planned reviews (deadline only): [YYYY-MM-DD, …]

Due: prompts whose Status is active or stable and whose Next date is today or earlier. Ask the oldest Next first; within a date, prompts that were failed or partial last time. The Log is history only; never work out due prompts from it.

## Prompts
| ID | Prompt | Type | Status | Streak | Last | Next |
|---|---|---|---|---|---|---|
| c3-01 | | recall / scenario / objection / exercise | active / stable / retired | 0 | YYYY-MM-DD | YYYY-MM-DD |

## Log
| Date | ID | First-attempt result | Main gap |
|---|---|---|---|
| YYYY-MM-DD | c3-01 | correct / partial / failed / not attempted | |

## Answer keys (read only after answering)
| ID | Answer key (short, with location) |
|---|---|
| c3-01 | |
```

Rules for this file:

- When you write a prompt, set Last to today and Next to its first scheduled review.
- Last is the date the prompt was written or last reviewed; the gap is Next − Last.
- Update Streak, Status, Last, and Next after each review, following Phase 5 of protocol.md, and append the results to the Log. Practice on prompts that are not yet due changes nothing here.
- IDs: `c<chapter>-<nn>` for chapter prompts, `bk-<nn>` for whole-book prompts.

For an Anki export, write `review.csv` with one row per prompt that is not retired. Anki imports a plain first row as a card, so start with its header lines:

```text
#separator:Comma
#columns:Question,Answer
"What does leader election assume about the network?","[short answer] (ch. 3, p. 71)"
```

## Whole-book synthesis

```markdown
# [Book]: synthesis

## One-sentence compression

## Executive synthesis (three paragraphs)

## Context and problem

## Central thesis or organizing purpose

## Argument architecture
| Claim | Supported by | Depends on | Challenged by | Label | Source |
|---|---|---|---|---|---|

## Durable ideas
1.

## Evidence, limitations, and currency

## Author / Context / Reader / Inference
- Author:
- Context:
- Reader:
- Inference:

## Applications and their risk

## Disagreements and open questions

## Review prompts (copied into review.md as bk-01, bk-02, …)
1.
```

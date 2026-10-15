# Review patterns

Ten verification patterns, a four-type documentation lens, and three reviewer perspectives. None of this is a universal standard; it's a practical synthesis, usable independently or together. Apply the ones that fit the manuscript's state (see SKILL.md, "The patterns") rather than running every one on every sentence.

## The ten patterns

Each pattern names a goal and the one question it answers.

1. **Claim Verification** — make technical statements trustworthy. Identify a specific claim about an API, a number, a behavior, or a performance characteristic; compare it against the companion repo, primary documentation, or a verifiable experiment; flag unsupported absolutes ("always," "never," "guarantees") and version-dependent statements. *What evidence supports this claim, and under what conditions is it true?*

2. **Executable Example** — make sure a reader can run what the book teaches. Build and run complete examples when practical; check prerequisites, versions, and output. Skip this where the project's own tooling already guarantees an excerpt matches its source — that's stronger than a manual run, and redundant to repeat. *Can the reader reproduce the stated result from the book's instructions?*

3. **Reader Simulation** — review from the stated audience's point of view, using only the knowledge the book says they already have; follow the chapter literally, without filling gaps from outside expertise. *Could a representative reader succeed without consulting the author?*

4. **Progressive Complexity** — check that fundamentals appear before what depends on them, and that complexity increases deliberately rather than jumping from a toy example straight to production architecture. *Does each step build naturally on what came before it?*

5. **Concept–Example Alignment** — match every major explanation to its demonstration; check that an example's output actually supports the surrounding claim, and that prose, code, and diagrams agree. *Does the example demonstrate what the text says it demonstrates?*

6. **Architectural Consistency** — check that diagrams, components, interfaces, and code describe one compatible system; challenge a design choice and make its trade-off explicit rather than letting it pass as obviously correct. *Would the reader build the architecture the diagrams and narrative actually describe?*

7. **Knowledge-Gap Detection** — find the prerequisite, trade-off, limitation, or failure mode the author assumed instead of taught; ask whether a beginner could mistake a simplified example for a production-ready one. *What important information has the author assumed rather than taught?*

8. **Cross-Chapter Consistency** — track a repeated term, API name, configuration value, or count across the whole manuscript, not just within one chapter; check references to earlier chapters, figures, and tables. A contradiction and an unnecessary duplication are both findings. *Do all chapters tell one coherent technical story?*

9. **Adversarial Validation** — try the unhappy path the prose doesn't mention: an invalid input, a dependency that's unavailable, a cancellation, a resource limit. Where full robustness is outside the book's stated scope, the finding is that the limitation isn't disclosed, not that the code lacks it. *Under what realistic conditions could the example fail or mislead?*

10. **Feedback–Correction–Retest** — a finding becomes a fix becomes a re-run, not a note that sits unresolved. Give the author room to pick the correction when more than one is valid; close a finding only after the original problem is gone and nothing new broke. *Has the correction resolved the identified problem without creating another?*

## A documentation-type lens

Borrowed from the Diátaxis framework (diataxis.fr), not a reviewing standard on its own — four kinds of content a technical chapter mixes, each with a different job:

| Type | Reader's question | Reviewer checks |
|---|---|---|
| Tutorial | "Can you teach me?" | Is the sequence approachable and does it actually execute? |
| How-to guide | "How do I do this?" | Can the reader follow the procedure and reach the stated goal? |
| Reference | "What is this?" | Are the facts, options, and constraints precise? |
| Explanation | "Why does this work?" | Are the mechanism, the reasoning, and the trade-offs clear? |

Check whether each part of a chapter serves the type it's actually trying to be — a tutorial step that quietly becomes a reference dump, or an explanation that never says why, is the finding. Don't require every chapter to contain all four; most won't.

## Three reviewer perspectives

Hold these separately rather than blending them into one voice:

- **Technical** — *is it correct, executable, secure, and architecturally defensible?* Claims, code, APIs, failure modes, diagrams.
- **Educational** — *can the intended reader understand, learn, and reproduce this?* The reader's journey, terminology, examples, prerequisites.
- **Developmental** — *does the book have the right structure, progression, and depth for what it promises?* Organization, narrative coherence, repetition, gaps.

Most findings in a finished, previously-reviewed manuscript come from the technical perspective — the other two matter more while a manuscript is still being drafted or restructured. Keep a finding's perspective visible rather than folding all three into one undifferentiated note.

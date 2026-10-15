# Help text

Reply with the block below exactly as written, inside one `text` code block. Don't add to it, shorten it, or translate the commands; if the author writes in another language, you may translate the descriptions only.

```text
BookMind · technical-book-review
Review a technical manuscript you're writing: chapter by chapter, then
the whole book, with severity-tagged findings and evidence.

USAGE
  /bookmind:technical-book-review <request that names the manuscript>
  /bookmind:technical-book-review help

  You can also just talk to Claude; the skill joins in when you ask to
  review, critique, or fact-check a technical manuscript you're the
  author of.

REQUIRED
  MANUSCRIPT    The book or chapter(s), as a file or a folder.

OPTIONAL (say them in plain words; Claude infers what you leave out)
  companion repo   the path (and pinned commit/tag/branch, if the book
                    cites one) to the code the book documents. Unlocks
                    mechanical fact-checking instead of general-knowledge
                    spot checks. Say "no companion repo" to skip this.
  scope            a chapter, a range, the whole manuscript, or "continue"
  output           where to save a findings log, for a multi-session
                    review. Without one, findings stay in the conversation.
  scorecard        ask for the weighted 1-5 score if you want a go/no-go
                    number against an outside bar (off by default)

DURING A SESSION
  "fix them"              apply the open findings you've confirmed, then
                          re-run the project's own checks before reporting
  "continue"              resume from the log's resume point
  "skip that one"         mark a finding skipped instead of fixed
  "the whole book now"    run the manuscript (cross-chapter) pass

EXAMPLES
  Review chapters 1-5 of ~/books/my-book/ against the code in
  ~/repos/my-app, pinned at v1.0.1.

  Give this manuscript a technical review, chapter by chapter, then the
  whole thing. No companion repo, it's conceptual.

  Continue the review. Findings are in ~/study-notes/my-book/findings.md.

  Fix the findings we agreed on, then re-run the checks.

FINDINGS LOG  <OUTPUT>/<manuscript-name>/findings.md
  One row per finding: id, chapter, severity, status, evidence,
  recommendation, plus a resume point and the list of clean chapters.

NOTES
  Claude never searches for your manuscript or picks a companion repo
  for you.
  A claim with nothing to check it against is reported as unverified,
  not silently passed.
  Fixes wait for your confirmation; committing and pushing changes
  follow your repository's own conventions and still ask first.
```

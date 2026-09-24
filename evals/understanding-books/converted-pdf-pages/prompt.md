---
description: "Input format and page citations. The book (fixture quiet-queues/quiet-queues.md, a fictional short book) is a PDF converted to Markdown: page anchors like page-17-0 count PDF pages from 0, while the printed pages in its table of contents start at 1 on anchor page-12, so printed page = anchor - 11. Chapter 2's central claim is on printed p. 6 (anchor page-17). Checks that Claude identifies the converted format and cites printed pages, not anchor numbers."
tags: [understanding-books, sources, page-citations]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
expected_outcome: "The skill fires; the reply states chapter 2's central claim (a bounded queue that rejects work early beats an unbounded one that fails late) and cites printed page 6, not 17, possibly noting that the file is a converted PDF with an offset."
---
I'm studying chapter 2 of Quiet Queues and I want to mark my paper copy. What is the chapter's central claim, and on which page of the printed book does the author state it? The book is in the resources/quiet-queues folder I added to this session. Save anything you write in the study-notes folder.

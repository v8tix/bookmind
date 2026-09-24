# Working with Book Sources

## Contents

- Find the text
- PDF
- EPUB
- Other formats
- Large books and coverage
- Page citations

## Find the text

If `book.md` records a Source file path, use it first. Otherwise look for the file in the working directory and in each additional working directory, with Glob `**/*.{pdf,epub,mobi,azw,azw3}`, ignoring the `books/` study folder. Search `.md` or `.txt` files only when the reader says the text or notes are in that form. If there is nothing, ask for a path or for pasted excerpts of the chapters that matter. Without any text, follow operating rule 2 in SKILL.md.

## PDF

1. Read the table-of-contents pages first.
2. Work out the page offset: find a page with a visible printed page number and record `PDF page = printed page + offset` in `book.md`. Recheck it at each chapter start, because plates, blank pages, and part dividers change it, and record any change.
3. Read chapter by chapter in ranges of 20 pages or fewer, writing notes as you go (see "Large books and coverage") so that context compaction does not lose them.
4. If the text layer is missing or garbled (a scanned book), say so and note the OCR limits. When it is installed, `pdftotext -layout -f <first> -l <last> book.pdf -` through Bash can help, one chapter range at a time.

## EPUB

Reading an EPUB directly returns compressed bytes; extract it instead:

1. List the contents with `unzip -l book.epub`.
2. Read `META-INF/container.xml` to find the `.opf` file. Take the chapter order from its `<spine>`, map each `idref` to its `href` in the `<manifest>`, and resolve hrefs relative to the `.opf` file's folder.
3. Extract a chapter as text with `unzip -p book.epub <path/to/chapter.xhtml> | sed -e 's/<[^>]*>//g'`, or convert the book with `pandoc` if it is installed.
4. EPUBs have no fixed pages: cite chapter and section instead.

## Other formats

MOBI, AZW, and AZW3 need conversion first (for example, Calibre's `ebook-convert`). DRM-protected files cannot be read; ask the reader for exported notes and highlights or pasted excerpts. Do not help remove DRM.

## Large books and coverage

Map first from the front matter, table of contents, introduction, and conclusion; then read only what the current purpose needs. For a book longer than about 50,000 words, write a short note of each chapter's claims with locations before reading the next: in the study folder when there is one, otherwise in a temporary directory, never in the reader's project. Keep a coverage line in `book.md` (or in those notes) and state it in every analysis:

```text
Coverage. Read: pp. 1–48, 102–130. Skimmed: ch. 5–6. Not read: ch. 7–12.
```

Make no chapter-level claims about unread pages, except recalled claims labeled under operating rule 2. Offer to read further when an answer depends on them.

## Page citations

Cite printed page numbers along with the edition. If only the PDF page is known, write "PDF p. 152". When the reader asks about specific pages and the offset is large, confirm whether they mean printed or PDF pages.

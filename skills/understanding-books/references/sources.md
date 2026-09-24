# Working with Book Sources

## Contents

- Identify the format
- PDF
- EPUB
- Converted text (Markdown or plain text from a PDF or EPUB)
- Other formats
- Large books and coverage
- Page citations

## Identify the format

Use only the input path the reader gave; never search other folders for a book. Before reading any of the text, work out what the input is:

1. **File or folder.** For a folder, list its contents. Find the book file itself (the largest text, PDF, or EPUB file) and note what sits beside it: page images, a `*_meta.json` or similar conversion metadata, or several chapter files.
2. **Extension.** `.pdf`, `.epub`, `.mobi`/`.azw`/`.azw3`, or a text format (`.md`, `.txt`, `.html`).
3. **Content, for text formats.** Read the first 100 or so lines and search the file for markers. Page anchors (`<span id="page-12-0">`, `[page 12]`, form-feed characters), image links, or a table of contents with page numbers mean the text was converted from a PDF: follow "Converted text". Plain prose with no markers is notes or an excerpt.
4. **Record it** in `book.md`: the input path, the format (for example "PDF converted to Markdown, with page anchors"), how to read it, and how to cite locations (the page offset, or chapter and section).

If the reader said there is no file, record that and follow operating rule 2 in SKILL.md.

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

## Converted text (Markdown or plain text from a PDF or EPUB)

Tools such as marker or pandoc turn a book into one large text file, often with page images and a metadata file beside it.

1. Map the chapters first: list the headings (`grep -n '^#'`) and match them to the table of contents. Record each chapter's line range in `book.md`, then read one chapter's range at a time.
2. Work out the page offset from the anchors. Find the anchor at a chapter's first line, compare it with that chapter's printed page in the table of contents, and record `printed page = anchor − offset` (anchors often count from 0 and include front matter). Check it at two or three more chapter starts. If it changes, record each range.
3. Cite printed pages worked out this way. With no page anchors, cite chapter and section, as for an EPUB.
4. Expect conversion damage: broken symbols, merged words, split tables, repeated or cut code blocks. Don't treat these as the author's errors, and say so if a passage you rely on looks damaged.

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

# Help text

Reply with the block below exactly as written, inside one `text` code block. Don't add to it, shorten it, or translate the commands; if the reader writes in another language, you may translate the descriptions only.

```text
BookMind · understanding-books
Study nonfiction and technical books: map, quiz, explain, recall, and
spaced review, with notes saved to a study folder.

USAGE
  /bookmind:understanding-books <request that names INPUT and OUTPUT>
  /bookmind:understanding-books help

  You can also just talk to Claude; the skill joins in when you ask to
  study, analyze, summarize, or review a book.

REQUIRED
  INPUT         The book as a PDF or Markdown file, or the folder that holds
                it. Or say "no file" to work from pasted excerpts or from
                what Claude knows (labeled as unverified).
  OUTPUT        Notes folder. Claude creates <OUTPUT>/<book-name>/ in it.
                Or say "no files" to get a paste-back review kit instead.

OPTIONAL (say them in plain words; Claude infers what you leave out)
  scope         a chapter, a range of chapters, or the whole book
  mode          guided   you read; you guess, explain, and recall first
                hybrid   you won't read; Claude's chapter briefs stand in
                analyst  Claude writes the analysis; no quizzing
  depth         light | standard | deep       (default: light or standard)
  goal          exam, interview, building something, critique, curiosity
  deadline      an exam or interview date, or how long to remember it
                (default: three months)
  language      the language for your notes (default: the one you write in)

DURING A SESSION
  "just give me the answer"      full answer now, no hints
  "stop quizzing me"             Claude answers this step's questions
  "next"                         move on to the next chapter
  "time for my review"           ask the questions that are due
  "export to Anki"               write review.csv in the study folder
  "5-minute overview"            thesis, key ideas, one caveat

EXAMPLES
  Help me understand chapter 3 of ~/books/ddia.pdf. Interview on
  October 23. Save my notes in ~/study-notes.

  Help me study ~/books/team-topologies.md and go deep. I won't read
  it. Save my notes in ~/study-notes.

  Analyze ~/books/deep-work.pdf: thesis, arguments, evidence, weak
  spots. Save it in ~/study-notes.

  Give me a 5-minute overview of ~/books/atomic-habits.md. No files.

  Time for my review. My notes are in ~/study-notes.

  I'm stuck on exercise 2.14 in ~/books/linear-algebra.pdf. Notes in
  ~/study-notes.

STUDY FOLDER  <OUTPUT>/<book-name>/
  book.md       book map, coverage, concepts, final synthesis
  chapters/     one file per chapter
  review.md     review questions, due dates, results, answer keys
  review.csv    Anki export, when you ask for it

NOTES
  Claude never searches for your book or picks a folder for you.
  PDF and Markdown books work; convert other formats to one of them first.
  Claude doesn't send reminders: copy review dates into your calendar.
```

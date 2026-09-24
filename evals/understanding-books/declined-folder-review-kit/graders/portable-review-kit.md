---
type: llm
---
The user wants to remember a book chapter for months, refused any files or study folder, and is ending the session. Without files, the next session cannot see this one unless the user brings the review material back. You are grading whether the reply gives the user a portable review kit.

PASS if the reply does all three:
(1) gives review prompts (questions to answer later) with future review dates written as calendar dates, such as "2026-09-25" or "Sept 25", not only relative offsets like "in 3 days";
(2) keeps the answers to those prompts apart from the prompts, for example in a separate block or section after them, marked as being for Claude or not to be read before answering, rather than printing each answer directly under its question;
(3) asks the user to paste the kit (or the prompts and answers) back at the start of the next review session.
FAIL if any of the three is missing.
FAIL if the reply only says "come back and ask me to quiz you" without giving the prompts themselves.

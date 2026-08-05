# Rubric: Notepad System (Authentication, Authorization, and CRUD)

**Python Fundamentals — Object-Oriented Programming (Minor Exam A)**

**Total: 100 points**, computed as Points Earned (Section A) minus Deductions (Section B), floored at 0.

## Section A — Points Earned (sums to 100)

| Criterion | Points |
|---|---|
| Authentication (Login / Register work correctly, blank fields and mismatched passwords handled without crashing) | 15 |
| Authorization (a logged-in user can only view, update, or delete their own notes; another user's notes are never reachable, even by guessing a note number) | 15 |
| CRUD — Create Note (Title/Description captured and correctly attached to the logged-in user) | 10 |
| CRUD — Retrieve/List Note (only the current user's notes shown, correctly formatted in PrettyTable, with Title, Description, Created At, Updated At all visible) | 10 |
| CRUD — Update Note (correct note is targeted by number, blank input keeps the old value, Updated At timestamp refreshes on change) | 10 |
| CRUD — Delete Note (correct note is targeted by number, confirmation step before deleting, note is actually removed) | 10 |
| Input validation & exception handling (invalid menu choices and non-numeric input handled gracefully anywhere in the program, not just in one function) | 10 |
| Code readability (separate function per menu option, sensible structure, comments where helpful, consistent style) | 5 |
| Naming conventions (variables, functions, and classes follow Python naming standards — e.g. snake_case for functions/variables, PascalCase for classes — and names are relevant to their purpose) | 10 |
| File format and name (submitted as a `.py` file, named `Surname_FirstName_minor_a.py`) | 5 |
| **Section A Total** | **100** |

## Section B — Deductions (subtracted from Section A total)

| Violation | Deduction |
|---|---|
| Program breaks — the main loop ends/crashes without the user having selected Exit (`[0]`) from the Main Menu | -15 |
| List Notes not implemented using PrettyTable | -10 |
| Authorization bypass — a user is able to view, update, or delete another user's note | -15 |
| A specific menu option crashes on invalid input instead of handling it gracefully (per distinct option affected, capped at -10 total) | -5 each (max -10) |
| Late submission (per day late) | -5 per day |

## Notes for Grading

- Section A and Section B are computed independently — do not skip an addition item just because a deduction overlaps with it; both apply.
- If Section A minus Section B is negative, record the final score as 0.
- "Breaks" in the first deduction means any uncaught exception or unexpected exit — not the same as pressing `[0]` Exit, which is the only valid way to end the program.

# Activity: Notepad System (Authentication, Authorization, and CRUD)

**Python Fundamentals — Object-Oriented Programming (Minor Exam A)**

Build a console-based Notepad application where users must register and log in before they can manage their own personal notes. The system must support full CRUD (Create, Retrieve, Update, Delete) on notes, and must ensure users can only see and modify their own notes, never anyone else's.

## What the System Is About

This is not a plain CRUD list — it has two layers:

- **Authentication**: verifying who the user is (Login / Register with username and password).
- **Authorization**: once logged in, a user may only List, Update, or Delete notes that belong to them. Another user's notes must never appear or be editable.
- **CRUD on Notes**: each logged-in user can Create, List (Retrieve), Update, and Delete their own notes.

## Setting Up Your Environment (venv)

Before writing any code, create and activate a virtual environment so your installed packages don't affect your system Python.

**Windows (Command Prompt / PowerShell):**

```
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux (Terminal):**

```
python3 -m venv venv
source venv/bin/activate
```

You'll know it worked if you see `(venv)` at the start of your terminal prompt. Always activate your venv before installing packages or running your script.

## Installing PrettyTable

With your venv activated, install PrettyTable:

```
pip install prettytable
```

Then import it in your script:

```python
from prettytable import PrettyTable
```

## Rules

- The program must run in a continuous loop. The loop only ends when the user explicitly selects Exit (`[0]`) from the Main Menu — the program must never crash or terminate on its own.
- There are two menu states:
  - **Main Menu** (no user logged in): `[0]` Exit, `[1]` Login, `[2]` Register
  - **User Menu** (logged in): `[0]` Logout, `[1]` List Notes, `[2]` Create Note, `[3]` Update Note, `[4]` Delete Note
- Each User has a Full Name, Username, and Password. Usernames should be treated as unique identifiers for login.
- Registration must ask for Full Name, Username, Password, and Confirm Password. If Password and Confirm Password don't match, the registration must fail gracefully (no crash) and let the user try again.
- Username and Password cannot be blank on login or registration.
- Each Note has a Title, Description, an owner (the User who created it), a Created At timestamp, and an Updated At timestamp, both set automatically — the user never types a date.
- **Option 1 — List Notes (Retrieve)**: display only the current user's notes using PrettyTable, clearly showing an index/number, Title, Description, Created At, and Updated At.
- **Option 2 — Create Note**: ask for a Title and Description, then attach the note to the currently logged-in user.
- **Option 3 — Update Note**: show the current user's notes, ask which note to update by its number, then allow changing the Title and/or Description. Leaving an input blank should keep the existing value. Updating a note must refresh its Updated At timestamp.
- **Option 4 — Delete Note**: show the current user's notes, ask which note to delete by its number, confirm with the user before deleting, then remove it.
- A user must never be able to update or delete a note that belongs to another user, even by guessing a valid note number.
- Handle invalid input gracefully using exceptions — an invalid menu choice or a non-numeric entry where a number is expected should never crash the program.

## How to Test It

| Action | Steps | Expected Result |
|---|---|---|
| Register | Choose `[2]` → fill in Full Name, Username, Password, Confirm | New account is created and you are logged in |
| Register (mismatch) | Choose `[2]` → Password and Confirm Password differ | Error message shown, no crash, returns to Main Menu |
| Login (valid) | Choose `[1]` → correct Username/Password | Logged in, User Menu appears |
| Login (invalid) | Choose `[1]` → wrong Username/Password | "Invalid Credentials" message, no crash |
| Create Note | Choose `[2]` → Title: "Groceries", Description: "Milk, eggs" | Note is added under your account |
| List Notes | Choose `[1]` | PrettyTable shows only your notes |
| Update Note | Choose `[3]` → select note → change Title | Title changes, Updated At refreshes |
| Update Note (blank input) | Choose `[3]` → select note → leave fields blank | Original Title/Description stay unchanged |
| Delete Note | Choose `[4]` → select note → confirm | Note no longer appears in the list |
| Authorization check | Log in as a second user, try to update/delete the first user's note by guessing its number | Rejected — "Invalid note number" or similar, no crash |
| Invalid menu choice | Enter an out-of-range number at any menu | Error message shown, menu asks again, no crash |
| Invalid numeric input | Enter letters when a number is expected (e.g. note number) | Error message shown, no crash |
| Logout | Choose `[0]` from the User Menu | Returns to Main Menu |
| Exit | Choose `[0]` from the Main Menu | Program ends cleanly |

Be sure to test every menu option, with more than one registered user, and confirm invalid input never crashes the program at any point.

## File Naming

Save/submit the file as:

```
Surname_FirstName_minor_a.py
```

(Replace with the student's actual surname and first name.)
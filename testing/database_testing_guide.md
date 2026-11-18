# Database Testing Guide

Database testing means checking that what the application shows on screen matches what is actually stored in the database.

## 1. Tools (pick one)
- **DB Browser for SQLite** (easiest, free GUI): https://sqlitebrowser.org. Open `application/student_management.db`, go to the **Execute SQL** tab, paste a query and press the Play button.
- **Python's built-in SQLite shell** (Python 3.12+): from the `application` folder run `python -m sqlite3 student_management.db`, then type queries ending with `;`. Type `.quit` to exit.
- **VS Code extension** "SQLite Viewer" to browse the table.

The database file is created the first time you run `python app.py`.

## 2. Workflow: UI action, then DB check, then compare
| Action in the app | Query to run (from `database_test_cases.sql`) | What to compare |
|---|---|---|
| Add a student | DB-03 and DB-01 | New row exists; every value equals what you typed |
| Update a student | DB-04 | Changed field has new value; other fields unchanged |
| Delete a student | DB-05 | Zero rows returned |
| Add duplicate roll/email (rejected) | DB-06, DB-07, DB-09 | Zero duplicates; total count unchanged |
| Add invalid data (rejected) | DB-08, DB-10 | Zero rows; no bad record saved |
| View students page | DB-01, DB-09 | Row count and values match the table on screen |
| Search | DB-11 | Same rows as the search results |

## 3. Example
1. Add student: Roll `101`, Name `Rahul Sharma`.
2. Run `SELECT * FROM students WHERE roll_number = '101';`
3. Expected: exactly 1 row with the same name, email, department and age.
4. Record the result in `manual_test_cases.csv` (Actual Result / Status columns).

## 4. Tips
- Close or refresh DB Browser after each app action (click "Refresh"/re-run the query) and click **Write Changes** if you edit data manually.
- Do not modify rows manually while the app is testing the same data unless the test says so.
- Test DB-12 once to see that SQLite itself rejects duplicates.
- Deleting `student_management.db` resets everything; the app recreates it empty on the next start.

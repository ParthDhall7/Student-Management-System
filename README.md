# Student Management System - Manual & Database Testing

## Project Overview
A simple Flask web application for managing student records, built as a **software testing portfolio project**. The focus is on test design, manual testing, and database verification with SQL.

## Objectives
- Build a small, working CRUD application.
- Design and document manual test cases, including negative and boundary tests.
- Verify database operations independently using SQL.
- Practice bug reporting and regression testing.

## Features
Add, View, Update, Delete (with confirmation) and Search (by name or roll number) students, with input validation and success/error messages.

## Technologies Used
Python, Flask, SQLite, HTML, CSS, SQL, CSV (test documentation).

## Folder Structure
```
Student-Management-System-Testing/
├── application/
│   ├── app.py                 # Flask routes + validation
│   ├── database.py            # SQLite connection + table creation
│   ├── templates/             # base, index, add_student, edit_student
│   └── static/style.css
├── testing/
│   ├── test_plan.md
│   ├── manual_test_cases.csv  # 30 test cases (all "Not Executed")
│   ├── bug_report.csv         # template + hypothetical examples
│   ├── database_test_cases.sql
│   └── database_testing_guide.md
├── screenshots/               # add your test evidence here
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation (Windows, VS Code)
Open the project folder in VS Code, then open a terminal (Ctrl + `):
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
(If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass` first.)

## How to Run
```
cd application
python app.py
```
Open **http://127.0.0.1:5000** in your browser. The database `student_management.db` is created automatically. Stop the server with Ctrl+C.

## Database Design
Database: `student_management.db`, table `students`

| Column | Type | Constraints |
|---|---|---|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| name | TEXT | NOT NULL |
| roll_number | TEXT | NOT NULL UNIQUE |
| email | TEXT | NOT NULL UNIQUE |
| department | TEXT | NOT NULL |
| age | INTEGER | NOT NULL |

All queries are parameterized. Uniqueness is enforced by the database itself, not only by the app.

## Testing Approach
Manual test cases are executed in the browser and recorded in `testing/manual_test_cases.csv`. Each UI action is then verified with SQL (see `testing/database_testing_guide.md`). See `testing/test_plan.md` for scope and criteria.

## Types of Testing
Functional, negative, boundary value, database, and regression testing.

## How to Execute SQL Queries
- DB Browser for SQLite: open `application/student_management.db` -> Execute SQL -> paste queries from `testing/database_test_cases.sql`.
- Or from the `application` folder (Python 3.12+): `python -m sqlite3 student_management.db`

## Test Status
Test cases are provided as a **template** and are marked *Not Executed*. Execute them yourself and record actual results; no results are claimed here.

## Future Improvements
Admin login, pagination, automated tests (pytest / Selenium), CSV export, API testing with Postman.

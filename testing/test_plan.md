# Test Plan - Student Management System

## 1. Project Overview
A Flask + SQLite web application where an administrator can add, view, update, delete and search student records. This plan describes how the application is tested manually and through SQL.

## 2. Testing Objectives
- Verify that all five features work as described.
- Verify that invalid input is rejected with clear messages.
- Verify that database constraints (unique roll number and email, NOT NULL) are enforced.
- Verify that the data shown in the application matches the database.
- Practice writing test cases, bug reports and SQL checks.

## 3. Testing Scope
Add, View, Update, Delete and Search student functions; form validation; data persistence; database integrity.

## 4. Features to be Tested
| Feature | Summary |
|---|---|
| Add Student | Mandatory fields, unique roll/email, email format, age rules |
| View Students | Table display, empty-database message |
| Update Student | Pre-filled form, duplicate prevention, success/error messages |
| Delete Student | Confirmation, success message, nonexistent ID handling |
| Search Student | By name or roll number, partial match, "No student found." |
| Persistence | Data remains after restarting the application |

## 5. Features Excluded
Login/authentication, performance and load testing, automated testing, security testing beyond a basic SQL-injection check, cross-browser and mobile device testing, accessibility testing.

## 6. Testing Approach
- **Functional testing:** each feature is checked against expected behaviour.
- **Negative testing:** empty, invalid, duplicate and nonexistent data (e.g. invalid email, age = "abc").
- **Boundary value testing:** age 0, 1 and 120/121 limits; name length 100 and 101 characters.
- **Database testing:** SQL queries in `database_test_cases.sql` compare database results with application results.
- **Regression testing:** after any bug fix or code change, re-run all test cases (at least the affected module plus Add and Search) to confirm nothing else broke.
- Execution is manual. Results are written into `manual_test_cases.csv`; defects into `bug_report.csv`.

## 7. Test Environment
- Windows 10/11, VS Code, Python 3.10+, Flask, SQLite
- Browser: Google Chrome (latest)
- URL: http://127.0.0.1:5000

## 8. Entry Criteria
- Application runs without errors and database file is created.
- Test cases and SQL queries are reviewed and ready.
- Database is in a known state (empty or deleted before the run).

## 9. Exit Criteria
- All test cases executed and results recorded.
- All defects logged in the bug report.
- No open High-severity bugs (or they are documented).
- Regression run completed after fixes.

## 10. Expected Deliverables
Test plan, manual test cases (CSV), bug report (CSV), database test cases (SQL), database testing guide, screenshots of test execution, README.

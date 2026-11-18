-- database_test_cases.sql
-- Database tests for the Student Management System (SQLite, table: students)
-- Schema: id (PK, autoincrement), name, roll_number (UNIQUE), email (UNIQUE), department, age (all NOT NULL)
-- Run these AFTER performing an action in the application, then compare with what the app shows.
-- Sample roll number used below is '101'; change it to the one you are testing.

-- DB-01: View all student records (compare with the table on the home page)
SELECT * FROM students;

-- DB-02: Find one student by roll number (use after search/add/update/delete)
SELECT * FROM students WHERE roll_number = '101';

-- DB-03: Verify record insertion (after Add Student): newest record appears last, values match the form
SELECT * FROM students ORDER BY id DESC LIMIT 1;

-- DB-04: Verify record update (after Edit): the changed field shows the new value
SELECT id, name, email, department, age FROM students WHERE roll_number = '101';

-- DB-05: Verify record deletion (after Delete): expected result is ZERO rows
SELECT * FROM students WHERE roll_number = '101';

-- DB-06: Duplicate roll numbers: expected result is ZERO rows
SELECT roll_number, COUNT(*) AS total
FROM students
GROUP BY roll_number
HAVING COUNT(*) > 1;

-- DB-07: Duplicate emails: expected result is ZERO rows
SELECT email, COUNT(*) AS total
FROM students
GROUP BY email
HAVING COUNT(*) > 1;

-- DB-08: NULL or empty values in required columns: expected result is ZERO rows
SELECT * FROM students
WHERE name IS NULL OR roll_number IS NULL OR email IS NULL OR department IS NULL OR age IS NULL
   OR TRIM(name) = '' OR TRIM(roll_number) = '' OR TRIM(email) = '' OR TRIM(department) = '';

-- DB-09: Total number of student records (compare with number of rows in the app table)
SELECT COUNT(*) AS total_students FROM students;

-- DB-10: Age validation: expected result is ZERO rows (age must be between 1 and 120)
SELECT * FROM students WHERE age < 1 OR age > 120;

-- DB-11: Search check (matches the app's search for "rah"): compare with app search results
SELECT * FROM students WHERE name LIKE '%rah%' OR roll_number LIKE '%rah%';

-- DB-12: Constraint check (run manually): this should FAIL with "UNIQUE constraint failed"
-- if roll number 101 already exists. This proves the DATABASE enforces uniqueness, not just the app.
-- INSERT INTO students (name, roll_number, email, department, age)
-- VALUES ('Test User', '101', 'unique_test@example.com', 'CS', 20);

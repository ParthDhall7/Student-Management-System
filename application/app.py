import os 
import re
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for

import database

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-key")  

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")  # basic email format check
MAX_NAME_LENGTH = 100
MAX_AGE = 120


def validate_student(form):
    """Check the submitted form. Returns (student_data, list_of_errors)."""
    student = {
        "name": form.get("name", "").strip(),
        "roll_number": form.get("roll_number", "").strip(),
        "email": form.get("email", "").strip().lower(),
        "department": form.get("department", "").strip(),
        "age": form.get("age", "").strip(),
    }
    errors = []

    if not student["name"]:
        errors.append("Student name is required.")
    elif len(student["name"]) > MAX_NAME_LENGTH:
        errors.append(f"Student name must be at most {MAX_NAME_LENGTH} characters.")

    if not student["roll_number"]:
        errors.append("Roll number is required.")

    if not student["email"]:
        errors.append("Email is required.")
    elif not EMAIL_PATTERN.match(student["email"]):
        errors.append("Email format is invalid (example: name@example.com).")

    if not student["department"]:
        errors.append("Department is required.")

    age_text = student["age"]
    if not age_text:
        errors.append("Age is required.")
    elif not (age_text.isascii() and age_text.isdigit()):
        errors.append("Age must be a positive whole number.")
    elif int(age_text) < 1:
        errors.append("Age must be greater than 0.")
    elif int(age_text) > MAX_AGE:
        errors.append(f"Age must not be more than {MAX_AGE}.")

    return student, errors


def duplicate_message(error):
    """Turn a database UNIQUE error into a friendly message."""
    text = str(error)
    if "roll_number" in text:
        return "Roll number already exists."
    if "email" in text:
        return "Email already exists."
    return "Could not save the student."


@app.route("/")
def index():
    """View all students, or search by name / roll number using ?q=..."""
    search_text = request.args.get("q", "").strip()
    connection = database.get_connection()
    if search_text:
        pattern = "%" + search_text + "%"
        students = connection.execute(
            "SELECT * FROM students WHERE name LIKE ? OR roll_number LIKE ? ORDER BY id",
            (pattern, pattern),
        ).fetchall()
    else:
        students = connection.execute("SELECT * FROM students ORDER BY id").fetchall()
    connection.close()
    return render_template("index.html", students=students, search_text=search_text)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "GET":
        return render_template("add_student.html", student={})

    student, errors = validate_student(request.form)
    if errors:
        for message in errors:
            flash(message, "error")
        return render_template("add_student.html", student=student)

    connection = database.get_connection()
    try:
        connection.execute(
            "INSERT INTO students (name, roll_number, email, department, age) VALUES (?, ?, ?, ?, ?)",
            (student["name"], student["roll_number"], student["email"],
             student["department"], int(student["age"])),
        )
        connection.commit()
    except sqlite3.IntegrityError as error:  # the database rejected a duplicate
        flash(duplicate_message(error), "error")
        return render_template("add_student.html", student=student)
    finally:
        connection.close()

    flash("Student added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    connection = database.get_connection()
    existing = connection.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    if existing is None:
        connection.close()
        flash("Student not found.", "error")
        return redirect(url_for("index"))

    if request.method == "GET":
        connection.close()
        return render_template("edit_student.html", student=dict(existing))

    student, errors = validate_student(request.form)
    student["id"] = student_id
    if errors:
        connection.close()
        for message in errors:
            flash(message, "error")
        return render_template("edit_student.html", student=student)

    try:
        connection.execute(
            "UPDATE students SET name = ?, roll_number = ?, email = ?, department = ?, age = ? WHERE id = ?",
            (student["name"], student["roll_number"], student["email"],
             student["department"], int(student["age"]), student_id),
        )
        connection.commit()
    except sqlite3.IntegrityError as error:
        flash(duplicate_message(error), "error")
        return render_template("edit_student.html", student=student)
    finally:
        connection.close()

    flash("Student updated successfully.", "success")
    return redirect(url_for("index"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    connection = database.get_connection()
    cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    connection.close()

    if cursor.rowcount == 0:  # nothing was deleted -> the ID did not exist
        flash("Student not found.", "error")
    else:
        flash("Student deleted successfully.", "success")
    return redirect(url_for("index"))

database.init_db()  # create the database and table automatically

if __name__ == "__main__":
    app.run(debug=True)

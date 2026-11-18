# database.py - all SQLite database code lives here.
import os
import sqlite3

# The database file is stored next to this script, whatever folder you run from.
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student_management.db")


def get_connection():
    """Open a connection to the database. Rows can be read like dictionaries."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Create the students table if it does not exist yet (runs on app start)."""
    connection = get_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            roll_number TEXT NOT NULL UNIQUE,
            email       TEXT NOT NULL UNIQUE,
            department  TEXT NOT NULL,
            age         INTEGER NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()

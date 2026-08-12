"""
SQLite Database Design and Advanced Queries
Assignment Starter Code

This starter template demonstrates basic database operations.
Your task is to expand this with a complete schema and advanced queries.
"""

import sqlite3
from pathlib import Path

# Database file location
DB_PATH = "school.db"

def create_connection(db_path):
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Access columns by name
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_tables(conn):
    """Create the database schema with related tables."""
    cursor = conn.cursor()
    
    # Example: Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        enrollment_date DATE
    )
    """)
    
    # Example: Courses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        instructor TEXT,
        credits INTEGER
    )
    """)
    
    # Example: Enrollments table (junction table for many-to-many relationship)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
    """)
    
    conn.commit()
    print("Database schema created successfully!")

def insert_sample_data(conn):
    """Insert sample data into the tables."""
    cursor = conn.cursor()
    
    # Insert students
    students = [
        ("Alice Johnson", "alice@school.com", "2024-01-15"),
        ("Bob Smith", "bob@school.com", "2024-01-15"),
        ("Carol White", "carol@school.com", "2024-02-01"),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO students (name, email, enrollment_date) VALUES (?, ?, ?)",
        students
    )
    
    # Insert courses
    courses = [
        ("Introduction to Python", "Dr. Smith", 3),
        ("Data Structures", "Dr. Johnson", 4),
        ("Database Design", "Dr. White", 3),
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO courses (title, instructor, credits) VALUES (?, ?, ?)",
        courses
    )
    
    # Insert enrollments
    enrollments = [
        (1, 1, "A"),
        (1, 2, "B"),
        (2, 1, "A"),
        (3, 3, "A"),
    ]
    cursor.executemany(
        "INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
        enrollments
    )
    
    conn.commit()
    print("Sample data inserted!")

def query_example(conn):
    """Example query: Get all enrollments with student and course details."""
    cursor = conn.cursor()
    
    query = """
    SELECT 
        s.name as student_name,
        c.title as course_title,
        e.grade,
        c.credits
    FROM enrollments e
    JOIN students s ON e.student_id = s.id
    JOIN courses c ON e.course_id = c.id
    ORDER BY s.name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    print("\nStudent Enrollments:")
    print("-" * 60)
    for row in results:
        print(f"{row['student_name']:20} | {row['course_title']:25} | Grade: {row['grade']} | Credits: {row['credits']}")

def main():
    """Initialize database and run queries."""
    # Remove existing database for fresh start (optional during development)
    # if Path(DB_PATH).exists():
    #     Path(DB_PATH).unlink()
    
    # Create connection and set up database
    conn = create_connection(DB_PATH)
    if conn:
        create_tables(conn)
        insert_sample_data(conn)
        query_example(conn)
        conn.close()
        print(f"\nDatabase initialized at: {DB_PATH}")
    else:
        print("Failed to create database connection")

if __name__ == "__main__":
    main()

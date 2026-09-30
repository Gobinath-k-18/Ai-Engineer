import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

students = [
    (1, "Arun", 21, 85),
    (2, "Bala", 22, 72),
    (3, "Kumar", 20, 91),
    (4, "Divya", 21, 88),
    (5, "Ravi", 23, 67)
]

cursor.executemany(
    "INSERT OR REPLACE INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    students
)

connection.commit()

print("Student data inserted successfully!")

cursor.execute("""
SELECT * FROM students
WHERE marks >= 80
ORDER BY marks DESC
""")
rows = cursor.fetchall()

for row in rows:
    print(row)
connection.close()
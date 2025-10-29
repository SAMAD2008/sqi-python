import sqlite3
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')


cursor.execute('''
INSERT INTO students (name, age)
VALUES 
    ('Alice Smith', 22),
    ('Bob Johnson', 19),
    ('Charlie Brown', 21),
    ('Diana Evans', 23),
    ('Ethan Davis', 20)
''')
conn.commit()

# Fetch the students table
cursor.execute('SELECT * FROM students')

rows = cursor.fetchall()
for row in rows:
    print(row)








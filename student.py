import sqlite3
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cmd="""
CREATE TABLE IF NOT EXISTS feedback (
    fullname text not null,
    usn varchar(10)  primary key not null,
    contact varchar(10) not null,
    email text not null,
    cgpa float
)
"""

cursor.execute(cmd)
connection.commit()

cmd="INSERT INTO feedback (fullname, usn, contact, email, cgpa) values (?, ?, ?, ?, ?)"
cursor.execute(cmd, ("Amrutha", "4MW233AD002", "8073972157", "amrutha.23ad002@sode-edu.in", 9.2))
connection.commit()

f = cursor.execute("SELECT * FROM feedback").fetchall()
print(f)
connection.close()

import sqlite3
connection = sqlite3.connect("feedback.db")
cursor = connection.cursor()

cmd="""
CREATE TABLE IF NOT EXISTS feedback (
    id integer primary key AUTOINCREMENT,
    fullname text not null,
    usn varchar(10)  not null,
    contact varchar(10) not null,
    email text not null,
    message text not null
)
"""

cursor.execute(cmd)
connection.commit()

cmd="INSERT INTO feedback (fullname, usn, contact, email, message) values (?, ?, ?, ?, ?)"
#cursor.execute(cmd, ("Amrutha", "4MW233AD002", "8073972157", "amrutha.23ad002@sode-edu.in", "This is good time to learn DevOps"))
connection.commit()

f = cursor.execute("SELECT * FROM feedback").fetchall()
print(f)
connection.close()

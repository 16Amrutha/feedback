from flask import Flask, render_template, request
import sqlite3
app = Flask(_name_)

@app.route("/")
def index():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    fullname = request.form.get('fullname')
    usn = request.form.get('usn')
    branch = request.form.get('branch')
    cgpa = request.form.get('cgpa')
    email = request.form.get('email')
    connection=sqlite3.connect('feedback.db')
    cursor=connection.cursor()
    cursor.execute('INSERT INTO FEEDBACK(fullname, usn, contact, email, message) values(?,?,?,?,?)',(fullname,usn,branch,cgpa,email))
    connection.commit()
    feedbacks=cursor.execute('select fullname,message from FEEDBACK').fetchall()
    return feedbacks

    return "Hello"+fullname

if _name_ == '_main_':
    app.run(debug=True)
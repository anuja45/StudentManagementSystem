from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anuja@2002",  
    database="student_db"
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100),
                    age INT,
                    course VARCHAR(100)
                )''')
conn.commit()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    course = request.form['course']
    cursor.execute("INSERT INTO students (name, email, age, course) VALUES (%s, %s, %s, %s)", (name, email, age, course))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_student(id):
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    course = request.form['course']
    cursor.execute("UPDATE students SET name=%s, email=%s, age=%s, course=%s WHERE id=%s", (name, email, age, course, id))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

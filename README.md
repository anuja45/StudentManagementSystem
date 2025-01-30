# Student Management System using Flask and MySQL

This is a simple Student Management System built using Flask and MySQL. It allows users to perform CRUD (Create, Read, Update, Delete) operations on student records.

## Features
- Add new students
- View all students
- Update student details
- Delete students
- MySQL database integration

## Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- MySQL Server
- Flask
- MySQL Connector for Python

## Installation
### 1. Clone the repository
```sh
git clone https://github.com/your-username/student-management-flask.git
cd student-management-flask
```

### 2. Install dependencies
```sh
pip install flask mysql-connector-python
```

### 3. Setup MySQL Database
Create a new database in MySQL:
```sql
CREATE DATABASE student_db;
USE student_db;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    age INT,
    course VARCHAR(100)
);
```

### 4. Configure Database Connection
Update `app.py` with your MySQL username and password:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",
    password="your_mysql_password",
    database="student_db"
)
```

### 5. Run the Application
```sh
python app.py
```

### 6. Open in Browser
Visit: `http://127.0.0.1:5000/`

## File Structure
```
student-management-flask/
│-- templates/
│   ├── index.html  # Frontend HTML template
│-- static/
│   ├── style.css   # CSS styling
│   ├── script.js   # JavaScript for UI functionality
│-- app.py          # Flask backend
│-- README.md       # Documentation
```

## Screenshots
(Include screenshots of the application here)

## License
This project is licensed under the MIT License.


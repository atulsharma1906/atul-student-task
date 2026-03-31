# 🚀 Student Data API (FastAPI + MySQL)

## 📌 Project Overview

This project is a **FastAPI-based backend application** that reads student data from a CSV file, stores it in a MySQL database, and exposes REST APIs to perform operations like fetching, filtering, updating, and deleting data.

---

## 🧱 Tech Stack

* Python
* FastAPI
* MySQL
* SQLAlchemy (ORM)
* Pandas

---

## 🔄 Project Flow

```text
CSV File → Pandas → MySQL Database → FastAPI → REST API
```

---

## 📂 Project Structure

```
student_task_api/
│
├── app/
│   ├── app.py          # Main FastAPI app
│   ├── db.py           # Database connection
│   ├── models.py       # Database models
│   ├── routes.py       # API routes
│   ├── schemas.py      # Pydantic schemas
│   
│
├── file_load.py        # CSV loading function
├── load_to_mysql.py    # Insert CSV data into MySQL
├── students_complete.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone (https://github.com/atulsharma1906/atul-student-task)
cd student_task_api
```

### 2️⃣ Create Virtual Environment

```
python -m venv atul
atul\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

1. Create MySQL database:

```
CREATE DATABASE student_db;
```

2. Database URL in `db.py`:

```
DATABASE_URL = "mysql+pymysql://root:atul1234@localhost/student_db"
```

---

## 📥 Load CSV Data into MySQL

Run:

```
python load_to_mysql.py
```

---

## ▶️ Run FastAPI Server

```
uvicorn app.app:app --reload
```

Open in browser:
👉 http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### 🔹 Get All Students

```
GET /student-data
```

### 🔹 Get Student by ID

```
GET /student-data/{student_id}
```

```

---

## 🔍 Additional Features

### ✔ Filtering

```
GET /students/filter?min_age=20
```

### ✔ Sorting (Top GPA)

```
GET /students/top-gpa?limit=5
```

### ✔ Pagination

```
GET /students?limit=10&offset=0
```


## 🧪 Health Check

```
GET /db-test
```

---

## 💯 Key Highlights

* CSV data processing using Pandas
* MySQL integration using SQLAlchemy
* Clean project structure
* RESTful API design
* Error handling
* Filtering, Sorting, Pagination

---

## 🧠 Learnings

* FastAPI framework usage
* Database integration with SQLAlchemy
* API design and architecture
* Backend project structuring

---

## 👨‍💻 Author

Atul Sharma

---

## ⭐ Conclusion

This project demonstrates a complete backend system with data processing, database integration, and API development using FastAPI.

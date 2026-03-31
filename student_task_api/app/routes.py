from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Optional

from app.db import SessionLocal
from app.model import Student
from file_load import file_load

router = APIRouter()


# =========================
# 🔹 DB Dependency
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# 🔹 DB CONNECTION TEST
# =========================
@router.get("/db-test")
def db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connected ✅"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =========================
# 🔹 GET ALL STUDENTS (DB)
# =========================
@router.get("/student-data")
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students


# =========================
# 🔹 GET STUDENT BY ID
# =========================
@router.get("/student-data/{student_id}")
def get_student(
    student_id: str = Path(..., description="Provide student ID", example="STU_1000"),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.student_id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


# =========================
# 🔹 CSV FILTER (AGE)
# =========================
@router.get("/students/filter_by_age")
def get_students_summary(
    age: int = Query(..., description="Minimum age")
):
    df = file_load()

    # Apply filter
    filtered = df[df['age'] >= age]

    # Handle empty result
    if filtered.empty:
        return {
            "total_students": 0,
            "students": []
        }

    # Count + details
    count = len(filtered)
    details = filtered.values.tolist()

    return {
        "total_students": count,
        "students": details
    }


# =========================
# 🔹 DB FILTER (AGE)
# =========================
@router.get("/students/db/filter_by_age")
def get_students_db_summary(
    age: int = Query(..., description="Minimum age"),
    db: Session = Depends(get_db)
):
    students = db.query(Student).filter(Student.age >= age).all()

    if not students:
        return {
            "total_students": 0,
            "students": []
        }

    count = len(students)

    # Convert to list format
    details = [
        [s.student_id, s.first_name, s.last_name, s.age, s.gpa]
        for s in students
    ]

    return {
        "total_students": count,
        "students": details
    }


# =========================
# 🔹 OPTIONAL: ADVANCED FILTER
# =========================
@router.get("/students/filter")
def advanced_filter(
    min_age: Optional[int] = Query(None),
    max_age: Optional[int] = Query(None)
):
    df = file_load()

    if min_age is not None:
        df = df[df['age'] >= min_age]

    if max_age is not None:
        df = df[df['age'] <= max_age]

    return df.values.tolist()

@router.get("/students/top-gpa")
def top_students(limit: int = 5, db: Session = Depends(get_db)):
    return db.query(Student).order_by(Student.gpa.desc()).limit(limit).all()

@router.get("/students")
def get_students(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return db.query(Student).offset(offset).limit(limit).all()



@router.get("/students/search")
def search_students(
    min_age: int = 0,
    city: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Student)

    if min_age:
        query = query.filter(Student.age >= min_age)

    if city:
        query = query.filter(Student.city == city)

    return query.all()
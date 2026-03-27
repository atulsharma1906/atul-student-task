from fastapi import APIRouter, Depends, HTTPException,Path
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.model import Student

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET ALL DATA
@router.get("/student-data")
def get_all_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


# GET BY ID
@router.get("/student-data/{student_id}")
def get_student(student_id: str=Path(description="PLEASE PROVIDE STUDENT ID " ,example='STU_1000'), db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id  == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
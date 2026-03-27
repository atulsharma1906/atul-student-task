from fastapi import APIRouter, HTTPException
from file_load import file_load
import numpy as np

app = APIRouter()

data = file_load()


@app.get("/student-data")
def get_all_student_data():
    return data



    
@app.get("/student-data/{student_id}")
def get_student(student_id: str):
    df = file_load()

    
    df['student_id'] = df['student_id'].astype(str)
    student = df[df['student_id'] == student_id]

    if student.empty:
        raise HTTPException(status_code=404, detail="Student not found")

    # Convert to JSON safe
    student = student.replace({np.nan: None})
    return student.to_json(orient="records")[0]
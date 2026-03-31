from pydantic import BaseModel
from typing import Optional, List, Dict


# 🔹 Base Student Schema (Common Fields)
class StudentBase(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    age: int
    major: str
    gpa: Optional[float] = None
    attendance: float
    scholarship: int
    city: str
    status: str


# 🔹 Full Student Response (for GET by ID / all data)
class StudentResponse(StudentBase):
    model_config = {"from_attributes": True}


# 🔹 Lightweight Response (for list APIs)
class StudentSummary(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    major: str
    gpa: Optional[float] = None
    city: str
    status: str

    model_config = {"from_attributes": True}


# 🔹 Pagination Response
class PaginatedStudents(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    data: List[StudentSummary]


# 🔹 Stats Response
class StatsSummary(BaseModel):
    total_students: int
    average_gpa: float
    average_attendance: float
    total_scholarship_awarded: int
    status_breakdown: Dict[str, int]
    major_breakdown: Dict[str, int]
    city_breakdown: Dict[str, int]


# 🔹 Error Response
class ErrorResponse(BaseModel):
    detail: str
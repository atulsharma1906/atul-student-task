from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    student_id = Column(String(20), primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    major = Column(String(100))
    gpa = Column(Float)
    attendance = Column(Float)
    scholarship = Column(Integer)
    city = Column(String(50))
    status = Column(String(50))
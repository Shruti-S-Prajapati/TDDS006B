from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students = {
    1: {"name": "shruti", "age": 20 },
    2:{"name": "Yukti", "age": 19}
}
class Student (BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {"message": "PUT API is running"}

@app.get("/students")
def get_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, student:Student):
    students[student_id] = student.model_dump()
    return students[student_id]
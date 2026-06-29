from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "This is my FastAPI app"
    }

@app.get("/view")
def view():

    students = [
        {
            "id": 1,
            "name": "Shruti",
            "age": 19,
            "course": "Data Science"
        },
        {
            "id": 2,
            "name": "Nancy",
            "age": 20,
            "course": "Computer Science"
        },
        {
            "id": 3,
            "name": "Yukti",
            "age": 18,
            "course": "Artificial Intelligence"
        },
        {
            "id": 4,
            "name":"Vishakha",
            "age": 21,
            "course":"Machine Learning"
        }
    ]

    return students
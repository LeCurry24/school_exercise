import uvicorn
from fastapi import FastAPI
from sqlmodel import Session, select
from db import engine
from models.courses import Course
from models.enrollments import Enrollment
from models.students import Student

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/courses")
def list_course():
    with Session(engine) as session:
        statement = select(courses)
        results = session.exec(statement).all()
    return results

@app.get("/enrollments")
def list_enrollment():
    with Session(engine) as session:
        statement = select(enrollments)
        results = session.exec(statement).all()
    return results

@app.get("/students")
def list_student():
    with Session(engine) as session:
        statement = select(Student)
        results = session.exec(statement).all()
    return results
    
if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
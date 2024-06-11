import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select, func
from db import get_session
from models.courses import Courses
from models.enrollments import Enrollments
from models.students import Students

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/courses")
def get_course(session: Session = Depends(get_session)):
    statement = select(Courses)
    results = session.exec(statement).all()
    return results
 

@app.get("/enrollments")
def get_enrollments(session: Session = Depends(get_session)):
    statement = select(
        Courses.name.label('course_name'),
        func.array_agg(Students.name).label('Students')
        ).select_from(
            Enrollments
        ).join(
            Students, Student.id == Enrollments.student_id
        ).join(
            Courses, Courses.id == Enrollments.course_id
        ).group_by(
            Courses.name
        )
    results = session.exec(statement).mapping().all()
    return results

@app.get("/students")
def get_student(session: Session = Depends(get_session)):
    statement = select(Students)
    results = session.exec(statement).all()
    return results
    
if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
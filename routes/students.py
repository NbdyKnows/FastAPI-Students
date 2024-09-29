from fastapi import APIRouter, Response, status
from config.db import conn
from models.student import students
from schemas.student import Student
from starlette.status import HTTP_204_NO_CONTENT

student = APIRouter()

@student.get("/students", response_model=list[Student])
def get_students():
    return conn.execute(students.select()).fetchall()


@student.post("/student/create", response_model=Student)
def create_students(student: Student):
    new_student = {"name": student.name, "nota": student.nota}
    result = conn.execute(students.insert().values(new_student))
    conn.commit()
    return conn.execute(students.select().where(students.c.id == result.lastrowid)).first()


@student.get("/student/{id}", response_model=Student)
def read_student(id: str):
    result = conn.execute(students.select().where(students.c.id == id)).first()
    if result:
        return dict(result._mapping)
    return "Error: Estudiante no encontrado"


@student.put("/student/update/{id}", response_model=Student)
def update_students(id: str, student: Student):
    conn.execute(students.update()
                .values(name= student.name, nota= student.nota)
                .where(students.c.id==id))
    conn.commit()
    return conn.execute(students.select().where(students.c.id == id)).first()


@student.delete("/student/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_students(id: str):
    conn.execute(students.delete().where(students.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
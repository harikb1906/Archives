from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from server.models.student import ResponseModel, ErrorResponseModel, StudentSchema, UpdateStudentModel


router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully")


@router.get("/", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved successfully")
    return ResponseModel(students, "Empty list returned")

@router.get("/{id}", response_description="Student data retrieved")
async def get_student_data(id):
    try:
        student = await retrieve_student(id)
        if student:
            return ResponseModel(student, "Student data retrieved successfully")
        else:
            return ErrorResponseModel("An error occured", 404, "Student doesn't exists.")
    except Exception as E:
        return ErrorResponseModel("An exception raised", 400, str(E))

# TODO Rest of tutorial (Mainly update and delete)
## https://testdriven.io/blog/fastapi-mongo/

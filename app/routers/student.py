from fastapi import APIRouter
from app.DTO.student_DTO import StudentDTO
from app.services.student import StudentService

router = APIRouter()
student_service = StudentService()


# @router.get("/students")
# def get_students():
#     return student_service.get_students()

@router.post("/students")
def create_student(student: StudentDTO):
    return student_service.create_student(student)

# @router.get("/students/{name}")
# def get_student(name: str):
#     return student_service.get_student(name)

# @router.put("/students/{name}")
# def update_student(name: str, new_students: Student):
#     return student_service.update_student(name, new_students)

# @router.delete("/students/{name}")
# def delete_student(name: str):
#     return student_service.delete_students(name)

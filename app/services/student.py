from app.models.student import Student
from app.DTO.student_DTO import StudentDTO
from app.configs.db.sqlite import session


class StudentService:

    def get_students(self):
        return self.students

    def create_student(self, student_dto: StudentDTO):
        student = Student(name=student_dto.name, age=student_dto.age, classes=student_dto.classes)
        student.crate_student(session)
        return student

    def get_student(self, name: str):
        for student in self.student:
            if student.name == name:
                return student
        return None

    def update_student(self, name: str, new_student: Student):
        for i, student in enumerate(self.students):
            if student.name == name:
                self.students[i] = new_student
                return True
        return False

    def delete_student(self, name: str):
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]
                return True
        return False

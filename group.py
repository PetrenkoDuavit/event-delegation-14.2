
from student import Student
from exceptions import GroupLimitError

class Group:
    def __init__(self, number, max_size=10):
        self.number = number
        self.max_size = max_size
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_size:
            raise GroupLimitError(f"Cannot add more than {self.max_size} students to the group.")
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                return

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Number: {self.number}\nStudents:\n{all_students}"

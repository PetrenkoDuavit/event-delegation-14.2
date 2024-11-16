
from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

# Добавляем студентов
gr.add_student(st1)
gr.add_student(st2)

# Проверяем
print(gr)
assert gr.find_student('Jobs') == st1  # Проверка сравнения
assert gr.find_student('Jobs2') is None

# Удаляем студента
gr.delete_student('Taylor')
print(gr)  # Должен остаться только один студент

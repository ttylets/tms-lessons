# Создайте файл university.py. Делайте задание в этом файле.
# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).

from students import Student
student = [
   Student('Иванов', 9),
   Student('Петров', 3),
   Student('Кабанова', 6),
]
scholarship_sum = 0
for i in student:
    scholarship_sum += i.get_scholarship()
print(scholarship_sum)

excellent_student = 0
for i in student:
    excellent_student += i.is_excellent()
print(excellent_student)


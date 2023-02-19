# Создайте файл friends.py. Делайте задание в этом файле.
# Импортируйте класс Person из первого задания
# from person import Person
# Создайте переменную my_friends - список из объектов класса Person.
# Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# Выведите информацию о каждом друге на экран.
# * Найдите среди друзей самого старшего, выведите информацию о нём на экран.
# * Выведите на экран информацию о всех друзьях мужского пола
# (можно использовать функцию filter, либо генератор списков).
# * Заверните код из пунктов 5 и 6 в функции get_oldest_pearson и filter_male_person
# соответственно.

from person import Person
my_friends = [
   Person('Ivan Ivanov', 20, 'M'),
   Person('Masha Petrova', 26, 'F'),
   Person('Anna Kabanova', 24, 'F'),
]
for i in my_friends:
    print(i.print_person_info())

for i in my_friends:
    print(i.print_person_info())







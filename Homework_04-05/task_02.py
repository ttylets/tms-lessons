# Программа выводит на экран числа от 0 до 100.
# После вывода каждого числа спрашивайте у пользователя “Should we break?”.
# Если он ответил “yes” - завершите программу.
# Иначе - продолжайте вывод чисел.

num = 0
for num in range(101):
    print(num)
    answer = input('Should we break? ')
    if answer == 'yes':
        break

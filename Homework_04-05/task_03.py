# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор, пока ответ не будет корректным.
num = 0
for num in range(101):
    answer = input('Should we break? ')
    if answer == 'no':
            print(num)
    elif answer == 'yes':
        break
    else:
        print("Don't understand you")

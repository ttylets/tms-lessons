# Пользователь вводит месяц и число. Выведите True, если такой день есть в году.
month = input('Введите месяц: ')
date = int(input('Введите число: '))
dict_a = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
          'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
print (dict_a.get(month) >= date)

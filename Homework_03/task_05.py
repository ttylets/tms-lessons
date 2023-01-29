# Пользователь вводит название месяца на английском. Выведите количество дней в этом месяце
# (не учитывая високосный год). Подсказка: понадобится создать dict: название месяца -> количество дней.
dict_a = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
          'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
mounth = input('Enter a month: ')
print(dict_a[mounth])

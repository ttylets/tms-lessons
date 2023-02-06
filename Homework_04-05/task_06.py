# Напишите функцию is_year_leap, которая принимает число (год) и возвращает True если год високосный
# (см. комментарий к слайда), False если нет.
def is_year_leap(year: int):
    return year % 4 == 0 and (year != 100 or year % 400 == 0)

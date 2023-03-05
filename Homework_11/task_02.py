# Напишите функцию is_date, которая принимает строку и возвращает bool. Функция должна вернуть True
# если переданная строка это дата в формате "DD-MM-YYYY", например "01-12-2022".

import re
def is_date(date: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', date) is not None

if __name__ == '__main__':
    assert is_date('25-11-1998')




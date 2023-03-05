# Напишите функцию is_float_number, которая принимает строку и возвращает bool.
# Функция должна вернуть True если переданная строка это корректное число с плавающей точкой. Например "1.0", "20.45".

import re

def is_float_number(num: str) -> bool:
    return re.fullmatch(r'\d+\.\d+', num) is not None

if __name__ == '__main__':
    assert is_float_number('2.5')
    assert not is_float_number('2,5')
    assert is_float_number('46.780')
    assert not is_float_number('46')




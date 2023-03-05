# Решите задание 4 с помощью генератора.
# Напишите функцию-генератор generate_words, которая принимает текст (слова и пробелы),
# разбивает их на слова и отдаёт (yield) по одному.
# Пример работы показан ниже.


def generate_words(text):
    words = text.split()
    for i in words:
        yield i

if __name__ == '__main__':
    text = 'мама мыла раму'
    for i in generate_words(text):
        print(i)

    assert ['мама', 'мыла', 'раму'] == [i for i in generate_words('мама мыла раму')]
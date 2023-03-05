# Создайте класс WordIterable, который в конструкторе принимает строку (текст) и итерируется по словам.
# Для простоты можно считать что текст это набор слов, разделённый только пробелами (никаких знаков препинания).
#То есть для разбиения можно использовать функцию split.

class WordIterable:
    def __init__(self, text):
        self.text = text
        self.count = 0
        self.word = self.text.split()

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.word):
            raise StopIteration()
        return self.word[self.count - 1]

if __name__ == '__main__':
    str = WordIterable('мама мыла раму')
    for i in str:
        print (i)

    assert ['мама', 'мыла', 'раму'] == [i for i in WordIterable('мама мыла раму')]

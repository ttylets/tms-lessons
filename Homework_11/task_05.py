# Сделайте прошлое задание, но в этот раз передаваемый в конструкторе текст
# может содержать любые знаки препинания и символы.
# Вам необходимо найти все слова (то есть подстроки, состоящие из букв).
# Используйте функцию re.findall.

import re

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
        return re.findall(r'\w+', self.word)

if __name__ == '__main__':
    str = WordIterable('мама мыла раму')
    for i in str:
        print (i)

    assert ['мама', 'мыла', 'раму'] == [i for i in WordIterable('мама мыла раму')]
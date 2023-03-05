import re

def generate_words(text):
    words = text.split()
    for i in words:
        yield re.findall(r'\w+', i)

if __name__ == '__main__':
    text = 'мама$ мыла раму'
    for i in generate_words(text):
        print(i)

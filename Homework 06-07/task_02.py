# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.
def remove_vowels():
    text = input().split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = list(filter(lambda text: text not in vowels, text))
    return(result)
print(remove_vowels())


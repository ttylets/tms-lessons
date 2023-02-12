# * Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре.
# Вам по прежнему нужно удалить все гласные.
# При этом вывести результат нужно вывести сохранив изначальный регистр.
def remove_vowels():
    text = list(input().split())
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = list(filter(lambda text: text not in vowels, text))
    return(result)
print(remove_vowels())

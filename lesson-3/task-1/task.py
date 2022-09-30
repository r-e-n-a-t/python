# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randrange

def createList(len):
    result = []
    for i in range(1, len + 1): result.append(randrange(0, 10))
    return result

def sumListElements(list):
    result = 0
    for i in range(0, len(list)):
        if i % 2 != 0: result += list[i]
    return result

listLength = int(input('Введите длину списка => '))
list = createList(listLength)
print(f'Ваш список - {list}')
print(f'Сумма нечетных элементов - {sumListElements(list)}')
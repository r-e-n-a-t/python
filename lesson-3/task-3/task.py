# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

def createList(len):
    result = []
    for i in range(1, len + 1): result.append(round(uniform(0.1, 10.0), 2))
    return result

def findDiff(list):
    a = list[0]
    b = list[len(list) - 1]
    while a > 1: a = a % 1
    while b > 1: b = b % 1
    return a - b if a - b > 0 else b - a
    
newList = []
listLength = int(input('Введите длину списка => '))
list = createList(listLength)
print(f'Ваш список - {list}')
print(f'Разница между максимальным и минимальным значением дробной части элементов - {round(findDiff(list), 2)}')
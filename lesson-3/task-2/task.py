# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randrange

def createList(len):
    result = []
    for i in range(1, len + 1): result.append(randrange(0, 10))
    return result

def multListElements(list, start, end):
    if start == end: newList.append(list[start] ** 2)
    if start >= end: return newList
    newList.append(list[start] * list[end])
    multListElements(list, start + 1, end - 1)
    
newList = []
listLength = int(input('Введите длину списка => '))
list = createList(listLength)
print(f'Ваш список - {list}')
multListElements(list, 0, len(list) - 1)
print(f'Сумма нечетных элементов - {newList}')
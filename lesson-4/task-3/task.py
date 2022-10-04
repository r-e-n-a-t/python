# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrange

def createList(len):
    result = []
    for i in range(1, len + 1): result.append(randrange(0, 10))
    return result

def foundRepeats(list):
    newList = []
    for i in list:
        if i not in newList: newList.append(i)
    return newList
    
list = createList(int(input('Введите длину списка => ')))
print(f'Ваш список - {list}')
print(f'Cписок неповторяющихся элементов исходной последовательности - {foundRepeats(list)}')
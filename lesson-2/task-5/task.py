# 5. Реализуйте алгоритм перемешивания списка.
from random import randrange

def createSequence(num):
    result = []
    for i in range(1, num + 1):
        result.append(i)
    return result

def shuffleList(list):
    for i in range(len(list) * 3):
        numOne = randrange(0, len(list))
        numTwo = randrange(0, len(list))
        temp = list[numOne]
        list[numOne] = list[numTwo]
        list[numTwo] = temp
    return list

listLength = int(input('Введите длину списка => '))
seq = createSequence(listLength)
print(f'Ваш список - {seq}')
print(f'Перемешанный список - {shuffleList(seq)}')
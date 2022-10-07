# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from random import randrange

def findSeq(list, index):
    result = [list[index]]
    max = list[index]
    for i in range(index, len(list)):
        if list[i] > max:
            max = list[i]
            result.append(max)
    return result
    
list = [randrange(0, 10) for i in range(int(input('Введите длину списка => ')))]
print(f'Ваш список - {list}')
for i in range(len(list)): 
    if len(findSeq(list, i)) > 1: print(findSeq(list, i))
print(f'Cписок неповторяющихся элементов исходной последовательности - {findSeq(list, 5)}')
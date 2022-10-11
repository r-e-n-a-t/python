# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

sum = 0
list = [random.randrange(10) for i in range(int(input('Введите длину списка => ')))]
for i in range(len(list)): 
    if i%2==0: sum += list[i]

print(f'Ваш список - {list}')
print(f'Сумма нечетных элементов - {sum}')
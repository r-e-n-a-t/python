# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randrange

def poly(k):
    poly = ''
    for i in reversed(range(k + 1)):
        r = randrange(1, 20)
        r = '' if r == 1 else f'{r}*'
        if i >= 2: poly += f'{r}X^{i} + '
        elif i == 1: poly += f'{r}X + '
        else: poly += f'{randrange(1, 20)} = 0'
    return poly

k = int(input('Введите степень => '))
poly = poly(k)
print(f'Многочлен степени {k} - {poly}')

with open("file", "w") as f:
    f.write(poly)

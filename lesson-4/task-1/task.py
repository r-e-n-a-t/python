# Вычислить число c заданной точностью d
import math

def pi(num):
    pi = math.pi
    return str(pi)[0:num + 2]

num = int(input('Введите количество чисел после запятой => '))
print(f'Число π = {pi(num)}')
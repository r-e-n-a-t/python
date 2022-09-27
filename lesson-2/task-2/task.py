# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import math

def sum(num):
    result = []
    for i in range(num):
        result.append(math.factorial(i + 1))
    return result

num = int(input('Введите число => '))
print(f'Набор произведений чисел от 1 до {num} - {sum(num)}')

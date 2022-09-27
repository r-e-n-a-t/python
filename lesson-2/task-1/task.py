# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum(num):
    result = 0
    for i in range(len(num)):
        if num[i] != '.':
            result += int(num[i])
    return result

num = input('Введите число => ')
print(f'Сумма его цифр - {sum(num)}')
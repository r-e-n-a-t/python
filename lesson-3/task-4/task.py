# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def binaryConverter(num):
    bin = ''
    while num > 1:
        bin = str(num % 2) + bin
        num //= 2
        if num == 1: bin = str(num % 2) + bin
    return bin

num = int(input('Введите число => '))
print(f'Ваше число в двоичной системе = {binaryConverter(num)}')
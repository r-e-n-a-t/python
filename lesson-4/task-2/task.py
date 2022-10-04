# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(round(i, 1))
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(round(n))
   return primfac

num = int(input('Введите число => '))
print(f'Список простых множителей числа \'{num}\' = {primfacs(num)}')
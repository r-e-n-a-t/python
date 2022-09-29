# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def createSequence(num):
    result = []
    for i in range(num + 1):
        if i != 0: result.append((1+1/(i))**i)
    return result

def sumList(list):
    result = 0
    for i in list:
        result += i
    return result

num = int(input('Введите число => '))
seq = createSequence(num)
print(f'Список из {num} чисел последовательности (1+1/{num})^{num} - {seq}')
print(f'Сумма чисел последовательности {sumList(seq)}')

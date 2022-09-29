# 4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

def createSequence(num):
    result = []
    for i in range(-num, num + 1):
        result.append(i)
    return result

def multiplyingNum(list, numOne, numTwo):
    return list[numOne - 1] * list[numTwo - 1]

listLength = int(input('Введите число => '))
seq = createSequence(listLength)
print(f'Список элементов - {seq}')
numOne = int(input('Введите позицию первого множителя => '))
numTwo = int(input('Введите позицию второго множителя => '))
print(f'Произведение элементов = {multiplyingNum(seq, numOne, numTwo)}')


# Создать иформационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.


from model import add_employees, find_employees, changes_employees, search
from logger import write_employees, read_employees, write_re

print('Выберите режим работы с данными сотрудников: ')
print('1. Внести данные нового сотрудника\n2. Поиск данных сотрудника по базе\n3. Вывести всех сотрудников на экран\n4. Внести изменения')
mode = input()
if mode == '1':
    write_employees(add_employees())

elif mode == '2':
    for i in find_employees(): print(i)

elif mode == '3':
    for i in search(''): print(i)

elif mode == '4':
    write_re(changes_employees())

else:
    print('Введено неверное значение!')
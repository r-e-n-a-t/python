def check_hollyday(day):
    if 0 < day < 8:
        if day > 5:
            return 'Выходной день'
        else:
            return 'Рабочий день'
    else: 
        return 'Такого дня недели нет'

day = int(input('Введите день недели => '))
print(check_hollyday(day))
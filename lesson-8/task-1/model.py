# Добавляем контакт
def add_employees():
    id = input('Введите ID: ')
    name = input('Введите имя: ')
    firstName = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    post = input('Введите должность: ')
    salary = input('Введите заработную плату: ')
    directory = id + ' ' + name + ' ' + firstName + ' ' + phone + ' ' + post + ' ' + salary + '\n'
    return directory

# Ищем контакт
def find_employees(f):
    a = input('Введите данные для поиска: ')
    findC = list(filter(lambda x: a in x, f))
    return findC

def changed_employees():
    id = input('Введите ID: ')
    name = input('Введите имя: ')
    firstName = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    post = input('Введите должность: ')
    salary = input('Введите заработную плату: ')
    directory = id + ' ' + name + ' ' + firstName + ' ' + phone + ' ' + post + ' ' + salary
    return directory


def changes_employees(mass):
    findC = find_employees(mass)
    index = mass.index(findC[0])
    mass[index] = changed_employees()
    return mass
    # print(findC)



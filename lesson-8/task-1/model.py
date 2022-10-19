def add_employees():
    id = input('Введите ID: ')
    name = input('Введите имя: ')
    firstName = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    post = input('Введите должность: ')
    salary = input('Введите заработную плату: ')
    directory = id + ' ' + name + ' ' + firstName + ' ' + phone + ' ' + post + ' ' + salary
    return directory

def find_employees():
    return search(input('Введите данные для поиска: '))

def changed_employees(str):
    strList = str.split()
    print('Что бы Вы хотели изменить? ')
    print('1. ID\n2. Имя\n3. Фамилию\n4. Номер телефона\n5. Должность\n6. Заработную плату')
    mode = input()
    newData = input('Новое значение => ')
    if mode == '1':
        strList[0] = newData
    elif mode == '2':
        strList[1] = newData
    elif mode == '3':
        strList[2] = newData
    elif mode == '4':
        strList[3] = newData
    elif mode == '5':
        strList[4] = newData
    elif mode == '6':
        strList[5] = newData
    return " ".join(strList)

def search(a):
    with open('employees.txt', 'r', encoding='utf-8') as f:
        return [i.strip() for i in f.readlines() if a in i]

def changes_employees():
    mass = search('')
    findC = find_employees()
    while findC == []:
        print('Ничего не найдено')
        findC = find_employees()
    if len(findC) > 1:
        print('Найденно несколько значений: ')
        for i in findC: print(i)
        findC = [findC[int(input('Введите номер нужного => ')) - 1]]
    for i in range(len(mass)):
        if mass[i] == findC[0]:
            mass[i] = changed_employees(findC[0])
    return mass



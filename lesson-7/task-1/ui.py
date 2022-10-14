# Создать телефонный справочник с возможностью импорта и экспорта данных .

import logger
import model

def show(list):
    for i in list: print(i)

def get_data(msg):
    return input(msg)

def menu():
    print('Телефонный справочник')
    print('Для создания контакта введите 1')
    print('Для поиска контакта введите 2')
    c = get_data('')
    if c == '1' or c == '2': return c
    return menu()

show(model.search(get_data('Введите данные для поиска в нижнем регистре => '))) if menu() == '2' else logger.save_data(get_data('Введите данные контакта в формате - ФИО || Телефон => '))
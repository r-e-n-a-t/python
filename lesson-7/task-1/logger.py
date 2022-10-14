def save_data(data):
    with open('file.txt', 'a', encoding='utf-8') as f:
        f.write('{}\n'.format(data).lower())
        print('Контакт записан')
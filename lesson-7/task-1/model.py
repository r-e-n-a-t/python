def search(data):
    with open('file.txt', 'r', encoding='utf-8') as f:
        return [i.strip() for i in f.readlines() if data in i]
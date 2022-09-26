# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def search_points(plane, len):
    sign_x = 1
    sign_y = 1

    if plane == 2: 
        sign_x = -1
    if plane == 3: 
        sign_x = -1
        sign_y = -1
    if plane == 4: 
        sign_y = -1

    if 0 < plane < 5:
        for i in range(1, len + 1):
            for j in range(1, len + 1):
                print(f'({i * sign_x}, {j * sign_y})')
    else:
        print("Вы ввели неверные данные")

len = int(input('Введите длинну координатной прямой => '))
plane = int(input('Введите номер плоскости => '))
search_points(plane, len)
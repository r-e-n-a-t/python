# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

def calc_distance(xa, ya, xb, yb):
    return round(math.sqrt(((xb - xa)**2) + ((yb - ya)**2)), 3)

xa = int(input('Введите координату x точки A => '))
ya = int(input('Введите координату y точки A => '))
xb = int(input('Введите координату x точки B => '))
yb = int(input('Введите координату y точки B => '))

distance = calc_distance(xa, ya, xb, yb)
print(f'Расстояние между точками - {distance}')
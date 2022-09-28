# 5. Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# in
# - 3
# - 6
# - 2
# - 1
# out
# 5.099

from cmath import sqrt

print('Введите координаты точки А')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
print('Введите координаты точки В')
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
dist = sqrt((x1-x2)**2 + (y1-y2)**2).real
print(f'расстояние = {round(dist,3)}')
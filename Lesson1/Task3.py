# 3. Напишите программу, которая принимает на вход
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
print('Введите координаты точки:')
x = int(input('x = '))
y = int(input('y = '))

if x == 0 and y == 0:
    print('Точка не принадлежит ни одной плоскости')
elif x == 0 and y != 0:
    print('Точка лежит на оси Y')
elif x != 0 and y == 0:
    print('Точка лежит на оси X')
elif x>0 and y > 0:
    print('I четверть')
elif x>0 and y < 0:
    print('II четверть')
elif x<0 and y < 0:
    print('III четверть')
# elif x<0 and y > 0:
else:
    print('IV четверть')

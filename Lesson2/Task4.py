# * 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos1 = int(input('Position one: '))
pos2 = int(input('Position two: '))
n = int(input('Number of elements: '))

len = 2*n+1
if n <= 0 or pos1 <= 0 or pos2 <= 0 or pos1 > len or pos2 > len:
    print('Input error')
else:
    list = []
    mult = 0
    for i in range(-n, n+1):
        list.append(i)
    mult = list[pos1-1] * list[pos2-1]

    print(f'-> {list}')
    print(f'-> {mult}')

# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def new_list(len_list):
    new_list = sample(list(range(1,len_list*2+1)),len_list)
    return new_list

def sum_odd(in_list):
    sum = 0
    for i in range(0,len(in_list),2):
        sum += in_list[i]
    return sum

my_list = new_list(int(input('Введите длину списка: ')))
print(my_list)
print(sum_odd(my_list))
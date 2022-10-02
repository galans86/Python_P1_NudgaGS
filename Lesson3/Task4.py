#  4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

from random import random

def new_list(len_list):
    if len_list <=0:
        return None
    new_list = []
    for i in range(len_list):
        new_list.append(round(random()*10,2))
    return new_list

def dif_min_max(in_list):
    if in_list == None:
        return 
    print(in_list)
    
    for i in range(len(in_list)):
        numb = round( in_list[i] * 100 ) % 100  
        if i==0:
            l_min = l_max = numb
        else:
            if numb < l_min:
                l_min = numb
            if numb > l_max:
                l_max = numb
    print(f'Min: {l_min}  Max: {l_max} Difference: {l_max - l_min}')


dif_min_max(new_list(int(input("Введите длину списка: "))))


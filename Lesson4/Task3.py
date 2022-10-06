# 3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!

from random import choices

def new_list(len_list: int):
    if len_list <=0:
        return
    new_list = choices(range(1,len_list+1),k=len_list)
    return new_list

def dif_list(in_list: list):
    out_list = []
    for i in range(0,len(in_list)):
        if in_list.count(in_list[i]) == 1:
            out_list.append(in_list[i])
    return out_list

n_list = new_list(int(input('Введите длину последовательностии: ')))
print(n_list)
print(dif_list(n_list))
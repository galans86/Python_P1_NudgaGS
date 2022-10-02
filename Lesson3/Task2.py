# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import sample

def new_list(len_list):
    if len_list <=0:
        return None
    new_list = sample(list(range(1,len_list*2+1)),len_list)
    return new_list

def mult_pair(in_list):
    if in_list == None:
        return None
        
    len_list = len(in_list) 
    if len_list % 2:
        len_range = len_list // 2 + 1
    else:
        len_range = len_list // 2

    mult_list = []
    for i in range(len_range):
        j = len_list - 1 - i
        print(j)
        if i == j:
            mult_list.append(in_list[i])
            return mult_list
        mult_list.append(in_list[i]*in_list[j])
    return mult_list
           
my_list = new_list(int(input('Введите длину списка: ')))
print(my_list)
print(mult_pair(my_list))
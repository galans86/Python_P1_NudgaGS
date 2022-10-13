# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

def gt(num_list:list):
    return [num_list[i] for i in range(1,len(num_list)) if num_list[i] > num_list[i-1] ]

from random import sample
def get_list(n:int):
    return sample(range(1,n*2+1),k = n)
    
n_list = get_list(int(input('Введите количество элементов: ')))
print(n_list)
print(gt(n_list))
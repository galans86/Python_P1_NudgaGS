# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

from random import sample


def get_list(n: int):
    if n <= 20:
        print('Input incorrect')
        return []
    return list(range(20, n+1))


def gt(num_list: list):
     return  list(filter( lambda i: not i % 20 or not i % 21, num_list))


print(gt(get_list(int(input('Введите число N > 20: ')))))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

from math import gcd

def simp(numb: int):
    if numb <= 0:
        return ('Input error')
    elif numb == 1:
        return list([numb])
    m_list = []
    i = 2
    while i:
        if i == numb:
            m_list.append(i)
            return m_list
        if gcd(numb, i) == i:
            m_list.append(i)

            numb //= i
            i = 2
        else:
            i += 1


print(simp(int(input('Введите натуральное число N: '))))

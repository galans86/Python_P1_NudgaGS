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
    m_list = []
    d = int(1) 
    i = int(2)
    while i > 1:
        if i == numb:
            m_list.append(i)
            return m_list
        d = gcd(numb, i)
        if d == i:
            m_list.append(i)
            numb /= i
        else:
            i += 1


print(simp(54))

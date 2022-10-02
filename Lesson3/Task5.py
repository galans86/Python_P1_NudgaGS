# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21


def neg_fib(n):
    if n < 0:
        return
    n_list = [0] * (n*2+1)

    for i in range(n,len(n_list)):
        if i == n:
            n_list[i] = 0
        elif i == n + 1:
            n_list[i]  = 1
        else:
            n_list[i] = n_list[i-1] + n_list[i-2]

        pos = n-(i-n)
        n_list[pos] =  n_list[i] * ( (-1)** (pos+1) )
        
    return n_list

print(neg_fib(int(input('Введите число: '))))
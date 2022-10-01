# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

numb_in = abs(float(input('Введите число: ')))
len = len(str(numb_in))
number = int(numb_in*10**len)
result = 0
while number != 0:
    result += int(number % 10)
    number /= 10
print(f'Сумма цифр равна {result}')
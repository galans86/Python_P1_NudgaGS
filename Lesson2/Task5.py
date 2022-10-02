# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

# from random import Random, random
import random

d = 10
list = list(range(d))
print(f' -> {list}')

for i in range(10):
 pos1 = random.randint(0,d-1)
 pos2 = random.randint(0,d-1)
 temp = list[pos1]
 list[pos1] = list[pos2]
 list[pos2] = temp

print(f' -> {list}')


# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
from random import sample
import random


def bot_count_cand(all_c, max_c):
    if max_c + 1 < all_c <= max_c * 2:
        return all_c - max_c - 1

    if all_c <= max_c:
        return all_c

    count_bot = random.randint(1, max_c)
    if (all_c - count_bot) <= max_c * 2:
        if all_c > max_c*2:
            return all_c - max_c*2

    return count_bot


def input_person(all_c, max_c):
    count = int(input(f'candies = {all_c} person: '))
    while max_c < count or count <= 0:
        print(f'{chr(10060)} You can take [1...{max_c}]{chr(127853)}')
        count = int(input(f'candies = {all_c} person: '))
    return count


def candies(all_c: int, max_c: int):

    m_l = sample('01', k=2)
    person = int(m_l[0])
    bot = int(m_l[1])

    count_bot = count_person = 0
    while all_c > 0:
        if bot == 1:
            count_bot = bot_count_cand(all_c, max_c)
            print(f'candies = {all_c} bot: {count_bot}')
            all_c -= count_bot
            if all_c == 0:
                return str(f'{chr(127942)} Bot WIN')
            if all_c > max_c:
                count_person = input_person(all_c,max_c)
                all_c -= count_person
            else:
                print(f'candies = {all_c} person: {all_c}')
                return str(f'{chr(127942)} Person WIN')

        else:
            if all_c > max_c:
                count_person = input_person(all_c, max_c)
                all_c -= count_person
            else:
                print(f'candies = {all_c} person: {all_c}')
                return str(f'{chr(127942)} Person WIN')

            count_bot = bot_count_cand(all_c, max_c)
            print(f'candies = {all_c} bot: {count_bot}')
            all_c -= count_bot
            if all_c == 0:
                return str(f'{chr(127942)} Bot WIN')

sweets = int(input('Enter number of sweets: '))
take = 28
if sweets < 2*take +1 or not sweets or sweets < 0:
    print('Incorrect input') 
else:
    print(f'\n{chr(127853)} There are {sweets} sweets on a table. You can take [1...{take}]{chr(127853)} ')
    print(candies(sweets, take))
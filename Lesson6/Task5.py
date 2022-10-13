# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
# 'автомобиль сегодня веселый', 'город позавчера утопичный']
from random import shuffle

def joker(i_list1: list, i_list2: list, i_list3: list, n: int, dist: bool):
    m_list = []
    while n > 0 and i_list1 and i_list2 and i_list3:
        n -= 1
        shuffle(i_list1)
        shuffle(i_list2)
        shuffle(i_list3)
        m_list.append(
            ' '.join(list(*zip(i_list1[:1], i_list2[:1], i_list3[:1]))))
        if dist:
            i_list1 = i_list1[1:]
            i_list2 = i_list2[1:]
            i_list3 = i_list3[1:]
    return m_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


print(joker(nouns, adverbs, adjectives, 10, True))
# print(joker(nouns, adverbs, adjectives, 10, False))

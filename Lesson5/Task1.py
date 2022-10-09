# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  В тексте используется разделитель пробел.

from random import choices


def text_new(n, word):
    if n <=0:  
        print('The data is incorrect')
        return ''
    new_line = ''
    new_list = []
    for i in range(n):
     a = choices(word, k=3)
     new_list.append(''.join(a))
     new_line += f'{new_list[i]} '
    return new_line


def del_from_text(word_d:str, in_line:str):
    m_list = in_line.split()
    n_line = ''
    for w in m_list:
     if w != word_d:
        n_line += f'{w} '
    return n_line


line= text_new(int(input('Введите количество слов в строке: ')), 'абв')
print(line)
print(del_from_text('абв',line))
# 4.* Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

from random import choices

def ch_list(len_list: int):
    if len_list <= 0:
        return
    o_list = choices(range(-10, 11), k=len_list)
    return o_list

def write_poly(k):
    c_list = ch_list(k+1)
    print(c_list)
    with open('poly.txt', 'a', encoding='utf-8') as m_file:
        if k <= 0:
            m_file.write('input error')
        for i in range(-k, 1):
            e = i*-1
            coef = c_list[i*-1]
            if (coef < 0 or e == k) and (abs(coef) > 1 or i == 0):
                m_file.write(f' {coef}')
            elif coef > 1 or (coef == 1 and i == 0):
                m_file.write(f' + {coef}')

            if coef and i < 0:
                if coef == 1:
                    m_file.write(f' + x')
                elif coef == -1:
                    m_file.write(f' -x')
                else:
                    m_file.write(f'*x')
                if e > 1:
                    m_file.write(f'^{e}')

        m_file.write(f' = 0\n')


with open('poly.txt', 'w', encoding='utf-8') as m_file:
    m_file.write('')

for i in range(0, 3):
    write_poly(int(input('Введите степень k: ')))

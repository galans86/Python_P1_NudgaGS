# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

def text_code(f_in, f_out):
    with open(f_in, 'r', encoding='utf-8') as file_in:
        line_list = file_in.readlines()

    with open(f_out, 'w', encoding='utf-8') as file_out:
        for line in line_list:
            s = line[0]
            n = 0
            for l in line:
                if l != s:
                    file_out.write(f'{s}{n}')
                    n = 0
                    s = l
                n += 1
            if s != '\n':
                file_out.write(f'{s}{n}')
            else:
                file_out.write(f'{s}')


def text_decode(f_in, f_out):
    with open(f_in, 'r', encoding='utf-8') as file_in:
        line_list = file_in.readlines()

    with open(f_out, 'w', encoding='utf-8') as file_out:
        for line in line_list:
            s = line[0]
            n = ''
            for l in line:
                if l.isdigit():
                    n += l
                elif n:
                    for i in range(0, int(n)):
                        file_out.write(s)
                    s = l
                    n = ''
            if n:
                for i in range(0, int(n)):
                    file_out.write(s)
            if l == '\n':
                file_out.write(l)


file_text = input('Enter the name of the file with the text: ')
file_code = input('Enter the file name to record: ')
file_decode = input('Enter the name of the file to decode: ')

text_code(file_text, file_code)
text_decode(file_code, file_decode)
print('done')


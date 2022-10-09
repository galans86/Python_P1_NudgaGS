# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

from random import sample


def player_input(value, table_dict):
    pos = int(
        input(f'Enter a number from 1 to 9. \nSelect a position {value}? '))
    while pos not in table_dict.keys():
        print('Incorrect input. Enter a number from 1 to 9.\n')
        pos = input(f'Select a position {value}? ')

    while table_dict[pos] != '':
        print('This cell is already occupied\n')
        pos = int(input(f'Select a position {value}? '))

    return pos


def check_win(table_dict, win_list):  # 5
    for win in win_list:
        count_0 = count_x = 0
        for val in win:
            if table_dict[int(val)] == 'x':
                count_x += 1
            elif table_dict[int(val)] == '0':
                count_0 += 1
        if count_x == 3:
            return 'x'
        elif count_0 == 3:
            return '0'
    return ''


def fill_win_list():
    w_list = ('123', '147', '159', '258', '369', '357', '456', '789')
    return w_list


def print_field(table_dict):
    for v in table_dict:
        if v in [1, 4, 7]:
            print('\n----------\n ')
        if table_dict[v] == 'x':
            print(chr(10060), end = '  ')
        elif table_dict[v] == '0':
            print(chr(128280), end = '  ')
        else:
            print(v, end = '   ')
    print('\n')

def tic_tac_toe():
    players_list = sample('0x', k=2)
    table_dict = {}.fromkeys(range(1, 10), '')
    win_list = fill_win_list()

    result = ''
    step = 0
    while step < 9 and result == '':
        for player in players_list:
            if step < 9 and result == '':
                print_field(table_dict)
                pos = player_input(player, table_dict)
                table_dict[pos] = player
                result = check_win(table_dict, win_list)
                step += 1
    
    print_field(table_dict)   
    if result == 'x':
        print(f'X WIN! {chr(127942)}{chr(127881)}\n')
    elif result == '0':
        print(f'0 WIN! {chr(127942)}{chr(127881)}\n')
    else:
        print(f'Drawn game! {chr(129309)}\n')


tic_tac_toe()

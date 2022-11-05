#Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - Бот.

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


def print_board(table_dict):
    line = f'{chr(128073)}\n\n'
    for v in table_dict:
        if v in [ 4, 7]:
            line += '\n\n'
        if table_dict[v] == 'x':
            line += f'{chr(10060)} '
        elif table_dict[v] == '0':
            line += f'{chr(128280)} '
        else:
            line+= f'  {v}  '
    return line

def bot_play(win_list,table_dict,player,bot):

    #ищем выигрышную комбинацию для бота
    for win in win_list:
        count_b = len([val for val in win if table_dict[int(val)] == bot ])
        count_e = len([val for val in win if table_dict[int(val)] == '' ])
        if count_b == 2 and count_e == 1:
            for val in win:
              if table_dict[int(val)] == '':
                 table_dict[int(val)] = bot
                 break
            return table_dict

    #ищем выигрышную позицию для игрока
    for win in win_list:
        count_p = len([val for val in win if table_dict[int(val)] == player ])
        count_e = len([val for val in win if table_dict[int(val)] == '' ])
        if count_p == 2 and count_e == 1:
            for val in win:
              if table_dict[int(val)] == '':
                 table_dict[int(val)] = bot
                 break
            return table_dict

    #пока что нет выигрышных, ищем свободные 2         
    for win in win_list:
        count_b = len([val for val in win if table_dict[int(val)] == bot ])
        count_e = len([val for val in win if table_dict[int(val)] == '' ])
        if count_b == 1 and count_e == 2:
            for val in win:
              if table_dict[int(val)] == '':
                 table_dict[int(val)] = bot
                 break
            return table_dict
    
    #пока что нет выигрышных, ищем свободные 3         
    for win in win_list:
        count_e = len([val for val in win if table_dict[int(val)] == '' ])
        if count_e == 3:
            for val in win:
              if table_dict[int(val)] == '':
                 table_dict[int(val)] = bot
                 break
            return table_dict
    
    #ищем любую оставшуюсю
    for pos in table_dict:
        if table_dict[pos] == '':
            table_dict[pos] = bot
            return table_dict

# def test():
#     win_list = fill_win_list()
#     table_dict = {}.fromkeys(range(1,10),'')
#     table_dict[1] = '0'
#     table_dict[2] = 'x'
#     table_dict[3] = '0'
#     table_dict[4] = 'x'
    # table_dict[9] = ''
    # table_dict = bot_play(win_list,table_dict,'0','x')
    # print(table_dict)
    # print(check_win(table_dict,win_list))
    
# test()
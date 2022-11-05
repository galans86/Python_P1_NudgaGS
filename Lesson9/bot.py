import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,  KeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from functions import *

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
PLAYER, POSITION = range(2)
#----
player = ''
bot = ''
table_dict = {}
win_list = []


# функция обратного вызова точки входа в разговор
def start(update, _):

    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пользователя
    logger.info("Игрок %s начал игру", user.first_name)
    
    # Список кнопок для ответа
    reply_keyboard = [[KeyboardButton(text='x'),KeyboardButton(text='0')]]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard,resize_keyboard = True, one_time_keyboard=True)
   
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Я бот Tic-Tac-Toe.\n'
        'Мы будем играть в крестики-нолики.\n'
        'Твой ход первый. Что ты выбираешь?\n'
        'х или 0?',
        reply_markup=markup_key,)
    # переходим к этапу `PLAYER`, это значит, что ответ
    return PLAYER


def player(update,_):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пользователя
    logger.info("Игрок %s выбрал: %s", user.first_name, update.message.text)
    
    # Запоминаем чем играют игрок и бот
    global player,bot
    player = update.message.text
    bot = 'x' if update.message.text == '0' else '0'

    # Инициализация 
    global table_dict, win_list
    table_dict = {}.fromkeys(range(1, 10), '')
    win_list = fill_win_list()

    # Список кнопок для ответа
    reply_keyboard = [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard,resize_keyboard = True, one_time_keyboard=True)
    
    # Выводим доску с вариантами выбора 
    update.message.reply_text(f'{print_board(table_dict)}'
                                '\n\nВыбери позицию от 1 до 9 \n',
                                reply_markup=markup_key,)
    # переходим к этапу `POSITION`, это значит, что ответ
    # отправленного сообщения в виде кнопок будет выбор игрока
    return POSITION

# Обрабатываем 
def position(update, _):
    global table_dict
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пользователя
    logger.info("Ввод %s значение: %s", user.first_name, update.message.text)

    # Список кнопок для ответа
    reply_keyboard = [['1', '2', '3', '4', '5', '6', '7', '8', '9']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard,resize_keyboard = True, one_time_keyboard=True)
   
    # ограничено фильтром
    pos = int(update.message.text)

    if table_dict[pos] != '':
      # Выводим доску с вариантами выбора 
      update.message.reply_text(f'Эта позиция занята. Игрок {player},\n'
                                'выбери другую позицию от 1 до 9.\n',
                                reply_markup=markup_key,)
      # переходим к этапу `POSITION`, повторный ввод
      return POSITION
    
    # Присваиваем новое значение
    table_dict[pos] = player
    result = check_win(table_dict, win_list)

    # Ход Бота
    if result == '' and '' in table_dict.values():
       table_dict = bot_play(win_list,table_dict, player,bot)
       result = check_win(table_dict, win_list)

    # Проверки выигрышных ситуаций
    if result == 'x':
       winner = user.first_name if player == 'x' else 'BOT'
       update.message.reply_text(f'{print_board(table_dict)}'
                                 f'\n\n{winner} WIN! {chr(127942)}{chr(127881)}\n', 
                                 reply_markup=ReplyKeyboardRemove())
    # Пишем в журнал пользователя
       logger.info("%s WIN", winner)

    elif result == '0':
       winner = user.first_name if player == '0' else 'BOT'
       update.message.reply_text(f'{print_board(table_dict)}'
                                 f'\n\n{winner} WIN! {chr(127942)}{chr(127881)}\n', 
                                 reply_markup=ReplyKeyboardRemove())
    # Пишем в журнал пользователя
       logger.info("%s WIN", winner)

    else:
        if '' in table_dict.values():
            # Выводим доску с вариантами выбора 
            update.message.reply_text(f'{print_board(table_dict)}'
                                       '\n\nВыбери позицию от 1 до 9 \n',
                                      reply_markup=markup_key,)
            return POSITION
        else:
          update.message.reply_text(f'{print_board(table_dict)}'
                                    f'\n\nDrawn game! {chr(129309)}\n', 
                                    reply_markup=ReplyKeyboardRemove())
    # Пишем в журнал пользователя
          logger.info(f"Drawn game with {user.first_name}")
    # Заканчиваем разговор.
    update.message.reply_text('Для начала новой игры нажмите /start',
                               reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END



# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text('END', 
                              reply_markup=ReplyKeyboardRemove() )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("TOKEN")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher
    # точка входа в разговор
    entry_points=[CommandHandler('start', start)],
    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями PLAYER, POSITION
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            PLAYER:   [MessageHandler(Filters.regex('^(x|0)$'), player)],
            POSITION: [MessageHandler(Filters.regex('^(1|2|3|4|5|6|7|8|9)$'), position)]
            # PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            # BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()  



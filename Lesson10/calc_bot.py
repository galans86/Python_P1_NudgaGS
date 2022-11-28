import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,  KeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from ratio import *   # функции вычисления для рац.чисел
from compl import *   # функции вычисления для компл.чисел
from logger import *  # запись в файл

from functions import *

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
TYPE, NUMBER_R1, OPERATION, NUMBER_R2, NUMBER_C1, OPERATION, NUMBER_C2 = range(7)
type = 1  # 1-ratio 2-complex
op = ''
n1_r = float(0)
n2_r = float(0)
n1_c = complex(0 + 0*1j)
n2_c = complex(0 + 0*1j)

# функция обратного вызова точки входа в разговор
def start(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пользователя
    logger.info(f'{user.first_name} start calc')

    # Список кнопок для ответа
    reply_keyboard = [[KeyboardButton(text='1'), KeyboardButton(text='2')]]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Calculator start.\n'
        '\nWorking with:\n'
        '1 - rational\n'
        '2 - complex\n'
        '/exit\n',
        reply_markup=markup_key,)
    return TYPE

# Определяем тип числа
def type(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал пользователя
    logger.info(f'{user.first_name} working with: {update.message.text}')
    # запоминаем тип числа
    global type
    type = int(update.message.text)
    #
    if type == 1:
        update.message.reply_text('\nEnter a number \n',
                                  reply_markup=ReplyKeyboardRemove(),)
    else:
        update.message.reply_text('\nEnter a complex number.\n'
                                  'Use space between real and imag parts.\n',
                                  reply_markup=ReplyKeyboardRemove(),)
    if type == 1:
        return NUMBER_R1
    else:
        return NUMBER_C1

# Ввод первого рационального числа
def number_r1(update, _):
    # Пишем в журнал пользователя
    logger.info(
        f'{update.message.from_user.first_name} enter: {update.message.text}')
    # запоминаем
    global n1_r
    n1_r = float(update.message.text)

    # Список кнопок для ответа
    reply_keyboard = [['+', '-', '*', '/', 'pow', 'sqrt', '//', '%']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

    # Выводим варианты выбора
    update.message.reply_text('\nOperation\n',
                              reply_markup=markup_key,)
    return OPERATION

# Ввод первого комплексного числа
def number_c1(update, _):
    # запоминаем
    global n1_c
    try:
        # записываем значение из строки
        n_l = update.message.text.split()
        n1_c = float(n_l[0]) + float(n_l[1])*1j
       # Пишем в журнал пользователя
        logger.info(
            f'{update.message.from_user.first_name} enter: {n1_c}')
    except:
        # Пишем в журнал пользователя
        logger.info(
            f'{update.message.from_user.first_name} enter: {update.message.text}')
        update.message.reply_text('\nEnter a complex number.\n'
                                  'Use space between real and imag parts.\n',
                                  reply_markup=ReplyKeyboardRemove(),)
        return NUMBER_C1

    # Список кнопок для ответа
    reply_keyboard = [['+', '-', '*', '/', 'pow', 'sqrt']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

    # Выводим варианты выбора
    update.message.reply_text('\nOperation\n',
                              reply_markup=markup_key,)
    return OPERATION

# Обработка ввода операции
def operation(update, _):
    # Пишем в журнал пользователя
    logger.info(
        f'{update.message.from_user.first_name} operation: {update.message.text}')
    global op
    op = str(update.message.text)
    if op != 'sqrt':
        if type == 1:
            update.message.reply_text('\nEnter a second number \n',
                                      reply_markup=ReplyKeyboardRemove(),)
        else:
            update.message.reply_text('\nEnter a second complex number.\n'
                                      'Use space between real and imag parts.\n',
                                      reply_markup=ReplyKeyboardRemove(),)
        if type == 1:
            return NUMBER_R2
        else:
            return NUMBER_C2
    else:
        if type == 1:
            result_r(update)
        else:
            result_c(update)
        return ConversationHandler.END

# Ввод второго рационального числа
def number_r2(update, _):
    # Пишем в журнал пользователя
    logger.info(
        f'{update.message.from_user.first_name} enter: {update.message.text}')
    # запоминаем
    global n2_r
    n2_r = float(update.message.text)

    result_r(update)
    return ConversationHandler.END

# Вычисление и вывод результата рац.числа
def result_r(update):
    result = calculate_r(n1_r, n2_r, op)
    logger.info(ratio_view_result(n1_r, n2_r, op, result))

    # Список кнопок для ответа
    reply_keyboard = [['/start', '/exit']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(f'{ save_ratio_logs(ratio_view_result(n1_r,n2_r,op,result))}\n',
                              reply_markup=markup_key)

# Ввод второго комплексного числа
def number_c2(update, _):
    # запоминаем
    global n2_c
    try:
        n_l = update.message.text.split()
        n2_c = float(n_l[0]) + float(n_l[1])*1j
        # Пишем в журнал пользователя
        logger.info(
            f'{update.message.from_user.first_name} enter: {n2_c}')
    except:
        # Пишем в журнал пользователя
        logger.info(
            f'{update.message.from_user.first_name} enter: {update.message.text}')
        update.message.reply_text('\nEnter a complex number.\n'
                                  'Use space between real and imag parts.\n',
                                  reply_markup=ReplyKeyboardRemove(),)
        return NUMBER_C2

    result_c(update)
    return ConversationHandler.END

# Вычисление и вывод комплексного числа
def result_c(update):
    result = calculate_c(n1_c, n2_c, op)
    logger.info(complex_view_result(n1_c, n2_c, op, result))

    # Список кнопок для ответа
    reply_keyboard = [['/start', '/exit']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(
        reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(f'{ save_complex_logs(complex_view_result(n1_c,n2_c,op,result))}\n',
                              reply_markup=markup_key)


# Обрабатываем команду /cancel если пользователь отменил разговор
def exit(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("%s exit", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text('END',
                              reply_markup=ReplyKeyboardRemove())
    # Заканчиваем разговор.
    return ConversationHandler.END


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("TOKEN")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher
    # точка входа в разговор
    entry_points = [CommandHandler('start', start)],
    # список кнопок для операции вычисления
    if type == 1:
        buttons = ['+', '-', '*', '/', 'pow', 'sqrt', '//', '%']
    else:
        buttons = ['+', '-', '*', '/', 'pow', 'sqrt']
    # с состояниями TYPE, NUMBER, OPERATION
    # Определяем обработчик разговоров `ConversationHandler`
    conv_handler = ConversationHandler(  # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            TYPE: [MessageHandler(Filters.regex('^(1|2)$'), type)],
            NUMBER_R1:   [MessageHandler(Filters.regex('^([-+]?(?:\d+(?:\.\d*)?|\.\d+))$'), number_r1)],
            OPERATION: [MessageHandler(Filters.text(buttons), operation)],
            NUMBER_R2:   [MessageHandler(Filters.regex('^([-+]?(?:\d+(?:\.\d*)?|\.\d+))$'), number_r2)],
            NUMBER_C1:   [MessageHandler(Filters.regex('^([-+]?(?:\d+(?:\.\d*)?|\.\d+) ?[-+]?(?:\d+(?:\.\d*)?|\.\d+))$'), number_c1)],
            NUMBER_C2:   [MessageHandler(Filters.regex('^([-+]?(?:\d+(?:\.\d*)?|\.\d+) ?[-+]?(?:\d+(?:\.\d*)?|\.\d+))$'), number_c2)]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('exit', exit)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

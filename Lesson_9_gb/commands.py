import random
from bot_config import dp, bot
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/start_candies')
b3 = KeyboardButton('/help')
rk_client = ReplyKeyboardMarkup()
rk_client.add(b1, b2, b3)

candies_total = 150
max_get = 28
game_on = False


def Bot_turn(max, total_candies):
    # result = total_candies % (max + 1)
    # if result == 0:
    #     result = random.randint(1, max) if total_candies >= max else total_candies

    if total_candies >= max:
        result = random.randint(1, max)
    else:
        result = total_candies
    return result


def check_win(total_candies):
    if total_candies <= 0:
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}, приветики! Я конфетный бот. '
                                                      f'Поиграешь со мной? Для начала игры необходимо '
                                                      f'ввести /start_candies',
                           reply_markup=rk_client)
    print(f'{message.from_user.id} - {message.from_user.username} - {message.text}')


@dp.message_handler(commands=['help'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'Я пока не то чтоб прям умный парень и умею лишь 2 вещи играть '
                                                      f'в конфеты (Для начала игры введи /start_candies) и выводить'
                                                      f' это сообщение :)')


@dp.message_handler(commands=['start_candies'])
async def CandiesRun(message: types.Message):
    global game_on
    global candies_total
    global max_get
    print(f'{message.from_user.username} Начал игру ')
    if game_on:
        await bot.send_message(message.from_user.id, text=f'Ну начнем игру заново.\n')
    candies_total = 150
    game_on = True
    await bot.send_message(message.from_user.id, text=f'Правила игры: На столе лежит {candies_total} конфет.\n'
                                                      f'Игроки по очереди берут конфеты,\n'
                                                      f'максимум - это {max_get} конфет.\n')
    first_turn = random.randint(1, 2)
    if first_turn == 1:
        await bot.send_message(message.from_user.id, text=f'{message.from_user.username} твой ход, сколько ты '
                                                          f'возьмешь конфет?')
    else:
        bot_turn = Bot_turn(max_get, candies_total)
        candies_total -= bot_turn
        await bot.send_message(message.from_user.id, text=f'Очередь бота!')
        await bot.send_message(message.from_user.id, text=f'Я уже забрал {bot_turn} конфет!\nНа столе '
                                                          f'осталось {candies_total} конфет.')
        await bot.send_message(message.from_user.id, text=f'Твоя очередь, дружок.\nСколько конфет ты возьмешь?\n'
                                                          f'Можно взять от 1 до {max_get} конфет')


@dp.message_handler()
async def anything(message: types.Message):
    global game_on
    global candies_total
    global max_get
    user_message = message.text
    print(f'{message.from_user.id} - {message.from_user.username} - {message.text}')
    if game_on:
        if user_message.isdigit():
            if 0 < int(user_message) <= max_get:
                candies_total -= int(user_message)
                await bot.send_message(message.from_user.id, text=f'Ты взял конфет: {user_message}.\nНа столе '
                                                                  f'осталось {candies_total} конфет.')
                if candies_total <= 0:
                    await bot.send_message(message.from_user.id, text=f'Ееее! Ты победил поздравляю!')
                    print(f'{message.from_user.username} победил ')
                    game_on = False
                    await bot.send_message(message.from_user.id, text=f'Для повтора игры введи /start_candies')
                else:
                    bot_turn = Bot_turn(max_get, candies_total)
                    candies_total -= bot_turn
                    await bot.send_message(message.from_user.id, text=f'Очередь бота!')
                    if candies_total <= 0:
                        await bot.send_message(message.from_user.id, text=f'Я забрал конфет: {bot_turn} и победил!')
                        game_on = False
                        await bot.send_message(message.from_user.id, text=f'Для повтора игры введи /start_candies')
                        print(f'{message.from_user.username} проиграл ')

                    else:
                        await bot.send_message(message.from_user.id, text=f'Я забрал конфет: {bot_turn} \nНа столе '
                                                                          f'осталось {candies_total} конфет.')
                        await bot.send_message(message.from_user.id, text=f'Теперь твоя очередь.')
            else:
                await bot.send_message(message.from_user.id, text=f'Ты хочешь взять {user_message} конфет, но можно '
                                                                  f'взять от 1 до {max_get} конфет. Сколько возьмешь?')
        else:
            await bot.send_message(message.from_user.id, text=f'Дружочек, попробуй еще раз')
    else:
        await bot.send_message(message.from_user.id, text=f'Я не такой умный парень, могу только играть в игру, '
                                                          f'для старта игры введи /start_candies')


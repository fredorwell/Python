# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется
# жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""
import random


def CandiesPVP(candies_total, max_get, player_id):
    while candies_total > 0:
        if player_id == 1:
            print(f'\nХодит Первый игрок')
        else:
            print(f'\nХодит второй игрок')
        print(f'Конфет на столе: {candies_total}')
        turn = int(input(f'Сколько ты возьмешь конфет, можно взять от 1 до 28: '))
        turn = CheckTurn(turn, max_get, candies_total)
        candies_total -= turn
        if candies_total == 0:
            if player_id == 1:
                print(f'Поздравляю, победил первый игрок')
            else:
                print(f'Поздравляю, победил второй игрок')
        else:
            if player_id == 1:
                player_id = 2
            elif player_id == 2:
                player_id = 1


def CandiesPVE(candies_total, max_get, player_id):
    while candies_total > 0:
        if player_id == 1:
            print(f'\nХодит Первый игрок')
            print(f'Конфет на столе: {candies_total}')
            turn = int(input(f'Сколько ты возьмешь конфет, можно взять от 1 до 28: '))
            turn = CheckTurn(turn, max_get, candies_total)
        else:
            print(f'\nХодит Бот')
            turn = BotTurn(max_get, candies_total)
            print(f'Бот взял {turn} конфет')
        candies_total -= turn

        if candies_total == 0:
            if player_id == 1:
                print(f'Поздравляю вы победили')
            else:
                print(f'Победил компьютер')
        else:
            if player_id == 1:
                player_id = 2
            elif player_id == 2:
                player_id = 1


def CheckTurn(value_turn, max, total_candies):
    if value_turn <= 0 or value_turn > max:
        value_turn = int(input(f'Ты не можешь взять {value_turn} конфет, можно взять от 1 до 28: '))
        if value_turn <= 0 or value_turn > max:
            print(f'Ты второй раз ошибся, нельзя взять {value_turn}. По этому будем считать что ты взял 1 конфету')
            value_turn = 1
    elif value_turn > total_candies:
        print(
            f'Ты не можешь взять {value_turn} конфет поскольку осталось всего {total_candies} конфет, будем считать что ты взял {total_candies} конфет.')
        value_turn = total_candies
    return value_turn


def BotTurn(max, total_candies):
    result = total_candies % (max + 1)
    if result == 0:
        result = random.randint(1, max) if total_candies >= max else total_candies
    return result


def CheckCountPlayer(value_players):
    if value_players < 1 or value_players > 2:
        print(f'Ты ввел не корректный режим игры, попробуй еще раз, либо введи "q" для выхода')
        value_players = int(input(f'Выберите режим игры: '))
        if value_players < 1 or value_players > 2:
            print(f'Ты второй раз ввел не корректный режим игры, поэтому поиграем против компьютера')
            value_players = 1
    return value_players


def CandiesRun():
    print('Правила игры: Игроки по очереди берут конфеты, максимум - это 28 конфет.\n')
    print('Игрок сделавший последний ход побеждает')
    candies_total = 150
    max_get = 28
    player_id = random.randint(1, 2)
    print('Выберите режим игры. 1 - против компьютера, 2 - против второго игрока')
    count_player = int(input(f'Выберите режим игры: '))
    count_player = CheckCountPlayer(count_player)
    if count_player == 2:
        CandiesPVP(candies_total, max_get, player_id)
    else:
        CandiesPVE(candies_total, max_get, player_id)



CandiesRun()

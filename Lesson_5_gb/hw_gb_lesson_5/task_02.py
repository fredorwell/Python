# Создайте программу для игры в ""Крестики-нолики"".

def print_desk(board):
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


# def CheckCountPlayer(value_players):
#     if value_players < 1 or value_players > 2:
#         print(f'Ты ввел не корректный режим игры, попробуй еще раз, либо введи "q" для выхода')
#         value_players = int(input(f'Выберите режим игры: '))
#         if value_players < 1 or value_players > 2:
#             print(f'Ты второй раз ввел не корректный режим игры, поэтому поиграем против компьютера')
#             value_players = 1
#     return value_players


def ticTacToeRun():
    print('Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один всегда крестики, другой всегда нолики). \n'
          'Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает. \n'
          'Первый ход делает игрок, ставящий крестики.')
    ticTacToePVP()
    # print('Выберите режим игры. 1 - против компьютера, 2 - против второго игрока')
    # count_player = int(input(f'Выберите режим игры: '))
    # count_player = CheckCountPlayer(count_player)
    # count_player = 2
    # if count_player == 2:
    #     ticTacToePVP()
    # else:
    #     ticTacToePVP()



def ticTacToePVP():
    print('\n')
    game_desk = list(range(1, 10))
    turn = 1
    win = False
    i = 0

    while win is not True:
        if i == 9:
            print_desk(game_desk)
            print('Ходы закончились, ничья!')
            break
        elif turn == 1:
            print('\nХод первого игрока')
            print_desk(game_desk)
            move = int(input('В какую ячейку поставить X: '))
            move = checkMove(game_desk, move)
            game_desk[move - 1] = 'X'
            if checkWin(game_desk):
                print('Победил игрок 1!')
                break
            else:
                turn = 2
                i += 1
        else:
            print('\nХод Второго игрока')
            print_desk(game_desk)
            move = int(input('В какую ячейку поставить O: '))
            move = checkMove(game_desk, move)
            game_desk[move - 1] = 'O'
            if checkWin(game_desk):
                print('Победил игрок 2!')
                break
            else:
                turn = 1
                i += 1


def checkMove(game_desk, move):
    if (0 < move < 10) and game_desk[move - 1] != 'X' and game_desk[move - 1] != 'O':
        return move
    else:
        move = checkMove(game_desk, int(input('Ты ввел не корректную ячейку, попробуй еще раз: ')))
        return move


def checkWin(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return True
    return False


ticTacToeRun()

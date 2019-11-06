# import random
x_choice = ''
o_choice = ''
x_move_1 = "X"
x_move_2 = "X"
x_move_3 = "X"
x_move_4 = "X"
o_move_1 = "O"
o_move_2 = "O"
o_move_3 = "O"
o_move_4 = "O"
x_moves = [x_move_1, x_move_2, x_move_3, x_move_4]
o_moves = [o_move_1, o_move_2, o_move_3, o_move_4]


player = ''
computer = 'O'


def game_rules_and_introduction():
    print("Welcome to TicTacToe",
          'The rules are simple. Get three in a row to win!')
    x_or_o = input("Would you like to be X or O")
    if x_or_o == 'x':
        print("X it is.")
    if x_or_o == 'o':
        print("Nope! You will be x.")


def player_input_for_game():
    player_choice = input("Pick a number between 1 and 9, 1 being the"
                          " left top corner, and nine being the bottom right corner")
    winning_combo = []
    if player_choice == 1:
        x_choice = x_move_1
    winning_combo +=
def game_board():
    board_lines = ['  ', '|', '-----', '------']
    # LINE ONE
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice,)
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    # LINE TWO
    print(board_lines[2], board_lines[3], board_lines[2])
    # LINE THREE
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    # LINE FOUR
    print(board_lines[2], board_lines[3], board_lines[2])
    # LINE FIVE
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
          x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )

game_rules_and_introduction()
player_input_for_game()
game_board()



x_choice = ''
o_choice = ''
x_move_1 = "X"
x_move_2 = "X"
x_move_3 = "X"
x_move_4 = "X"
o_move_1 = "O"
o_move_2 = "O"
o_move_3 = "O"
o_move_4 = "O"
x_moves = [x_move_1, x_move_2, x_move_3, x_move_4]
o_moves = [o_move_1, o_move_2, o_move_3, o_move_4]

def board_for_game():
    board_lines = ['  ', '|', '-----', '------']
    for x in range(1,4):
        print(board_lines[0], x_choice, o_choice, board_lines[1], board_lines[0],
              x_choice, o_choice, board_lines[1], board_lines[0], x_choice, o_choice, )
    for x in  range

board_for_game()

def numbers():
    for x in range(1, 2):
        print('  |  '.join(str(x) for x in range(1, 4)))
    print("---")
    for x in range(2, 4):
        vertical = x[2:3]
        print(str(vertical))
numbers()



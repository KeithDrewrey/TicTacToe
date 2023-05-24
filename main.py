import os
from os import system

### Create board ###

board = {
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
}

count = 0
taken = [0]
count +=1
game = True

def clear():
    for i in range(0,100):
        print ("\n")

def print_board():
    print(f"{board['1']}, |, {board['2']}, |, {board['3']}")
    print("------------")
    print(f"{board['4']}, |, {board['5']}, |, {board['6']}")
    print("------------")
    print(f"{board['7']}, |, {board['8']}, |, {board['9']}")
    print("\n", "\n")


def check_winner():
    global game
    winner = [player, player, player]
    winning_lines = [
        [board["1"], board["2"], board["3"]],
        [board["4"], board["5"], board["6"]],
        [board["7"], board["8"], board["9"]],
        [board["1"], board["4"], board["7"]],
        [board["2"], board["5"], board["8"]],
        [board["3"], board["6"], board["9"]],
        [board["1"], board["5"], board["9"]],
        [board["3"], board["5"], board["7"]],
         ]
    for line in winning_lines:
        if line == winner:
            print("The winner is", player)
            print_board()
            game = False

while game:
    print_board()
    if count == 10:
        print("It's a draw")
        game = False
    if count % 2 == 0:
        player = "X"
    else: player = "O"

    turn = int(input(f"Player {player}, which square do you want to choose? \n \n"))
    if turn in taken or turn > 9:
        print("Please enter a valid space on the board")

    else:
        print(game)
        taken.append(turn)
        turn = str(turn)
        board[turn] = player
        clear()
        check_winner()
        count +=1



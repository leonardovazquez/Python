# Tic Tac Toe with IA
# This is a small project developed by Leonardo Vazquez.
# It uses functions to solve the problem of the IA Computer, the interface and other things


# Import libraries
import random
import time

#  Definitions
board = [" " for x in range(10)]
x = "x"
o = "o"


# Clear screen
def clc():
    print('\n' * 150)


# Insert letter function
def insert_letter(letter, pos):
    board[pos] = letter


# Is a position free?
def space_free(pos):
    return board[pos] == " "


# Is the board full or not?
def board_full(b):
    if b.count(" ") > 1:
        return False
    else:
        return True


# Is "x" the winner or not?
def winner(b, x):
    a = [False for j in range(10)]
    v = [False for j in range(3)]
    h = [False for j in range(3)]
    d = [False for j in range(2)]

    for j in range(10):
        a[j] = b[j] == x

    for j in range(3):
        h[j] = a[1+(j*3)] and a[2+(j*3)] and a[3+(j*3)]
        v[j] = a[1+j] and a[4+j] and a[7+j]
        if j < 2:
            d[j] = a[5] and (a[1+j*2] and a[9-2*j])

    if h[0] or h[1] or h[2] or v[0] or v[1] or v[2] or d[0] or d[1]:
        return True
    else:
        return False


# The board. I mean, the "console-view"
def print_board(b):
    print("-------------------------")
    print("|       |       |       |")
    print("|   " + board[1] + "   |   " + board[2] + "   |   " + board[3] + "   |")
    print("|       |       |       |")
    print("-------------------------")
    print("|       |       |       |")
    print("|   " + board[4] + "   |   " + board[5] + "   |   " + board[6] + "   |")
    print("|       |       |       |")
    print("-------------------------")
    print("|       |       |       |")
    print("|   " + board[7] + "   |   " + board[8] + "   |   " + board[9] + "   |")
    print("|       |       |       |")
    print("-------------------------")


# Ok, here is the players move function
def player_move(y1):
    r = True
    while r:
        move = input("Please select a position between 1 to 9: ")
        try:
            move = int(move)
            if (move > 0) and (move < 10):
                if space_free(move):
                    insert_letter(y1, move)
                    r = False
                else:
                    print("That Position is occupied!")
        except:
            print("Please, type a number!")


# some random function definition
def random_fun(obj):
    lng = len(obj)
    r = random.randrange(0, lng)
    return obj[r]


# and here is the interesting thing, a few algorithms to give some intelligence to the computer
def computer_move():
    possible_pos = [j for j, letter in enumerate(board) if letter == " " and j != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possible_pos:
            board_2 = board[:]
            board_2[i] = let
            if winner(board_2, let):
                move = i
                return move

    corners = []
    for i in possible_pos:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = random_fun(corners)
        return move

    if 5 in possible_pos:
        move = 5
        return move

    edges = []
    for i in possible_pos:
        if i in [2, 4, 6, 8]:
            edges.append(i)

    if len(edges) > 0:
        move = random_fun(edges)
        return move


# To update the screen and the board
def update_screen():
    clc()
    print(" Tic Tac Toe Game with IA".upper())
    print_board(board)


# To publish the results and to question if you want to play again
def results():
    update_screen()
    if winner(board, x):
        print("You are the winner!")
    elif winner(board, o):
        print("The Computer is the winner!")
    else:
        print("No one is the winner!")
    play_again()


# It ends?
def ends():
    return board_full(board) or winner(board, x) or winner(board, o)


# The main part of the code of the game
def main():
    z = True
    run = True

    while z:
        q1: str = input("Do you want to start? yes/no: ")
        if q1 == "yes" or q1 == "no" or q1 == "y" or q1 == "n":
            z = False
            break
        else:
            print("I don't understand")

    while run:
        update_screen()
        if q1 == "yes" or q1 == "y":
            if ends():
                run = False
                results()
            player_move(x)
            update_screen()
            print("The IA is thinking..")
            time.sleep(2)
            if ends():
                run = False
                results()
            board[computer_move()] = "o"
        elif q1 == "no" or q1 == "n":
            if ends():
                run = False
                results()
            print("The IA is thinking..")
            time.sleep(2)
            board[computer_move()] = "o"
            update_screen()
            if ends():
                run = False
                results()
            player_move(x)


# Play again or not?
def play_again():
    z = True
    while z:
        enter = input("Do you want to play again?: ")
        if enter == "yes" or enter == "y":
            for i in range(10):
                board[i] = " "
            z = False
            main()
            results()
        elif enter == "n" or enter == "no":
            print("Ok! Bye")
            break
        else:
            print("I don't understand")


# initialization definition
def initialization():
    update_screen()
    main()
    results()


# initialization call
initialization()










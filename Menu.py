import sys
from Board import *
from Game import *


board = Board(5)
game = Game(board)

def initial_menu():
    while True:
        option = int(input("""
---------- Menu Quoridor ----------
         
            1. Initiate
             2. Exit
               option: """))
        print("-----------------------------------")
        if option == 1:
            board.add_symbol()
            game.add_white()
            game.add_black()
            white_turn()

        elif option == 2:
            sys.exit()

        else:
            print('Invalid option, try again')
            continue

def white_turn():
    while True:
        print()
        board.print_board()
        print()
        print("-------------White Turn-------------")
        option = int(input("""
1. Move
2. Block
option: """))
        if option == 1:
            game.white_move()
            game.winner()
            print("-----------------------------------")
            black_turn()
        if option == 2:
            game.white_blockade()
            game.winner()
            print("-----------------------------------")
            black_turn()
        else:
            continue

def black_turn():
    print()
    board.print_board()
    print()
    print("-------------Black Turn-------------")
    print("""
Black Turn
1. Move
2. Block""")
    print()        
    random_direction = random.randint(1, 2)
    if random_direction == 1:
        print("¡The black player moved!")
        game.black_move()
        game.winner()
        print()
        print("-----------------------------------")
    if random_direction == 2:
        print("¡Black player locks a cell!")
        game.black_blockade()
        game.winner()
        print()
        print("-----------------------------------")
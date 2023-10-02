import sys
from Board import *
from Game import *


board = Board(5)
game = Game(board)

def initial_menu():
        print("""
__________ Menu Quoridor __________
          
            1. Initiate
             2. Exit""")
        while True:
            option = int(input("             option: "))
            print("___________________________________")
            if option == 1:
                if option == 1:
                    board.add_symbol()
                    game.add_white()
                    game.add_black()
                    board.print_board()
                    game_menu()

            elif option == 2:
                sys.exit()

            else:
                print('Opcion inválida, intente de nuevo.')
                continue

def game_menu():
    while True:
        print("""
White Turn
1. Move
2. Block""")
        option = int(input("option: "))
        print("___________________________________")
        if option == 1:
            game.white_move()
        if option == 2:
            game.white_blockade()
        else:
            print('Opcion inválida, intente de nuevo.')
            continue
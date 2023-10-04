import sys
import random
from Board import Board
from Game import Game


board = Board(int(input("Enter board size: ")))
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
            game_turns()
            break

        elif option == 2:
            sys.exit()

        else:
            print('Invalid option, try again')
            continue

def game_turns():
    while True:

        print()
        board.print_board()
        print()

        print("-------------White Turn-------------")
        white_option = int(input("""
1. Move
2. Block
option: """))
        if white_option == 1:
            game.white_move()
            print("-----------------------------------")
        if white_option == 2:
            game.white_blockade()
            print("-----------------------------------")
        
        # Verificar si hay un ganador después del turno del jugador blanco
        winner = game.winner()
        if winner:
            print("Game Over!")
            break

        print()
        board.print_board()
        print()
        print("-------------Black Turn-------------")
        print("""
Black Turn
1. Move
2. Block""")
        print()        
        black_option  = random.randint(1, 2)
        if black_option  == 1:
            print("¡The black player moved!")
            game.black_move()
            print("-----------------------------------")
        if black_option  == 2:
            game.black_blockade()
            print("-----------------------------------")

        # Verificar si hay un ganador después del turno del jugador negro
        winner = game.winner()
        if winner:
            print("Game Over!")
            break
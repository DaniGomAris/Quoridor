import sys
from Board import *
from Game import *

class MenuConsole:

    def game_menu(self):
        print("""
White Turn
1. Move
2. Block""")
        while True:
            option = int(input("option: "))
            print("___________________________________")
            if option == 1:
                self.board.white_move()
            if option == 2:
                self.board.white_blockade()
            else:
                print('Opcion inválida, intente de nuevo.')
                continue
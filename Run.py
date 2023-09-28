from Menu import *
from Game import *
from Menu import *
import random

if __name__ == "__main__":
    print("""
__________ Menu Quoridor __________
          
            1. Initiate
             2. Exit""")
    while True:
        option = int(input("             option: "))
        print("___________________________________")
        if option == 1:
            if option == 1:
                board = Board(9)
                board.print_board()
                MenuConsole.game_menu()

        elif option == 2:
            sys.exit()

        else:
            print('Opcion inválida, intente de nuevo.')
            continue
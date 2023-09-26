from Board import Board
import sys

if __name__ == "__main__":
    option = int(input("""
__________ Menu Quoridor __________
          
            1. Iniciar
             2. Salir
             option: """))
    print("___________________________________")
    while True:
        if option == 1:
            board1 = Board(9)
            board1.print_board()
            break
        elif option == 2:
            sys.exit()
        else:
            print('Opcion inválida, intente de nuevo.')
            continue
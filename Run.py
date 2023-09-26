from Board import Board
import sys

if __name__ == "__main__":
    print("""
__________ Menu Quoridor __________
          
            1. Iniciar
             2. Salir""")
    while True:
        option = int(input("             option: "))
        print("___________________________________")
        if option == 1:
            board1 = Board(9)
            board1.print_board()
            break
        elif option == 2:
            sys.exit()
        else:
            print('Opcion inválida, intente de nuevo.')
            continue
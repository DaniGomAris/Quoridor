from Board import Board
import random

class Game:
    def __init__(self):
        self.board = None
        self.white_pos = None
        self.black_pos = None

    def add_white(self):
        self.white_pos = self.board.white_initial_position()

    def add_black(self):
        self.black_pos = self.board.black_initial_position()

    def white_move(self):
        print(
"""
Direcciones 
1.arriba 
2.abajo 
3.izquierda 
4.derecha 
""")
        while True:
            new_row, new_col = self.white_pos
            direction = int(input("opcion:  "))

            if direction == '1': # Arriba
                new_row -= 1
            elif direction == '2': # Abajo
                new_row += 1
            elif direction == '3': # Izquierda
                new_col -= 1
            elif direction == '4': # Derecha
                new_col += 1
            else:
                print('Dirección inválidan intente de nuevo.')
                continue

            if self.board.valid_position(new_row, new_col):
                self.white_pos = (new_row, new_col)

    def black_move(self):
        while True:
            new_row, new_col = self.black_pos

            random_direction = random.randint(1, 4)

            if random_direction == 1:  # Arriba
                new_row -= 1
            elif random_direction == 2:  # Abajo
                new_row += 1
            elif random_direction == 3:  # Izquierda
                new_col -= 1
            elif random_direction == 4:  # Derecha
                new_col += 1
            else:
                print('Direccion inválida, intente de nuevo.')
                continue

            if self.board.valid_position(new_row, new_col):
                self.black_pos = (new_row, new_col)
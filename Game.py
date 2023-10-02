import random
from Board import *
from LinkedList import *

class Game:
    def __init__(self, board):
        self.board = board
        self.white_pos = None
        self.black_pos = None

    def add_white(self):
        self.white_pos = self.board.white_initial_position()

    def add_black(self):
        self.black_pos = self.board.black_initial_position()

    def white_move(self):
        while True:
            direction = int(input(
"""
Directions
1.up 
2.down 
3.left 
4.right
option:"""))
            new_row, new_col = self.white_pos

            if direction == 1: # Arriba
                new_row -= 1
            elif direction == 2: # Abajo
                new_row += 1
            elif direction == 3: # Izquierda
                new_col -= 1
            elif direction == 4: # Derecha
                new_col += 1
            else:
                print('Dirección inválida. Intente de nuevo.')
                continue

            if self.board.valid_position(new_row, new_col):

                node_value = self.board.get_cell_value(new_row, new_col)

                if node_value == '🟨':
                    print("--------------------White's play--------------------")
                    print("You can't move there is a locked cell")
                    return
                else:
                    self.board.set_cell(new_row, new_col, '⚪')
                self.white_pos = (new_row, new_col)
                self.board.print_board()
                return
            else:
                print("You can't move there")

    def black_move(self):
        while True:
            random_direction = random.randint(1, 4)
            new_row, new_col = self.black_pos

            if random_direction == 1:  # Arriba
                new_row -= 1
            elif random_direction == 2:  # Abajo
                new_row += 1
            elif random_direction == 3:  # Izquierda
                new_col -= 1
            elif random_direction == 4:  # Derecha
                new_col += 1
            else:
                continue

            if self.board.valid_position(new_row, new_col):

                node_value = self.board.get_cell_value(new_row, new_col)

                if node_value == '🟨':
                    print("--------------------Black's play--------------------")
                    print("You can't move there is a locked cell")
                    return
                else:
                    self.board.set_cell(new_row, new_col, '⚫')
                self.black_pos = (new_row, new_col)
                return
            else:
                print("You can't move there")

    def white_blockade(self):
        while True:
            # Solicitar al usuario las coordenadas de fila y columna para bloquear una casilla
            row = int(input("Ingrese la fila para bloquear: "))
            col = int(input("Ingrese la columna para bloquear: "))
                
            # Verificar si la posición está fuera del rango válido
            if not self.board.valid_position(row, col):
                print("Posicion fuera de rango, intente de nuevo")
                continue  # Continuar con el próximo intento si la posición es inválida

            # Verificar si la casilla seleccionada ya está bloqueada
            if self.board.get_cell_value(row, col) == '🟨':
                print("La casilla ya esta bloqueada, intente de nuevo")
                continue  # Continuar con el próximo intento si la casilla ya está bloqueada

            # Verificar si la casilla seleccionada esta el jugador negro
            if self.board.get_cell_value(row, col) == '⚫':
                print("En la casilla esta el jugador negro, intente de nuevo")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            # Bloquear la casilla en el tablero
            self.board.set_cell(row, col, '🟨')
            print(f"Jugador blanco bloquea la casilla en la fila {row} y columna {col}.")
            break
    
    def black_blockade(self):
        while True:
            # Generar coordenadas aleatorias para bloquear una casilla
            row = random.randint(0, self.board.n - 1)
            col = random.randint(0, self.board.n - 1)

            # Verificar si la posición está fuera del rango válido
            if not self.board.valid_position(row, col):
                print("Posicion fuera de rango, intente de nuevo")
                continue  # Continuar con el próximo intento si la posición es inválida
                
            # Verificar si la casilla seleccionada ya está bloqueada
            if self.board.get_cell_value(row, col) == '🟨':
                print("La casilla ya esta bloqueada, intente de nuevo")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente
            
            # Verificar si la casilla seleccionada esta el jugador blanco
            if self.board.get_cell_value(row, col) == '⚪':
                print("En la casilla esta el jugador blanco, intente de nuevo")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            # Bloquear la casilla en el tablero
            self.board.set_cell(row, col, '🟨')
            print(f"Jugador negro bloquea la casilla en la fila {row} y columna {col}.")
            break

    def winner(self):
        white_row = self.white_pos
        black_row = self.black_pos
        n = self.board.n

        if white_row == 0:
            print("¡El jugador blanco es el ganador!")
            return 
        elif black_row == n - 1:
            print("¡El jugador negro es el ganador!")
            return 
        else:
            return None
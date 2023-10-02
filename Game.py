import random

class Game:
    def __init__(self, board):
        self.board = board
        self.white_pos = None
        self.black_pos = None

    def add_white(self):
        self.white_pos = self.board.white_initial_position()

    def add_black(self):
        self.black_pos = self.board.black_initial_position()

    def jump_two_spaces(self, row, col, direction):
        if direction == 1:  # Arriba
            row -= 1
            #row -= 1
        elif direction == 2:  # Abajo
            row += 1
            #row += 1
        elif direction == 3:  # Izquierda
            col -= 1
            #col -= 1
        elif direction == 4:  # Derecha
            col += 1
            #col += 1

        return row, col

    def white_move(self):
        while True:
            direction = int(input(
"""
Directions
1.up 
2.down 
3.left 
4.right
option: """))
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
                print('Invalid address, try again')
                continue

            if self.board.valid_position(new_row, new_col):

                node_value = self.board.get_cell_value(new_row, new_col)

                if node_value == '🟨':
                    print("You can't move there is a locked cell")
                    return
                
                if node_value == '⚫':
                    jump_row, jump_col = self.jump_two_spaces(new_row, new_col, direction)
                    self.board.set_cell(*self.white_pos, '🟫')  # Restaurar la celda original
                    self.board.set_cell(jump_row, jump_col, '⚪')  # Mover al jugador
                    self.white_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                    print("In this direction is the black player, you jump 2 cells")
                    return
                
                else:
                    self.board.set_cell(*self.white_pos, '🟫')
                    self.board.set_cell(new_row, new_col, '⚪')
                self.white_pos = (new_row, new_col)
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
                    print("You can't move there is a locked cell")
                    return
                
                if node_value == '⚪':
                    jump_row, jump_col = self.jump_two_spaces(new_row, new_col, random_direction)
                    self.board.set_cell(*self.black_pos, '🟫')  # Restaurar la celda original
                    self.board.set_cell(jump_row, jump_col, '⚫')  # Mover al jugador
                    self.black_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                    print("In this direction is the white player, you jump 2 cells")
                    return
                
                else:
                    self.board.set_cell(*self.black_pos, '🟫')
                    self.board.set_cell(new_row, new_col, '⚫')
                self.black_pos = (new_row, new_col)
                return
            
            else:
                print("You can't move there")

    def white_blockade(self):
        while True:
            # Solicitar al usuario las coordenadas de fila y columna para bloquear una casilla
            row = int(input("Enter the row to lock: "))
            col = int(input("Enter the column to lock: "))
                
            # Verificar si la posición está fuera del rango válido
            if not self.board.valid_position(row, col):
                print()
                print("Out of range position, try again")
                continue  # Continuar con el próximo intento si la posición es inválida

            # Verificar si la casilla seleccionada ya está bloqueada
            if self.board.get_cell_value(row, col) == '🟨':
                print()
                print("The cell is already locked, try again")
                continue  # Continuar con el próximo intento si la casilla ya está bloqueada

            # Verificar si la casilla seleccionada esta el jugador negro
            if self.board.get_cell_value(row, col) == '⚫':
                print()
                print("In the cell is the black player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            # Verificar si la casilla seleccionada esta el jugador blanco
            if self.board.get_cell_value(row, col) == '⚪':
                print()
                print("In the cell is the white player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            # Bloquear la casilla en el tablero
            self.board.set_cell(row, col, '🟨')
            print(f"White player locks the box in the row {row} y column {col}")
            break
    
    def black_blockade(self):
        while True:
            # Generar coordenadas aleatorias para bloquear una casilla
            row = random.randint(0, self.board.n - 1)
            col = random.randint(0, self.board.n - 1)

            # Verificar si la posición está fuera del rango válido
            if not self.board.valid_position(row, col):
                print()
                print("Out of range position, try again")
                continue  # Continuar con el próximo intento si la posición es inválida
                
            # Verificar si la casilla seleccionada ya está bloqueada
            if self.board.get_cell_value(row, col) == '🟨':
                print()
                print("The cell is already locked, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente
            
            # Verificar si la casilla seleccionada esta el jugador blanco
            if self.board.get_cell_value(row, col) == '⚪':
                print()
                print("In the cell is the white player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            # Verificar si la casilla seleccionada esta el jugador negro
            if self.board.get_cell_value(row, col) == '⚫':
                print()
                print("In the cell is the black player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            # Bloquear la casilla en el tablero
            self.board.set_cell(row, col, '🟨')
            print(f"Black player locks the box in the row {row} y column {col}")
            break

    def winner(self):
        white_row, _ = self.white_pos
        black_row, _ = self.black_pos
        n = self.board.n

        if white_row == 0:
            print("¡The white's player is winner!")
            self.board.print_board()
            return "white"
        if black_row == n - 1:
            print("¡The black's player is winner!")
            self.board.print_board()
            return "black"
        else:
            return None
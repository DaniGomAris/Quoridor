import random

class Game:
    def __init__(self, board):
        # Inicializa el juego con un tablero y las posiciones iniciales de los jugadores
        self.board = board
        self.white_pos = None
        self.black_pos = None

    def add_white(self):
        self.white_pos = self.board.white_initial_position() # Asigna la posición inicial del jugador blanco en el tablero

    def add_black(self):
        self.black_pos = self.board.black_initial_position() # Asigna la posición inicial del jugador negro en el tablero

    def jump_two_spaces(self, row, col, direction):
        # Despues de saltar una vez, vuelve y salta por eso se le vuelve a sumar +1, si fuera +2 saltaria 3 espacios
        if direction == 1:  # Arriba
            row -= 1
        elif direction == 2:  # Abajo
            row += 1
        elif direction == 3:  # Izquierda
            col -= 1
        elif direction == 4:  # Derecha
            col += 1

        if self.board.valid_position(row, col): # Verifica si la nueva posición (row, col) está dentro de los límites del tablero
                node_value = self.board.get_cell_value(row, col) # Obtiene el valor de la celda en la nueva posición

                if node_value == '🟨': # Si la celda es una celda bloqueada
                    print("You can't move there is a locked cell")
                    if direction == 1:  # Arriba
                        row += 2
                    elif direction == 2:  # Abajo
                        row -= 2
                    elif direction == 3:  # Izquierda
                        col += 2
                    elif direction == 4:  # Derecha
                        col -= 2
    
        return row, col

    def white_move(self):
        while True:
            direction = int(input(
"""
Directions
1. up 
2. down 
3. left 
4. right
option: """))
            
            new_row, new_col = self.white_pos # Obtiene las coordenadas actuales del jugador blanco (fila y columna) en la forma (new_row, new_col)

            if direction == 1:  # Arriba
                new_row -= 1
            elif direction == 2:  # Abajo
                new_row += 1
            elif direction == 3:  # Izquierda
                new_col -= 1
            elif direction == 4:  # Derecha
                new_col += 1
            else:
                print('Invalid address, try again')
                continue

            if self.board.valid_position(new_row, new_col): # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
                node_value = self.board.get_cell_value(new_row, new_col) # Obtiene el valor de la celda en la nueva posición

                if node_value == '🟨': # Si la celda es una celda bloqueada
                    print("You can't move there is a locked cell")
                    return

                if node_value == '⚫': # Si la direccion es el jugador negro
                    jump_row, jump_col = self.jump_two_spaces(new_row, new_col, direction) # El jugador blanco salta dos celdas si hay un jugador negro en la dirección
                    self.board.set_cell(*self.white_pos, '🟫')  # Restaurar la celda original
                    self.board.set_cell(jump_row, jump_col, '⚪')  # Mover al jugador blanco
                    self.white_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                    print("In this direction is the black player, you jump 2 cells")
                    return

                else:
                    self.board.set_cell(*self.white_pos, '🟫') # Restaurar la celda original
                    self.board.set_cell(new_row, new_col, '⚪')  # Mover al jugador blanco
                self.white_pos = (new_row, new_col) # Actualizar la nueva posición
                return

            else:
                print("You can't move there")

    def black_move(self):
        while True:
            # El jugador negro mueve aleatoriamente en una dirección válida
            random_direction = random.randint(1, 4)
            new_row, new_col = self.black_pos # Obtiene las coordenadas actuales del jugador negro (fila, columna) en la forma (new_row, new_col)

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

            if self.board.valid_position(new_row, new_col): # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
                node_value = self.board.get_cell_value(new_row, new_col) # Obtiene el valor de la celda en la nueva posición

                if node_value == '🟨': # Si la celda es una celda bloqueada
                    print("You can't move there is a locked cell")
                    return

                if node_value == '⚪': # Si en la direccion es el jugador blanco
                    jump_row, jump_col = self.jump_two_spaces(new_row, new_col, random_direction) # El jugador negro salta dos celdas si hay un jugador blanco en la dirección
                    self.board.set_cell(*self.black_pos, '🟫')  # Restaurar la celda original
                    self.board.set_cell(jump_row, jump_col, '⚫')  # Mover al jugador negro
                    self.black_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                    print("In this direction is the white player, you jump 2 cells")
                    return

                else:
                    self.board.set_cell(*self.black_pos, '🟫') # Restaurar la celda original
                    self.board.set_cell(new_row, new_col, '⚫')  # Mover al jugador negro
                self.black_pos = (new_row, new_col) # Actualizar la nueva posición
                return

            else:
                print("You can't move there")

    def white_blockade(self):
        while True:
            # Solicitar al usuario las coordenadas de fila y columna para bloquear una casilla
            row = int(input("Enter the row to lock: "))
            col = int(input("Enter the column to lock: "))
                
            if not self.board.valid_position(row, col):  # Verificar si la posición está fuera del rango válido
                print()
                print("Out of range position, try again")
                continue  # Continuar con el próximo intento si la posición es inválida

            if self.board.get_cell_value(row, col) == '🟨': # Verificar si la casilla seleccionada ya está bloqueada
                print()
                print("The cell is already locked, try again")
                continue  # Continuar con el próximo intento si la casilla ya está bloqueada

            if self.board.get_cell_value(row, col) == '⚫': # Verificar si la casilla seleccionada esta el jugador negro
                print()
                print("In the cell is the black player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            if self.board.get_cell_value(row, col) == '⚪': # Verificar si la casilla seleccionada esta el jugador blanco
                print()
                print("In the cell is the white player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            self.board.set_cell(row, col, '🟨') # Bloquear la casilla en el tablero
            print(f"White player locks the box in the row {row} y column {col}")
            break
    
    def black_blockade(self):
        while True:
            # Generar coordenadas aleatorias para bloquear una casilla
            row = random.randint(0, self.board.n - 1)
            col = random.randint(0, self.board.n - 1)
           
            if not self.board.valid_position(row, col): # Verificar si la posición está fuera del rango válido
                print()
                print("Out of range position, try again")
                continue  # Continuar con el próximo intento si la posición es inválida
                            
            if self.board.get_cell_value(row, col) == '🟨': # Verificar si la casilla seleccionada ya está bloqueada
                print()
                print("The cell is already locked, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente
                        
            if self.board.get_cell_value(row, col) == '⚪': # Verificar si la casilla seleccionada esta el jugador blanco
                print()
                print("In the cell is the white player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            if self.board.get_cell_value(row, col) == '⚫': # Verificar si la casilla seleccionada esta el jugador negro
                print()
                print("In the cell is the black player, try again")
                continue  # Si la casilla ya está bloqueada, intenta nuevamente

            self.board.set_cell(row, col, '🟨') # Bloquear la casilla en el tablero
            print(f"Black player locks the box in the row {row} y column {col}")
            break

    def winner(self):
        # Tupla (row, col)
        # En la primera coordenada (row) es las posiciones en la fila de los jugadores
        # En la egunda coordenada (col) el "_" es la forma de indicar que no vamos a utilizar esa parte de la tupla
        white_row, _ = self.white_pos
        black_row, _ = self.black_pos
        n = self.board.n

        if white_row == 0: # Si la fila es la 0
            print("¡The white's player is winner!")
            self.board.print_board()
            return "white"
        if black_row == n - 1: # Si la fila es la ultima del tablero
            print("¡The black's player is winner!")
            self.board.print_board()
            return "black"
        else:
            return None # Devuelve None si no hay un ganador en el turno actual
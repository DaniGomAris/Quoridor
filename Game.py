import random
from LinkedList import LinkedList

class Game:
    def __init__(self, board):
        # Empezar el juego con un tablero y las posiciones iniciales de los jugadores
        self.board = board
        self.white_pos = None
        self.black_pos = None


    def add_white(self):
        self.white_pos = self.board.white_initial_position() # Asigna la posición inicial del jugador blanco en el tablero


    def add_black(self):
        self.black_pos = self.board.black_initial_position() # Asigna la posición inicial del jugador negro en el tablero


    def add_obligatory_cell(self):
        row = self.board.n//2, self.board.n//2
        col = self.board.n//2, self.board.n//2


    def is_possible_to_win_verification(self, player_pos, win_row): # Bloquea temporalmente una casilla y se activa este metodo para verificar si se puede ganar al hacer el bloqueo
        print()
        self.board.print_board()
        row, col = player_pos # Obtener las coordenadas del jugador
        row_pass = self.board.n // 2
        col_pass = self.board.n // 2

        if row == win_row and self.board.get_cell_value(row_pass, col_pass) == '🟦':
            return True  # Retorna True si pudo llegar
        
        current_value = self.board.get_cell_value(row, col) # Celdas visitadas
        self.board.set_cell(row, col, '🟦') # Marcar la celda actual como visitada

        directions = LinkedList() # Se crea una lista enlazada para guardar las direcciones posibles: arriba, abajo, izquierda, derecha...
        directions.add_head((-1,0)) # Arriba
        directions.add_head((1,0)) # Abajo
        directions.add_head((0,-1)) # Izquierda
        directions.add_head((0,1)) # Derecha

        current = directions.head # Para recorrer la lista enlazada "directions"

        while current:
            change_row, change_col = current.value # Obtener los cambios en las coordenadas desde la direccion actual de la lista enlazada "directions"
            new_row, new_col = row + change_row, col + change_col # Calcular las nuevas coordenadas sumando los cambios a las coordenadas actuales de la lista enlazada "directions"

            # Verificar si se puede llegar a la fila objetivo
            if (self.board.valid_position(new_row, new_col) # Si pasa por las celdas validas
                and self.board.get_cell_value(new_row, new_col) != '🟦' # Si no pasa por las celdas visitadas
                and self.board.get_cell_value(new_row, new_col) != '🟨' # Si no pasa por los bloqueos
                and self.is_possible_to_win_verification((new_row, new_col), win_row)): # Llamado recursivo y para que se cumpla el IF tiene que haber retornado True

                self.board.set_cell(row, col, current_value) # Restaurar las celdas por las que paso
                return True # Retorna True si pudo llegar, aqui termina el metodo 'is_possible_to_win_verification'

            current = current.next # Pasar a la siguiente dirección en la lista enlazada

        self.board.set_cell(row, col, current_value) # Restaurar el valor original si no se encontro una solución
        return False # Si no es posible ganar devuelve False


    def is_possible_to_win(self):
        print("Intento de llegar a la linea de ganada para el blanco")
        white_win_possible = self.is_possible_to_win_verification(self.white_pos, 0) # Comprobar si es posible ganar para el jugador blanco
        print()
        print("Intento de llegar a la linea de ganada para el negro")
        black_win_possible = self.is_possible_to_win_verification(self.black_pos, self.board.n - 1) # Comprobar si es posible ganar para el jugador negro
        print()
        return white_win_possible and black_win_possible # Devolver True si es posible ganar para ambos jugadores, si no, devolver False


    def jump_two_spaces(self, row, col, direction, player_pos): # El player_pos, es donde se pone si lo esta usando el blanco o el negro
        # Después de saltar una vez, vuelve y salta por eso se le vuelve a sumar +1, si fuera +2 saltaría 3 espacios
        if direction == 1:  # Arriba
            row -= 1
        elif direction == 2:  # Abajo
            row += 1
        elif direction == 3:  # Izquierda
            col -= 1
        elif direction == 4:  # Derecha
            col += 1

        print()
        if not self.board.valid_position(row, col):  # Verifica si la nueva posición está fuera de los límites del tablero
            print("You can't move there, you leave the limits of the board")
            row, col = player_pos  # Si está fuera del rango, regresar a la posición original

        node_value = self.board.get_cell_value(row, col)  # Obtiene el valor de la celda en la nueva posición
        if node_value == '🟨':  # Si la celda a la que va a saltar es una celda bloqueada
            print("You can't move there, is a locked cell")
            row, col = player_pos  # Si está fuera del rango, regresar a la posición original

        if node_value == '🟩':  # Si la celda a la que va a saltar es una celda obligatoria
            print("You can't move there, is a obligatory cell ")
            row, col = player_pos  # Si está fuera del rango, regresar a la posición original

        if node_value == '⚪':  # Si la celda a la que va a saltar esta el jugador blanco
            print("You can't move there, is a white player")
            row, col = player_pos  # Si está fuera del rango, regresar a la posición original

        if node_value == '⚫':  # Si la celda a la que va a saltar esta el jugador negro
            print("You can't move there, is a black player")
            row, col = player_pos  # Si está fuera del rango, regresar a la posición original

        return row, col # Devuelve las cordenadas despues de saltar otra vez


    def white_move(self):
        direction = int(input(
"""
Directions
1. up
2. down
3. left
4. right
option: """))

        new_row, new_col = self.white_pos # Obtiene las coordenadas actuales del jugador blanco (fila y columna) en la forma (new_row, new_col)
        print()
        if direction == 1:  # Arriba
            new_row -= 1
        elif direction == 2:  # Abajo
            new_row += 1
        elif direction == 3:  # Izquierda
            new_col -= 1
        elif direction == 4:  # Derecha
            new_col += 1
        else:
            print('Invalid direction, try again')
            self.white_move()

        if self.board.valid_position(new_row, new_col): # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
            node_value = self.board.get_cell_value(new_row, new_col) # Obtiene el valor de la celda en la nueva posición

            if node_value == '🟨': # Si la celda a la que va a saltar es una celda bloqueada
                print("You can't move there, is a locked cell")
                return

            if node_value == '⚫': # Si la direccion a la que va a saltar esta el jugador negro
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, direction, self.white_pos) # El jugador blanco salta dos celdas si hay un jugador negro en la dirección
                self.board.set_cell(*self.white_pos, '🟫')  # Restaurar la celda original
                self.board.set_cell(jump_row, jump_col, '⚪')  # Mover al jugador blanco
                self.white_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                print("In this direction is the black player, you jump 2 cells")
                return

            if node_value == '🟩': # Si la direccion a la que va a saltar esta el la celda obligatoria
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, direction, self.white_pos) # El jugador blanco salta dos celdas si hay una celda obligatoria en la dirección
                self.board.set_cell(*self.white_pos, '🟫')  # Restaurar la celda original
                self.board.set_cell(jump_row, jump_col, '⚪')  # Mover al jugador blanco
                self.white_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                print("In this direction is the obligatory cell, you jump 2 cells")
                return

            else:
                self.board.set_cell(*self.white_pos, '🟫') # Restaurar la celda original
                self.board.set_cell(new_row, new_col, '⚪')  # Mover al jugador negro
            self.white_pos = (new_row, new_col) # Actualizar la nueva posición
            return

        else:
            print()
            print("You can't move there, is off the board")


    def black_move(self):
        random_direction = random.randint(1, 4) # El jugador negro se mueve aleatoriamente en una dirección valida
        new_row, new_col = self.black_pos # Obtiene las coordenadas actuales del jugador negro (fila, columna) en la forma (new_row, new_col)

        if random_direction == 1:  # Arriba
                new_row -= 1
        elif random_direction == 2:  # Abajo
                new_row += 1
        elif random_direction == 3:  # Izquierda
                new_col -= 1
        elif random_direction == 4:  # Derecha
                new_col += 1

        if self.board.valid_position(new_row, new_col): # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
            node_value = self.board.get_cell_value(new_row, new_col) # Obtiene el valor de la celda en la nueva posición

            if node_value == '🟨': # Si la celda a la que va a saltar es una celda bloqueada
                print("You can't move there, is a locked cell")
                return

            if node_value == '⚪': # Si en la direccion a la que va a saltar esta el jugador blanco
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, random_direction, self.black_pos) # El jugador negro salta dos celdas si hay un jugador blanco
                self.board.set_cell(*self.black_pos, '🟫')  # Restaurar la celda original
                self.board.set_cell(jump_row, jump_col, '⚫')  # Mover al jugador negro
                self.black_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                print("In this direction is the white player, you jump 2 cells")
                return

            if node_value == '🟩': # Si en la direccion a la que va a saltar esta la celda obligatoria
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, random_direction, self.black_pos) # El jugador negro salta dos celdas si hay una celda obligatoria
                self.board.set_cell(*self.black_pos, '🟫')  # Restaurar la celda original
                self.board.set_cell(jump_row, jump_col, '⚫')  # Mover al jugador negro
                self.black_pos = (jump_row, jump_col)  # Actualizar la nueva posición
                print("In this direction is the obligatory cell, you jump 2 cells")
                return

            else:
                self.board.set_cell(*self.black_pos, '🟫') # Restaurar la celda original
                self.board.set_cell(new_row, new_col, '⚫')  # Mover al jugador negro
            self.black_pos = (new_row, new_col) # Actualizar la nueva posición
            return

        else:
            print()
            print("You can't move there, is off the board")


    def white_blockade(self):
        print()
        # Solicitar al usuario las coordenadas de fila y columna para bloquear una casilla
        row = int(input("Enter the row to lock: "))
        col = int(input("Enter the column to lock: "))

        print()
        if not self.board.valid_position(row, col):  # Verificar si la posición está fuera del rango válido
            print("Cannot be blocked, out of range position")
            return

        if self.board.get_cell_value(row, col) == '🟨': # Verificar si la casilla seleccionada ya está bloqueada
            print("Cannot be blocked, the cell is already locked")
            return

        if self.board.get_cell_value(row, col) == '⚫': # Verificar si la casilla seleccionada esta el jugador negro
            print("Cannot be blocked, in the cell is the black player")
            return

        if self.board.get_cell_value(row, col) == '⚪': # Verificar si la casilla seleccionada esta el jugador blanco
            print("Cannot be blocked, in the cell is the white player")
            return

        if self.board.get_cell_value(row, col) == '🟩': # Verificar si la casilla seleccionada esta la casilla obligatoria
            print("Cannot be blocked, in the cell is the obligatory cell")
            return

        self.board.set_cell(row, col, '🟨') # Bloquear la casilla en el tablero

        if not self.is_possible_to_win(): # Se bloquea la casilla y se verifica si se puede ganar, si no se puede ganar sigue con el condicional
            print("Cannot be blocked, unable to win if that cell is locked")
            self.board.set_cell(row, col, '🟫')  # Se desbloquea la casilla
            return

        print(f"White player locks the cell in the row {row} y column {col}")


    def black_blockade(self):
        # Generar coordenadas aleatorias para bloquear una casilla
        row = random.randint(0, self.board.n - 1)
        col = random.randint(0, self.board.n - 1)

        if not self.board.valid_position(row, col): # Verificar si la posición está fuera del rango válido
            print("Cannot be blocked, out of range position")
            return

        if self.board.get_cell_value(row, col) == '🟨': # Verificar si la casilla seleccionada ya está bloqueada
            print("Cannot be blocked, the cell is already locked")
            return

        if self.board.get_cell_value(row, col) == '⚪': # Verificar si la casilla seleccionada esta el jugador blanco
            print("Cannot be blocked, in the cell is the white player")
            return

        if self.board.get_cell_value(row, col) == '⚫': # Verificar si la casilla seleccionada esta el jugador negro
            print("Cannot be blocked, in the cell is the black player")
            return

        if self.board.get_cell_value(row, col) == '🟩': # Verificar si la casilla seleccionada esta la casilla obligatoria
            print("Cannot be blocked, in the cell is the obligatory cell")
            return

        self.board.set_cell(row, col, '🟨') # Bloquear la casilla en el tablero

        if not self.is_possible_to_win(): # Se bloquea la casilla y se verifica si se puede ganar, si no se puede ganar sigue con el condicional

            print("Cannot be blocked, unable to win if that cell is locked")
            self.board.set_cell(row, col, '🟫')  # Se desbloquea la casilla
            return

        print(f"Black player locks the cell in the row {row} y column {col}")


    def winner(self):
        # Tupla (row, col)
        # En la primera coordenada (row) es las posiciones en la fila de los jugadores
        # En la segunda coordenada (col) el "_" es la forma de indicar que no vamos a utilizar esa parte de la tupla
        white_row, _ = self.white_pos
        black_row, _ = self.black_pos

        if white_row == 0: # Si la fila es la 0
            print()
            print("¡The white's player is winner!")
            print()
            self.board.print_board()
            return True

        if black_row == self.board.n - 1: # Si la fila es la ultima del tablero
            print()
            print("¡The black's player is winner!")
            print()
            self.board.print_board()
            return True
        else:
            return None # Devuelve None si no hay un ganador en el turno actual
import random
from LinkedList import LinkedList

class Game:
    def __init__(self, board):
        self.board = board
        self.white_pos = None
        self.black_pos = None


    def add_white(self):
        """
        Asignar la posición inicial del jugador blanco en el tablero
        """
        self.white_pos = self.board.white_initial_position()


    def add_black(self):
        """
        Asigna la posición inicial del jugador negro en el tablero
        """
        self.black_pos = self.board.black_initial_position()

 
    def add_obligatory_cell(self):
        row = self.board.n//2, self.board.n//2
        col = self.board.n//2, self.board.n//2


    def is_possible_to_win_verification(self, player_pos, win_row):
        """
        Bloquea temporalmente una casilla y se llama a este metodo para verificar si se puede ganar al hacer el bloqueo
        """
        print()
        self.board.print_board()
        row, col = player_pos
        row_pass = self.board.n // 2
        col_pass = self.board.n // 2

        if row == win_row and self.board.get_cell_value(row_pass, col_pass) == '🟦':
            return True
        
        current_value = self.board.get_cell_value(row, col)
        self.board.set_cell(row, col, '🟦') # Marcar la celda actual como visitada

        directions = LinkedList()
        directions.add_head((-1,0)) # Arriba
        directions.add_head((1,0)) # Abajo
        directions.add_head((0,-1)) # Izquierda
        directions.add_head((0,1)) # Derecha

        current = directions.head

        while current:
            change_row, change_col = current.value 
            new_row, new_col = row + change_row, col + change_col

            # Verificar si se puede llegar a la fila objetivo verificando,si: paso por las celdas validas, no paso por las celdas visitadas ni las bloqueadas y el metodo es True
            if (self.board.valid_position(new_row, new_col)
                and self.board.get_cell_value(new_row, new_col) != '🟦' 
                and self.board.get_cell_value(new_row, new_col) != '🟨' 
                and self.is_possible_to_win_verification((new_row, new_col), win_row)):

                self.board.set_cell(row, col, current_value) # Restaurar el valor original de las celdas por las que paso
                return True # Retorna True si pudo llegar, aqui termina el metodo 'is_possible_to_win_verification'

            current = current.next

        self.board.set_cell(row, col, current_value) # Restaurar el valor original por las que paso
        return False


    def is_possible_to_win(self):
        """
        Se utiliza para hacer el llamado por parte de los 2 jugadores al metodo "is_possible_to_win_verification"
        """
        print("Intento de llegar a la linea de ganada para el blanco")
        white_win_possible = self.is_possible_to_win_verification(self.white_pos, 0)
        print()
        print("Intento de llegar a la linea de ganada para el negro")
        black_win_possible = self.is_possible_to_win_verification(self.black_pos, self.board.n - 1)
        print()
        return white_win_possible and black_win_possible


    def jump_two_spaces(self, row, col, direction, player_pos):
        """
        Después de saltar una vez, vuelve y salta por eso se le vuelve a sumar +1
        """
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
            row, col = player_pos

        node_value = self.board.get_cell_value(row, col)
        
        # Si la celda a la que va a saltar es una celda bloqueada
        if node_value == '🟨':
            print("You can't move there, is a locked cell")
            row, col = player_pos

        # Si la celda a la que va a saltar es una celda obligatoria
        if node_value == '🟩':  
            print("You can't move there, is a obligatory cell ")
            row, col = player_pos

        # Si la celda a la que va a saltar esta el jugador blanco
        if node_value == '⚪':  
            print("You can't move there, is a white player")
            row, col = player_pos

        # Si la celda a la que va a saltar esta el jugador negro
        if node_value == '⚫':
            print("You can't move there, is a black player")
            row, col = player_pos

        return row, col


    def white_move(self):
        """
        Permite hacer los movimientos del jugador blanco a eleccion del usuario
        """
        direction = int(input(
"""
Directions
1. up
2. down
3. left
4. right
option: """))

        new_row, new_col = self.white_pos
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
            node_value = self.board.get_cell_value(new_row, new_col)

            # Si la celda a la que va a saltar es una celda bloqueada
            if node_value == '🟨': 
                print("You can't move there, is a locked cell")
                return

            # Si la direccion a la que va a saltar esta el jugador negro
            if node_value == '⚫': 
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, direction, self.white_pos)
                self.board.set_cell(*self.white_pos, '🟫')
                self.board.set_cell(jump_row, jump_col, '⚪')
                self.white_pos = (jump_row, jump_col)
                print("In this direction is the black player, you jump 2 cells")
                return

            # Si la direccion a la que va a saltar esta el la celda obligatoria
            if node_value == '🟩': 
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, direction, self.white_pos)
                self.board.set_cell(*self.white_pos, '🟫')
                self.board.set_cell(jump_row, jump_col, '⚪')
                self.white_pos = (jump_row, jump_col)
                print("In this direction is the obligatory cell, you jump 2 cells")
                return

            else:
                self.board.set_cell(*self.white_pos, '🟫')
                self.board.set_cell(new_row, new_col, '⚪')
            self.white_pos = (new_row, new_col)
            return

        else:
            print()
            print("You can't move there, is off the board")


    def black_move(self):
        """
        Permite hacer los movimientos del jugador negro aleatoriamente
        """
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

        # Verifica si la nueva posición (new_row, new_col) está dentro de los límites del tablero
        if self.board.valid_position(new_row, new_col): 
            node_value = self.board.get_cell_value(new_row, new_col) 

            # Si la celda a la que va a saltar es una celda bloqueada
            if node_value == '🟨': # Si la celda a la que va a saltar es una celda bloqueada
                print("You can't move there, is a locked cell")
                return

            # Si en la direccion a la que va a saltar esta el jugador blanco
            if node_value == '⚪': 
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, random_direction, self.black_pos)
                self.board.set_cell(*self.black_pos, '🟫')
                self.board.set_cell(jump_row, jump_col, '⚫')
                self.black_pos = (jump_row, jump_col)
                print("In this direction is the white player, you jump 2 cells")
                return

            # Si en la direccion a la que va a saltar esta la celda obligatoria
            if node_value == '🟩': 
                jump_row, jump_col = self.jump_two_spaces(new_row, new_col, random_direction, self.black_pos)
                self.board.set_cell(jump_row, jump_col, '⚫')
                self.black_pos = (jump_row, jump_col)
                print("In this direction is the obligatory cell, you jump 2 cells")
                return

            else:
                self.board.set_cell(*self.black_pos, '🟫')
                self.board.set_cell(new_row, new_col, '⚫')
            self.black_pos = (new_row, new_col)
            return

        else:
            print()
            print("You can't move there, is off the board")


    def white_blockade(self):
        """
        Permite hacer los bloqueos del jugador blanco a eleccion del jugador
        """
        print()
        row = int(input("Enter the row to lock: "))
        col = int(input("Enter the column to lock: "))

        print()
        # Verificar si la posición está fuera del rango válido
        if not self.board.valid_position(row, col):
            print("Cannot be blocked, out of range position")
            return

        # Verificar si la casilla seleccionada ya está bloqueada
        if self.board.get_cell_value(row, col) == '🟨': 
            print("Cannot be blocked, the cell is already locked")
            return  
        
        # Verificar si la casilla seleccionada esta el jugador negro
        if self.board.get_cell_value(row, col) == '⚫': 
            print("Cannot be blocked, in the cell is the black player")
            return

        # Verificar si la casilla seleccionada esta el jugador blanco
        if self.board.get_cell_value(row, col) == '⚪': 
            print("Cannot be blocked, in the cell is the white player")
            return

        # Verificar si la casilla seleccionada esta la casilla obligatoria
        if self.board.get_cell_value(row, col) == '🟩': 
            print("Cannot be blocked, in the cell is the obligatory cell")
            return

        self.board.set_cell(row, col, '🟨')

        # Se bloquea la casilla y se verifica si se puede ganar, si no se puede ganar sigue con el condicional
        if not self.is_possible_to_win(): 
            print("Cannot be blocked, unable to win if that cell is locked")
            self.board.set_cell(row, col, '🟫')
            return

        print(f"White player locks the cell in the row {row} y column {col}")


    def black_blockade(self):
        """
        Permite hacer los bloqueos del jugador negro aleatoriamente
        """
        row = random.randint(0, self.board.n - 1)
        col = random.randint(0, self.board.n - 1)

        # Verificar si la posición está fuera del rango válido
        if not self.board.valid_position(row, col): 
            print("Cannot be blocked, out of range position")
            return

        # Verificar si la casilla seleccionada ya está bloqueada
        if self.board.get_cell_value(row, col) == '🟨': 
            print("Cannot be blocked, the cell is already locked")
            return  

        # Verificar si la casilla seleccionada esta el jugador blanco
        if self.board.get_cell_value(row, col) == '⚪': 
            print("Cannot be blocked, in the cell is the white player")
            return  

        # Verificar si la casilla seleccionada esta el jugador negro
        if self.board.get_cell_value(row, col) == '⚫': 
            print("Cannot be blocked, in the cell is the black player")
            return

        # Verificar si la casilla seleccionada esta la casilla obligatoria
        if self.board.get_cell_value(row, col) == '🟩': 
            print("Cannot be blocked, in the cell is the obligatory cell")
            return

        self.board.set_cell(row, col, '🟨')

        if not self.is_possible_to_win():
            print("Cannot be blocked, unable to win if that cell is locked")
            self.board.set_cell(row, col, '🟫')
            return

        print(f"Black player locks the cell in the row {row} y column {col}")


    def winner(self):
        """
         Tupla (row, col)
         En la primera coordenada (row) es las posiciones en la fila de los jugadores
         En la segunda coordenada (col) el "_" es la forma de indicar que no vamos a utilizar esa parte de la tupla
        """ 
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
            return None
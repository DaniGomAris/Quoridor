from LinkedList import LinkedList
import random

class Board:
    def __init__(self, n: int):
        self.n: int = n # Tamaño de tabñero
        self.board = self.create_board() # Creacion del tablero

    def create_board(self):
        board = LinkedList()  # Crea una lista enlazada 'board' para representar el tablero

        for i in range(self.n): # Itera a traves de las filas del tablero
            row = LinkedList()  # Crea una lista enlazada 'row' para representar una fila del tablero

            for j in range(self.n): # Itera a traves de las columnas del tablero
                row.add_head(None)  # Agrega un elemento None al inicio de la fila 'row'
            board.add_head(row) # Agrega la fila 'row' al inicio del tablero 'board'

        return board # Tablero 'board' creado
    
    def print_board(self):
        print()
        for row in range(self.n): # Itera a traves de las filas del tablero
            row_str = ''  # Inicializa un str para almacenar la fila actual

            for col in range(self.n): # Itera a traves de las columnas del tablero, agrega el emoji 🟫 a 'row_str'
                row_str += '🟫 ' # Agrega el emoji 🟫 a 'row_str'
            print(row_str) # Imprime la fila actual del tablero

    def black_initial_position(self):
        cells = [(0, col) for col in range(self.n)] # Recorre las columnas de la primera fila del tablero y las agrega a la lista 'cells'

        if cells:
            row, col = random.choice(cells) # Elegir aleatoriamente una columna de la lista 'cells'
            self.set_cell(row, col, '⚫') # Establecer la celda en la primera fila y columna aleatoria como '⚫'
            return row, col # Devolver las coordenadas (fila y columna) de la celda donde se coloco la ficha negra

    def white_initial_position(self):
        row = self.n - 1  # Determinar que la fila donde aparecera la ficha blanca es la ultima

        while True:
            col = int(input('Ingrese columna para aparecer: ')) - 1 # Solicitar al usuario que ingrese la columna donde aparecerá la ficha blanca

            if self.valid_position(row, col): # Verificar si la posición ingresada es valida
                self.set_cell(row, col, '⚪') # Establecer la celda en la ultima fila y columna seleccionada como '⚪'
                return row, col # Devolver las coordenadas (fila y columna) de la celda donde se coloco la ficha blanca
            else:
                print('Posición invalida, intente de nuevo')

    def valid_position(self, row, col) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n # Verificar si las coordenadas (fila y columna) estan dentro de los limites del tamaño del tablero

    def set_cell(self, row, col, value):
        curr_row = self.board.head # Se inicializa 'curr_row' como la primera fila del tablero

        for _ in range(row): # Avanzar hasta la fila especificada
            curr_row = curr_row.next # Pasar a la siguiente fila 

        curr_node = curr_row.value.head # Obtener el valor del nodo actual de la fila
        for _ in range(col): # Avanzar hasta la columna especificada
            curr_node = curr_node.next # Pasar a la siguiente columna

        curr_node.value = value # Establecer el valor de la celda en la fila y columna especificadas.

    def get_cell_value(self, row, col):
        curr_row = self.board.head # Se inicializa la variable 'curr_row' para que apunte a la primera fila del tablero

        for _ in range(row): # Avanzar hasta la fila especificada (row)
            curr_row = curr_row.next # Pasar a la siguiente fila

        curr_node = curr_row.value.head # Obtener el nodo actual de la fila (celda)
        for _ in range(col): # Avanzar hasta la columna especificada (col)
            curr_node = curr_node.next # Pasar a la siguiente columna

        return curr_node.value # Retornar el valor de la celda en la fila y columna especificadas
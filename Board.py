from LinkedList import LinkedList

class Board:
    def __init__(self, n: int):
        self.n: int = n # Tamaño de tabñero
        self.board = self.create_board() # Creacion del tablero

    def create_board(self):
        board = LinkedList() # Crea una lista enlazada 'board' para representar el tablero

        for i in range(self.n): # Itera a traves de las filas del tablero
            row = LinkedList()  # Crea una lista enlazada 'row' para representar una fila del tablero
            for j in range(self.n): # Itera a traves de las columnas del tablero
                row.add_head(None)  # Agrega un elemento None al inicio de la fila 'row'
            board.add_head(row) # Agrega la fila 'row' al inicio del tablero 'board'
        return board # Tablero 'board' creado

    def print_board(self):
        curr_row = self.board.head # Itera a través de las filas de la matriz enlazada
        while curr_row: # Itera a través de los nodos de cada fila
            curr_node = curr_row.value.head
            row_str = ''
            while curr_node: 
                row_str += curr_node.value # Concatena el valor de cada nodo a la cadena de la fila
                curr_node = curr_node.next # Pasa al siguiente nodo
            print(row_str)# Imprime la fila completa
            curr_row = curr_row.next # Pasa a la siguiente fila

    def add_symbol(self):
        symbol_table = ['🟫'] * (self.n * self.n) # Crea una lista de símbolos ('🟫') para todas las celdas del tablero

        curr_row = self.board.head # Itera a traves de las filas de la matriz enlazada
        while curr_row: # Itera a través de los nodos de cada fila
            curr_node = curr_row.value.head 
            while curr_node: # Itera a través de los nodos de cada fila
                if symbol_table and curr_node.value is None: # Asigna un símbolo de la tabla a cada celda vacía en el tablero
                    curr_node.value = symbol_table.pop() # Quita un elemento de la lista de el simbolo del tablero y lo asigna al nodo
                curr_node = curr_node.next # Pasa al siguiente nodo
            curr_row = curr_row.next # Pasa a la siguiente fila

    def black_initial_position(self) -> (int,int):
        row = 0 # Primera fila
        col = (self.n // 2) # Mitad de la ultima fila

        if self.valid_position(row, col): # Verificar si la posición ingresada es valida
            self.set_cell(row, col, '⚫') # Establecer la celda en la primera fila y columna aleatoria como '⚫'
            return row, col # Devolver las coordenadas (fila y columna) de la celda donde se coloco la ficha negra

    def white_initial_position(self) -> (int,int):
        row = self.n - 1  # Determinar que la fila donde aparecera la ficha blanca es la ultima
        col = (self.n // 2) # Mitad de la ultima fila

        if self.valid_position(row, col): # Verificar si la posición ingresada es valida
            self.set_cell(row, col, '⚪') # Establecer la celda en la ultima fila y columna seleccionada como '⚪'
            return row, col # Devolver las coordenadas (fila y columna) de la celda donde se coloco la ficha blanca
    
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
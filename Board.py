from LinkedList import LinkedList
import random

class Board:
    def __init__(self, n: int):
        self.n: int = n
        self.board = self.create_board()


    def create_board(self, board = None, current_row: int = 0) -> LinkedList:
        if board is None: # Si no existe tablero, se crea una instancia de la clase LinkedList()
            board = LinkedList()
        if current_row == self.n: # Si ya se alcanzo el numero de filas retorna el tablero creado
            return board
        row = LinkedList()
        for columns in range(self.n): # Crea "self.n" comunas en la fila
            row.add_head(None)  
        board.add_head(row)

        return self.create_board(board, current_row + 1)


    def print_board(self):
        curr_row = self.board.head
        while curr_row: # Itera a traves de cada fila
            curr_node = curr_row.value.head
            row_str = ''
            while curr_node: # Itera a traves de los nodos de cada fila
                row_str += curr_node.value
                curr_node = curr_node.next
            print(row_str)
            curr_row = curr_row.next


    def add_symbol(self):
        symbol_table = '🟫'
        curr_row = self.board.head

        while curr_row: # Itera a través de las filas del tablero
            curr_node = curr_row.value.head 
            while curr_node: # Itera a través de los nodos de cada fila
                if curr_node.value is None: # Si el valor de nodo actual es None se añade el "symbol_table"
                    curr_node.value = symbol_table
                curr_node = curr_node.next
            curr_row = curr_row.next


    def black_initial_position(self) -> (int,int):
        row = 0
        col = random.randint(0, self.n - 1) 

        self.set_cell(row, col, '⚫')
        return row, col # Devolver las coordenadas (fila y columna) de la celda donde se coloco la ficha negra


    def white_initial_position(self) -> (int,int):
        row = self.n - 1
        col = random.randint(0, self.n - 1)

        self.set_cell(row, col, '⚪')
        return row, col # Devolver las coordenadas (fila y columna) de la celda donde se coloco la ficha blanca
        
    
    def valid_position(self, row, col) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n
    

    def set_cell(self, row, col, value):
        curr_row = self.board.head

        for row in range(row): # Avanzar hasta la fila especificada
            curr_row = curr_row.next

        curr_node = curr_row.value.head
        for col in range(col): # Avanzar hasta la columna especificada
            curr_node = curr_node.next

        curr_node.value = value # Establece el valor del nodo actual por el valor requerido


    def get_cell_value(self, row, col):
        curr_row = self.board.head

        for row in range(row):
            curr_row = curr_row.next # Pasar a la siguiente fila

        curr_node = curr_row.value.head
        for col in range(col): # Avanzar hasta la columna especificada
            curr_node = curr_node.next

        return curr_node.value
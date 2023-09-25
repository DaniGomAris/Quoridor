from LinkedList import LinkedList
import random

class Board:
    def __init__(self, n):
        self.n: int = n
        self.board = self.create_board()

    def print_board(self):
        for row in range(self.n):
            row_str = ''
            for col in range(self.n):
                if (row + col) % 2 == 0:
                    row_str += '🟨'
                else:
                    row_str += '🟫'
            print(row_str)

    def create_board(self):
        board = LinkedList()
        for i in range(self.n):
            row = LinkedList()
            for j in range(self.n):
                row.add_head(None)
            board.add_head(row)
        return board

    def black_initial_position(self):
        cells = [(0, col) for col in range(self.n)]

        if cells:
            row, col = random.choice(cells)
            self.set_cell(row, col, '⚫')
            return row, col

    def white_initial_position(self):
        row = self.n - 1
        while True:
            col = int(input('Ingrese columna para aparecer: ')) - 1
            if self.valid_position(row, col):
                self.set_cell(row, col, '⚪')
                return row, col
            else:
                print('Posición inválida. Intente de nuevo.')

    def valid_position(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.n

    def set_cell(self, row, col, value):
        curr_row = self.board.head
        for _ in range(row):
            curr_row = curr_row.next

        curr_node = curr_row.value.head
        for _ in range(col):
            curr_node = curr_node.next

        curr_node.value = value

    def get_cell_value(self, row, col):
        curr_row = self.board.head
        for _ in range(row):
            curr_row = curr_row.next

        curr_node = curr_row.value.head
        for _ in range(col):
            curr_node = curr_node.next

board1 = Board(5)
board1.print_board()
print('⚫')
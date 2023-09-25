from LinkedList import LinkedList
import random

class Board:
    def __init__(self, n):
        self.n: int = n
        self.board = self.create_board()

    def print_board(self):
        print()
        curr_row = self.board.head
        while curr_row:
            curr_node = curr_row.value.head
            row_str = ''
            while curr_node:
                row_str += f"| {curr_node.value} |"
                curr_node = curr_node.next
                if curr_node == None:
                  row_str += f""
            print(row_str)
            curr_row = curr_row.next
        print()

    def create_board(self):
        board = LinkedList()
        for i in range(self.n):
            row = LinkedList()
            for j in range(self.n):
                row.add_head(None)
            board.add_head(row)
        return board

    def black_initial_position(self):
        empty_cells = []
        curr_row = self.board.head
        row_index = 0

        while curr_row:
            curr_node = curr_row.value.head
            col_index = 0

            while curr_node:
                if curr_node.value == ' ':
                    empty_cells.append((row_index, col_index))
                elif curr_node.value == '#':
                    break
                col_index += 1
                curr_node = curr_node.next
            row_index += 1
            curr_row = curr_row.next

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.set_cell(row, col, '\U0001F916')
            return row, col

    def white_initial_position(self):
        while True:
            row = int(input('Fila: ')) - 1
            col = int(input('Columna: ')) - 1
            if self.invalid_cell():
                print("HOLAAAAAAAAAAAAAAAAAAAAAAAAA")
            if self.valid_position(row, col):
                self.set_cell(row, col, '\U0001F47D')
                return row, col
            else:
                print('Posición inválida. Intente de nuevo.')

    def valid_position(self, row, col) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n

    def invalid_cell(self):
        curr_row = self.board.head
        curr_node = curr_row.value.head
        if curr_node == '#':
          print("HOLAAAAAAAAAAAAAAAAAAAAAAAAA")

    def set_cell(self, row, col, value):
        curr_row = self.board.head
        for _ in range(row):
            curr_row = curr_row.next

        curr_node = curr_row.value.head
        for _ in range(col):
            curr_node = curr_node.next

        curr_node.value = value

    def get_cell_value(self, row, col) -> str:
        curr_row = self.board.head
        for _ in range(row):
            curr_row = curr_row.next

        curr_node = curr_row.value.head
        for _ in range(col):
            curr_node = curr_node.next

board1 = Board(5)
board1.print_board()
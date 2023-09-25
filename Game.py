from Board import Board

class Game:
    def __init__(self):
        self.board = None
        self.white_pos = None
        self.black_pos = None

    def add_white(self):
        self.white_pos = self.board.white_initial_position()

    def add_black(self):
        self.black_pos = self.board.black_initial_position()

    def white_move(self):
        while True:
            direction = input(
"""
Direcciones 
1.arriba 
2.abajo 
3.izquierda 
4.derecha
opcion: """)
            new_row, new_col = self.white_pos

            #Arriba
            if direction == '1':
                new_row -= 1
            #Abajo
            elif direction == '2':
                new_row += 1
            #Izquierda
            elif direction == '3':
                new_col -= 1
            #Derecha
            elif direction == '4':
                new_col += 1
                print('Dirección inválida. Intente de nuevo.')
                continue

            if self.board.valid_position(new_row, new_col):

                Node_value = self.board.get_cell_value(new_row, new_col)

                #Si cae en una casilla "+"
                if Node_value == '+':
                    self.alien_life += 10
                    self.board.Put_cell_value(new_row, new_col, 'daw')
                    print("--------------------JUGADA DEL ALIEN--------------------")
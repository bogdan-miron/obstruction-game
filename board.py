from texttable import Texttable


class BoardExceptions(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class OutOfBoundsException(BoardExceptions):
    def __init__(self):
        super().__init__("Choice is out bounds")


class AlreadyHitException(BoardExceptions):
    def __init__(self):
        super().__init__("Cannot place choice there")


class GameOverException(Exception):
    pass


class Board:
    def __init__(self, size=8):
        self.__size = size
        self._board = [[' ' for _ in range(self.__size)] for _ in range(self.__size)]

    @property
    def size(self):
        return self.__size

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new_value):
        self._board = new_value

    def inside_matrix(self, x: int, y: int) -> bool:
        return 0 <= x < self.__size and 0 <= y < self.__size

    def place_O(self, x: int, y: int):
        displacement_x = [0, 0, -1, 1, -1, -1, 1, 1]
        displacement_y = [-1, 1, 0, 0, -1, 1, -1, 1]

        if self.inside_matrix(x, y) and self._board[x][y] == ' ':
            self._board[x][y] = 'O'
            for i in range(8):
                new_x = x + displacement_x[i]
                new_y = y + displacement_y[i]
                if self.inside_matrix(new_x, new_y):
                    self._board[new_x][new_y] = 'E'
        elif not self.inside_matrix(x, y):
            raise OutOfBoundsException()
        else:
            raise AlreadyHitException()

    def place_X(self, x: int, y: int):
        displacement_x = [0, 0, -1, 1, -1, -1, 1, 1]
        displacement_y = [-1, 1, 0, 0, -1, 1, -1, 1]

        if self.inside_matrix(x, y) and self._board[x][y] == ' ':
            self._board[x][y] = 'X'
            for i in range(8):
                new_x = x + displacement_x[i]
                new_y = y + displacement_y[i]
                if self.inside_matrix(new_x, new_y):
                    self._board[new_x][new_y] = 'E'
        elif not self.inside_matrix(x, y):
            raise OutOfBoundsException()
        else:
            raise AlreadyHitException()

    def is_board_won(self):
        contains_space = any(' ' in row for row in self._board)
        return not contains_space

    # def __str__(self):
    #     table = Texttable()
    #     header = [' '] + [str(i) for i in range(self.size)]
    #     table.header(header)
    #     for i in range(self.size):
    #         row = [str(i)] + self._board[i]
    #         table.add_row(row)
    #     return table.draw()

    def __str__(self):
        color_codes = {
            'O': '\033[34m',  # blue
            'X': '\033[31m',  # red
            'E': '\033[37m',  # white
        }
        reset_code = '\033[0m'  # reset color
        output = "   " + " ".join([str(i) for i in range(self.size)]) + "\n"
        for i in range(self.size):
            row = [
                f"{color_codes.get(cell, '')}{cell}{reset_code}"
                for cell in self._board[i]
            ]
            output += f"{i}  " + " ".join(row) + "\n"
        return output


if __name__ == '__main__':
    board = Board()
    board.place_O(2, 2)
    board.place_X(4, 4)
    board.place_X(1, 4)
    board.place_O(4, 1)
    board.place_O(1, 0)
    board.place_X(0, 2)
    print(board)
    print(board.is_board_won())

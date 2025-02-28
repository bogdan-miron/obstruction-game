from board import *


class ComputerOpponent:
    def __init__(self, board: Board):
        self.__curr_board = board

    def __find_best_move(self) -> tuple:
        best_x = -1
        best_y = -1
        best_result = -1
        for i in range(self.__curr_board.size):
            for j in range(self.__curr_board.size):
                if self.__curr_board.board[i][j] == ' ':
                    partial_result = 0
                    # count the number of empty spaces around - ' ' characters
                    displacement_x = [0, 0, -1, 1, -1, -1, 1, 1]
                    displacement_y = [-1, 1, 0, 0, -1, 1, -1, 1]

                    for d in range(8):
                        new_x = i + displacement_x[d]
                        new_y = j + displacement_y[d]
                        if self.__curr_board.inside_matrix(new_x, new_y) and self.__curr_board.board[new_x][new_y] == ' ':
                            partial_result = partial_result + 1

                    if partial_result > best_result:
                        best_result = partial_result
                        best_x = i
                        best_y = j

        return best_x, best_y

    def play_best_move(self):
        row, column = self.__find_best_move()
        self.__curr_board.place_X(row, column)


if __name__ == '__main__':
    board = Board()
    board.place_O(2, 2)
    board.place_X(4, 4)
    board.place_X(1, 4)
    opponent = ComputerOpponent(board)
    print(board)
    opponent.play_best_move()
    print('bogdan bogdan')
    print(board)
    opponent.play_best_move()
    print(board)
    print('hheehe')
    opponent.play_best_move()
    print(board)
    opponent.play_best_move()
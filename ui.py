from board import *
from opponent import *
import pyfiglet

class UI:
    def __init__(self):
        self.__board = Board()
        self.__opponent = ComputerOpponent(self.__board)

    def __print_hello_message(self, msg: str):
        ascii_art = pyfiglet.figlet_format(msg)
        print(ascii_art)

    def __place_player_input(self):
        print('Place your option: ')
        try:
            row = int(input('Row = '))
            col = int(input('Column = '))
            self.__board.place_O(row, col)
        except Exception as e:
            print(e)
            self.__place_player_input()


    def start_game(self):
        self.__print_hello_message('Bogdan Occupation Game')
        print('Current board: ')
        print(self.__board)
        while True:
            self.__place_player_input()
            print('You have played: ')
            print(self.__board)
            if self.__board.is_board_won():
                self.__print_hello_message('You have won')
                break
            self.__opponent.play_best_move()
            print('The computer has responded: ')
            print(self.__board)
            if self.__board.is_board_won():
                self.__print_hello_message('The computer has won dummy')
                break



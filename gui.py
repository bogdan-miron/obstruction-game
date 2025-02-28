import tkinter as tk
from tkinter import messagebox
from board import *
from opponent import *
import pyfiglet


class ObstructionGameGUI:
    def __init__(self, root):
        self.__board = Board()
        self.__opponent = ComputerOpponent(self.__board)
        self.root = root
        self.root.title("Obstruction Game")
        self.create_gui()

    def create_gui(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.board_size = self.__board.size  # Get board size from the Board class
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col] = tk.Button(
                    self.board_frame,
                    text="",
                    width=4,
                    height=2,
                    command=lambda r=row, c=col: self.player_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

        self.message_label = tk.Label(self.root, text="Welcome to Obstruction!", font=("Helvetica", 14))
        self.message_label.pack(pady=10)

    def update_message(self, message):
        self.message_label.config(text=message)
        ascii_art = pyfiglet.figlet_format(message)
        print(ascii_art)

    def player_move(self, row, col):
        try:
            if self.__board.board[row][col] == " ":
                self.__board.place_O(row, col)
                self.update_board()
                if self.check_win("Player"):
                    return
                self.computer_move()
        except OutOfBoundsException:
            messagebox.showerror("Invalid Move", "Choice is out of bounds.")
        except AlreadyHitException:
            messagebox.showerror("Invalid Move", "Cannot place choice there.")

    def computer_move(self):
        try:
            self.__opponent.play_best_move()
            self.update_board()
            self.check_win("Computer")
        except GameOverException:
            self.update_message("The Player has won!")
            self.disable_buttons()

    def update_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell = self.__board.board[row][col]
                if cell == "O":
                    self.buttons[row][col].config(text="O", state="disabled", disabledforeground="blue")
                elif cell == "X":
                    self.buttons[row][col].config(text="X", state="disabled", disabledforeground="red")
                elif cell == "E":
                    self.buttons[row][col].config(state="disabled")

    def check_win(self, last_player):
        if not any(" " in row for row in self.__board.board):
            winner = "Computer" if last_player == "Computer" else "Player"
            self.update_message(f"{winner} has won!")
            self.disable_buttons()
            return True
        return False

    def disable_buttons(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(state="disabled")


def main():
    root = tk.Tk()
    game = ObstructionGameGUI(root)
    game.update_message("Bogdan Occupation Game")
    root.mainloop()


if __name__ == "__main__":
    main()

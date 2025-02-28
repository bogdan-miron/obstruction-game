from ui import *
from gui import *

def main():

    # start the game in console here
    # ui = UI()
    # ui.start_game()

    root = tk.Tk()
    game = ObstructionGameGUI(root)
    game.update_message("Bogdan Occupation Game")
    root.mainloop()


if __name__ == '__main__':
    main()
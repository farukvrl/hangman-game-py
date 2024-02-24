import tkinter as tk
from hangman.ui import HangmanUI

def main():
    root = tk.Tk()
    ui = HangmanUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

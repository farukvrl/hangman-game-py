# Benutzeroberfläche des Hangman-Spiels

import tkinter as tk
from tkinter import ttk
from .hangman import HangmanGame

class HangmanUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.game = HangmanGame()

        self.create_widgets()

    def create_widgets(self):
        self.hangmanWordLabel = tk.Label(self.root, text=self.game.get_display_word(), font=("Helvetica", 16))
        self.hangmanWordLabel.pack(pady=10)

        self.hangmanLifesLabel = tk.Label(self.root, text="♥ " * self.game.remainingLifes, font=("Helvetica", 16))
        self.hangmanLifesLabel.pack(pady=5)

        self.alphabetFrame = ttk.Frame(self.root)
        self.alphabetFrame.pack(pady=10)

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖ"
        num_letters = len(alphabet)
        num_columns = 9
        num_rows = -(-num_letters // num_columns)  # Ceiling division

        self.alphabetButtons = {}

        for i, char in enumerate(alphabet):
            row = i // num_columns
            col = i % num_columns
            button = ttk.Button(self.alphabetFrame, text=char, command=lambda c=char: self.on_letter_clicked(c))
            button.grid(row=row, column=col, padx=2, pady=2)
            self.alphabetButtons[char] = button

        self.hintButton = ttk.Button(self.root, text="Hinweis", command=self.on_hint_clicked)
        self.hintButton.pack(pady=5)

        self.gameMessageLabel = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.gameMessageLabel.pack()

    def on_letter_clicked(self, letter):
        if letter not in self.game.guessedLetters:
            if self.game.check_letter(letter):
                self.hangmanWordLabel.config(text=self.game.get_display_word())
            else:
                self.hangmanLifesLabel.config(text="♥ " * self.game.remainingLifes)
                self.alphabetButtons[letter].config(state="disabled")
            self.check_game_status()

    def on_hint_clicked(self):
        if self.game.reveal_hint():
            self.hangmanWordLabel.config(text=self.game.get_display_word())
        else:
            self.hangmanLifesLabel.config(text="♥ " * self.game.remainingLifes)
            self.check_game_status()

    def check_game_status(self):
        if self.game.is_game_over():
            if "_" not in self.game.get_display_word():
                self.hangmanWordLabel.config(text=self.game.selectedWord)
            self.display_message("Spiel vorbei!", "danger")
            self.reset_game()

    def reset_game(self):
        for button in self.alphabetButtons.values():
            button.config(state="enabled")
        self.game = HangmanGame()
        self.hangmanWordLabel.config(text=self.game.get_display_word())
        self.hangmanLifesLabel.config(text="♥ " * self.game.remainingLifes)
        self.gameMessageLabel.config(text="")

    def display_message(self, message, type="info"):
        self.gameMessageLabel.config(text=message)
        if type == "danger":
            self.gameMessageLabel.config(fg="red")
        else:
            self.gameMessageLabel.config(fg="black")

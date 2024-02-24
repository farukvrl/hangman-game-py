import random
from .words import words

class HangmanGame:
    def __init__(self):
        self.selectedWord = random.choice(words)
        self.remainingLifes = 5
        self.guessedLetters = []

    def check_letter(self, letter):
        if letter in self.selectedWord:
            self.guessedLetters.append(letter)
            return True
        else:
            self.remainingLifes -= 1
            return False

    def reveal_hint(self):
        hidden_letters = [char for char in self.selectedWord if char not in self.guessedLetters]
        if hidden_letters:
            self.guessedLetters.append(hidden_letters[0])
            return True
        else:
            self.remainingLifes -= 1
            return False

    def get_display_word(self):
        display_word = ""
        for letter in self.selectedWord:
            if letter in self.guessedLetters:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word.strip()

    def is_game_over(self):
        return "_" not in self.get_display_word() or self.remainingLifes == 0

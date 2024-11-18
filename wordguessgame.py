import tkinter as tk
from tkinter import messagebox
import random

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        
        # List of words
        self.word_list = ['python', 'java', 'kotlin', 'javascript']
        self.secret_word = random.choice(self.word_list)
        self.guesses_left = 7
        self.guessed_word = ['_'] * len(self.secret_word)
        self.guessed_letters = []
        
        # Setting up the GUI components
        self.setup_gui()

    def setup_gui(self):
        # Display the word with underscores
        self.word_label = tk.Label(self.root, text=' '.join(self.guessed_word), font=('Arial', 24))
        self.word_label.pack(pady=20)
        
        # Entry for the user's guess
        self.entry = tk.Entry(self.root, font=('Arial', 14))
        self.entry.pack(pady=10)
        
        # Submit button
        self.submit_button = tk.Button(self.root, text='Submit Guess', command=self.check_guess)
        self.submit_button.pack(pady=10)
        
        # Guesses left label
        self.guesses_left_label = tk.Label(self.root, text=f'Guesses Left: {self.guesses_left}', font=('Arial', 14))
        self.guesses_left_label.pack(pady=10)
        
        # Restart button
        self.restart_button = tk.Button(self.root, text='Restart Game', command=self.new_game)
        self.restart_button.pack(pady=10)

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if not guess or guess in self.guessed_letters:
            messagebox.showinfo("Invalid Guess", "You have already guessed that letter or provided an empty input.")
            return

        self.guessed_letters.append(guess)
        if guess in self.secret_word:
            for index, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.guessed_word[index] = guess
        else:
            self.guesses_left -= 1

        self.word_label.config(text=' '.join(self.guessed_word))
        self.guesses_left_label.config(text=f'Guesses Left: {self.guesses_left}')
        
        if '_' not in self.guessed_word:
            messagebox.showinfo("Congratulations", "You guessed the word!")
            self.new_game()
        elif self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"The word was: {self.secret_word}")
            self.new_game()

    def new_game(self):
        self.secret_word = random.choice(self.word_list)
        self.guesses_left = 7
        self.guessed_word = ['_'] * len(self.secret_word)
        self.guessed_letters = []
        
        self.word_label.config(text=' '.join(self.guessed_word))
        self.guesses_left_label.config(text=f'Guesses Left: {self.guesses_left}')

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()


import tkinter as tk
from tkinter import messagebox
import random

# List of words for the Hangman game
words = ["python", "hangman", "algorithm", "coding", "developer"]

# Function to start a new game
def new_game():
    global word, guessed_letters, mistakes, correct_guesses
    word = random.choice(words)
    guessed_letters = []
    mistakes = 0
    correct_guesses = ["_"] * len(word)
    update_display()

# Function to update the display
def update_display():
    display_word = " ".join(correct_guesses)
    word_label.config(text=display_word)
    guesses_label.config(text=f"Guessed Letters: {' '.join(guessed_letters)}")
    attempts_label.config(text=f"Mistakes: {mistakes}/6")

# Function to handle guesses
def guess_letter():
    global mistakes
    letter = entry.get().lower()
    entry.delete(0, tk.END)
    
    if not letter or len(letter) > 1 or not letter.isalpha():
        messagebox.showwarning("Invalid input", "Please enter a single letter.")
        return
    
    if letter in guessed_letters:
        messagebox.showinfo("Already guessed", "You have already guessed that letter.")
        return
    
    guessed_letters.append(letter)
    
    if letter in word:
        for index, char in enumerate(word):
            if char == letter:
                correct_guesses[index] = letter
    else:
        mistakes += 1
    
    update_display()
    
    if "_" not in correct_guesses:
        messagebox.showinfo("Congratulations!", "You won!")
        new_game()
    elif mistakes >= 6:
        messagebox.showinfo("Game Over", f"You lost! The word was '{word}'.")
        new_game()

# Set up the main window
root = tk.Tk()
root.title("Hangman Game")

# Word display
word_label = tk.Label(root, text="_ _ _ _ _", font=("Helvetica", 24))
word_label.pack(pady=20)

# Entry for guessing letters
entry = tk.Entry(root, font=("Helvetica", 18))
entry.pack(pady=10)
entry.focus()

# Guess button
guess_button = tk.Button(root, text="Guess", font=("Helvetica", 18), command=guess_letter)
guess_button.pack(pady=10)

# Display for guessed letters and mistakes
guesses_label = tk.Label(root, text="Guessed Letters: ", font=("Helvetica", 14))
guesses_label.pack(pady=10)
attempts_label = tk.Label(root, text="Mistakes: 0/6", font=("Helvetica", 14))
attempts_label.pack(pady=10)

# Start a new game
new_game()

# Run the GUI main loop
root.mainloop()

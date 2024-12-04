import tkinter as tk
from tkinter import simpledialog, messagebox
import random

# Sample data for users and questions
users = {}
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 1
    },
    {
        "question": "Which programming language is used for AI?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": 2
    }
]

# Function to register a new user
def register():
    username = simpledialog.askstring("Register", "Enter a username:")
    if username in users:
        messagebox.showwarning("Register", "Username already exists. Try a different one.")
        return
    while True:
        password = simpledialog.askstring("Register", "Enter a numeric password (digits only):", show='*')
        if password.isdigit():
            users[username] = password
            messagebox.showinfo("Register", "Registration successful!")
            break
        else:
            messagebox.showwarning("Register", "Password must contain digits only. Try again.")

# Function to log in an existing user
def login():
    username = simpledialog.askstring("Login", "Enter your username:")
    if username not in users:
        messagebox.showwarning("Login", "User not found. Please register first.")
        return None
    while True:
        password = simpledialog.askstring("Login", "Enter your numeric password:", show='*')
        if users[username] == password:
            messagebox.showinfo("Login", "Login successful!")
            return username
        else:
            messagebox.showwarning("Login", "Incorrect password. Try again.")

# Function to conduct the test
def take_test():
    score = 0
    for i, q in enumerate(questions, start=1):
        answer = simpledialog.askinteger(f"Question {i}", f"{q['question']}\nOptions:\n" + "\n".join([f"{j+1}. {opt}" for j, opt in enumerate(q['options'])]))
        if answer is not None and answer - 1 == q['answer']:
            score += 1
    messagebox.showinfo("Test Completed", f"Your score: {score}/{len(questions)}")

# Main program loop with GUI
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    while True:
        choice = simpledialog.askinteger("Online Test System", "1. Register\n2. Login\n3. Exit\nEnter your choice:")
        if choice == 1:
            register()
        elif choice == 2:
            username = login()
            if username:
                take_test()
        elif choice == 3:
            messagebox.showinfo("Exit", "Exiting the system. Goodbye!")
            break
        else:
            messagebox.showwarning("Invalid Choice", "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
# Initialize the board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=3,
                                      command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row, column=col)

def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

root.mainloop()

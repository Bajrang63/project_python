import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)

        self.width = 500
        self.height = 500
        self.cell_size = 20

        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.snake_dir = "Right"
        self.food = self.place_food()
        self.running = True

        self.draw_snake()
        self.draw_food()
        
        self.root.bind("<KeyPress>", self.change_direction)
        self.update_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="green", tag="snake")

    def draw_food(self):
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="red", tag="food")

    def place_food(self):
        while True:
            x = random.randint(0, int(self.width / self.cell_size) - 1) * self.cell_size
            y = random.randint(0, int(self.height / self.cell_size) - 1) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        new_direction = event.keysym
        if (new_direction == "Up" and self.snake_dir != "Down") or \
           (new_direction == "Down" and self.snake_dir != "Up") or \
           (new_direction == "Left" and self.snake_dir != "Right") or \
           (new_direction == "Right" and self.snake_dir != "Left"):
            self.snake_dir = new_direction

    def update_snake(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]
        if self.snake_dir == "Right":
            head_x += self.cell_size
        elif self.snake_dir == "Left":
            head_x -= self.cell_size
        elif self.snake_dir == "Up":
            head_y -= self.cell_size
        elif self.snake_dir == "Down":
            head_y += self.cell_size

        new_head = (head_x, head_y)
        
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height or new_head in self.snake:
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.place_food()
            self.draw_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.root.after(100, self.update_snake)

    def game_over(self):
        self.running = False
        self.canvas.create_text(self.width / 2, self.height / 2, text="GAME OVER", fill="white", font=("Helvetica", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

import tkinter as tk
import time
from math import cos, sin, radians

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.center_x = 200
        self.center_y = 200
        self.radius = 100

        self.update_clock()

    def draw_hand(self, length, angle, width, color):
        x_end = self.center_x + length * cos(radians(angle))
        y_end = self.center_y - length * sin(radians(angle))
        self.canvas.create_line(self.center_x, self.center_y, x_end, y_end, width=width, fill=color)

    def update_clock(self):
        self.canvas.delete("all")

        # Draw the clock face
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius, self.center_x + self.radius, self.center_y + self.radius)

        # Get the current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate the angles for the hands
        sec_angle = 6 * seconds
        min_angle = 6 * minutes + seconds / 10
        hour_angle = 30 * hours + minutes / 2

        # Draw the clock hands
        self.draw_hand(self.radius * 0.9, hour_angle, 4, "black")
        self.draw_hand(self.radius * 0.9, min_angle, 2, "blue")
        self.draw_hand(self.radius * 0.9, sec_angle, 1, "red")

        # Redraw the clock every second
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()

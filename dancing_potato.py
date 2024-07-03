import tkinter as tk
from tkinter import messagebox
import random

class DancingPotatoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dancing Potato - Spudly")
        self.root.geometry("400x400")

        self.canvas = tk.Canvas(root, width=400, height=300, bg='lightblue')
        self.canvas.pack()

        self.potato_image = tk.PhotoImage(file="potato.png")  # Make sure you have a potato.png file
        self.potato = self.canvas.create_image(200, 150, image=self.potato_image)

        self.health = 100
        self.happiness = 100

        self.health_label = tk.Label(root, text=f"Health: {self.health}")
        self.health_label.pack()

        self.happiness_label = tk.Label(root, text=f"Happiness: {self.happiness}")
        self.happiness_label.pack()

        self.dance_button = tk.Button(root, text="Dance!", command=self.dance)
        self.dance_button.pack()

        self.feed_button = tk.Button(root, text="Feed", command=self.feed)
        self.feed_button.pack()

        self.check_status_button = tk.Button(root, text="Check Status", command=self.check_status)
        self.check_status_button.pack()

        self.update_status()

    def dance(self):
        moves = [(-10, 0), (10, 0), (0, -10), (0, 10)]
        for _ in range(10):
            move = random.choice(moves)
            self.canvas.move(self.potato, move[0], move[1])
            self.root.update()
            self.root.after(100)
        self.happiness += 10
        self.update_status()

    def feed(self):
        self.health += 10
        self.update_status()

    def check_status(self):
        status = f"Health: {self.health}\nHappiness: {self.happiness}"
        messagebox.showinfo("Spudly's Status", status)

    def update_status(self):
        self.health_label.config(text=f"Health: {self.health}")
        self.happiness_label.config(text=f"Happiness: {self.happiness}")

if __name__ == "__main__":
    root = tk.Tk()
    game = DancingPotatoGame(root)
    root.mainloop()

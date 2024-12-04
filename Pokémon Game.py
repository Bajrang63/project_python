import tkinter as tk
from tkinter import messagebox

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.xp = 0

    def train(self):
        self.xp += 10

# Function to update the display
def update_display():
    pokemon_name_label.config(text=f"Pokémon: {selected_pokemon.name}")
    xp_label.config(text=f"XP: {selected_pokemon.xp}")

# Function to handle training
def train_pokemon():
    selected_pokemon.train()
    update_display()
    if selected_pokemon.xp >= 100:
        messagebox.showinfo("Congratulations!", f"{selected_pokemon.name} has reached 100 XP!")

# Function to select a Pokémon
def select_pokemon(pokemon):
    global selected_pokemon
    selected_pokemon = pokemon
    update_display()

# Set up the main window
root = tk.Tk()
root.title("Pokémon Training Game")

# Create Pokémon instances
pikachu = Pokemon("Pikachu")
charmander = Pokemon("Charmander")
bulbasaur = Pokemon("Bulbasaur")

# Select the initial Pokémon
selected_pokemon = pikachu

# Display Pokémon name
pokemon_name_label = tk.Label(root, text=f"Pokémon: {selected_pokemon.name}", font=("Helvetica", 18))
pokemon_name_label.pack(pady=10)

# Display XP
xp_label = tk.Label(root, text=f"XP: {selected_pokemon.xp}", font=("Helvetica", 18))
xp_label.pack(pady=10)

# Button to train Pokémon
train_button = tk.Button(root, text="Train Pokémon", font=("Helvetica", 18), command=train_pokemon)
train_button.pack(pady=10)

# Buttons to select different Pokémon
select_pikachu_button = tk.Button(root, text="Select Pikachu", font=("Helvetica", 14), command=lambda: select_pokemon(pikachu))
select_pikachu_button.pack(pady=5)

select_charmander_button = tk.Button(root, text="Select Charmander", font=("Helvetica", 14), command=lambda: select_pokemon(charmander))
select_charmander_button.pack(pady=5)

select_bulbasaur_button = tk.Button(root, text="Select Bulbasaur", font=("Helvetica", 14), command=lambda: select_pokemon(bulbasaur))
select_bulbasaur_button.pack(pady=5)

# Run the GUI main loop
root.mainloop()

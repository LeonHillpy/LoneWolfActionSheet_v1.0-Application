
from tkinter import *  # Main Tkinter module.
import customtkinter as ctk  # type: ignore # Module for modernising Tkinter.
from PIL import Image, ImageTk  # Modules for image processing.
from random import randrange

def dice_roll(self):
    dice = randrange(10)
    self.dice_roll_button.configure(text=str(dice))

def combat(self, player_endurance_value, player_combat_value):
    # Create a new window using CTkToplevel for the combat system.
    self.combat_window = ctk.CTkToplevel(self)

    # Set the title and geometry for the new window and set resizable to False.
    self.combat_window.title("Lone Wolf Combat System")
    self.combat_window.geometry("1200x720")
    self.combat_window.resizable(False, False)

    # Set window priority
    self.combat_window.grab_set()  # Prevent interaction with other windows
    self.combat_window.attributes('-topmost', True)  # Keep it on top

    # Handle window closing
    def on_close():
        # Update the main app's endurance entry with the current value
        self.endurance.delete(0, END)  # Clear the old value
        self.endurance.insert(0, player_endurance.get())  # Insert the new value
        self.combat_window.grab_release()  # Release the grab when closing
        self.combat_window.destroy()  # Destroy the window
    self.combat_window.protocol("WM_DELETE_WINDOW", on_close)  # Override the close button

    # Player Endurance (health)
    player_endurance_label = ctk.CTkLabel(self.combat_window, text="Player Endurance:")
    player_endurance_label.place(x=250, y=10)
    player_endurance = ctk.CTkEntry(self.combat_window, width=100, text_color='lightgreen')
    player_endurance.place(x=360, y=10)
    player_endurance.insert(0, player_endurance_value)  # Pre-fill with current endurance

    # Player Combat Score
    player_combat_label = ctk.CTkLabel(self.combat_window, text="Player Combat Score:")
    player_combat_label.place(x=10, y=10)
    player_combat = ctk.CTkEntry(self.combat_window, width=100, text_color='lightgreen')
    player_combat.place(x=140, y=10)
    player_combat.insert(0, player_combat_value)  # Pre-fill with current combat score

    # Enemy Endurance (health)
    enemy_endurance_label = ctk.CTkLabel(self.combat_window, text="Enemy Endurance:")
    enemy_endurance_label.place(x=250, y=50)
    enemy_endurance = ctk.CTkEntry(self.combat_window, width=100, text_color='red')
    enemy_endurance.place(x=360, y=50)

    # Enemy Combat Score
    enemy_combat_label = ctk.CTkLabel(self.combat_window, text="Enemy Combat Score:")
    enemy_combat_label.place(x=10, y=50)
    enemy_combat = ctk.CTkEntry(self.combat_window, width=100, text_color='red')
    enemy_combat.place(x=140, y=50)

    # Battle ratio
    battle_ratio_label = ctk.CTkLabel(self.combat_window, text="Battle Ratio:")
    battle_ratio_label.place(x=470, y=50)
    battle_ratio = ctk.CTkEntry(self.combat_window, width=100)
    battle_ratio.place(x=550, y=50)

    # Add an error message label to display errors
    error_label = ctk.CTkLabel(self.combat_window, text="", text_color="red", font=("Helvetica", 12))
    error_label.place(x=850, y=60)  # Position it below the combat score entries

    def generate_battle_ratio():
    # Clear previous error messages
        error_label.configure(text="")  # Clear the error label
        
        # Check if enemy combat score entry is empty
        enemy_combat_value = enemy_combat.get()
        if not enemy_combat_value:  # If the entry is empty
            error_label.configure(text="Enemy Combat Score cannot be empty.", text_color="red")
            return  # Exit the function if there's no data

        # Continue with the calculation if the input is valid
        try:
            player_combat_number = int(player_combat.get())
            enemy_combat_number = int(enemy_combat_value)
            battle_ratio_amount = player_combat_number - enemy_combat_number
            battle_ratio.delete(0, END)
            battle_ratio.insert(0, str(battle_ratio_amount))
        except ValueError:
            error_label.configure(text="Please enter valid numbers for combat scores.", text_color="red")
    
    battle_ratio_generator = ctk.CTkButton(self.combat_window, text="Generate Battle Ratio", command=generate_battle_ratio)
    battle_ratio_generator.place(x=530, y=15)

    # Dice Roll button
    self.dice_roll_button = ctk.CTkButton(self.combat_window, 
                                          height=70, text="Roll Dice", font=("Helvetica", 26), 
                                          command=lambda: dice_roll(self))
    self.dice_roll_button.place(x=700, y=10)

    # Display the combat matrix
    combatimage = Image.open("images/combatresults.jpg")
    combatimage_ctk = ctk.CTkImage(combatimage, size=(1160, 600))
    combat_results_label = ctk.CTkLabel(self.combat_window, text="", image=combatimage_ctk)
    combat_results_label.place(x=10, y=100)

    # Exit button
    exit = ctk.CTkButton(self.combat_window, text="Exit Combat", width=110, fg_color='red', hover_color="darkred",
                                        command=on_close)
    exit.place(x=1080, y=10)

from tkinter import * # Main Tkinter module.
from tkinter import messagebox
import customtkinter as ctk # Module for modernising Tkinter.
import csv # Handling csv files
import os
from datetime import datetime #Module for date and time
    
def save(self):  # Function for saving sheet to csv.
    try:
        # Read the values from the widgets
        book = self.book_name.get()
        disciplines = [entry.get() for entry in self.disciplineEntries]
        backpack = [entry.get() for entry in self.backpackEntries]
        special = [entry.get() for entry in self.specialEntries]
        weapon1 = self.weaponOne.get()
        weapon2 = self.weaponTwo.get()
        belt_pouch = self.beltPouch.get()
        meals = self.meals.get()
        deaths = self.deaths.get()
        endurance = self.endurance.get()
        combat = self.combat_score.get()
        og_endurance = self.original_endurance.get()
        og_combat = self.original_combat.get()

        # Generate filename with current date and time
        current_time = datetime.now().strftime("%d-%m-%y_%H-%M-%S")  # e.g., "2024-11-26_14-30-15"
        folder_path = "SavedSheets"  # Replace with your desired folder
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
        filename = os.path.join(folder_path, f"{current_time}.csv")  # Full path to the file

        # Create name-value pairs for each data entry
        rows = [
            f"book: {book}",
            f"weapon1: {weapon1}",
            f"weapon2: {weapon2}",
            f"belt_pouch: {belt_pouch}",
            f"meals: {meals}",
            f"deaths: {deaths}",
            f"endurance: {endurance}",
            f"combat: {combat}",
            f"original_endurance: {og_endurance}",
            f"original_combat: {og_combat}",
        ]

        # Append disciplines, backpack, and special data with their indices
        rows.extend([f"discipline_{i+1}: {value}" for i, value in enumerate(disciplines)])
        rows.extend([f"backpack_{i+1}: {value}" for i, value in enumerate(backpack)])
        rows.extend([f"special_{i+1}: {value}" for i, value in enumerate(special)])

        # Save to CSV
        with open(filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in rows:
                csv_writer.writerow([row])  # Each variable is written on a new line

        # Show success message
        messagebox.showinfo("Save Successful", f"Sheet saved successfully to {filename}")

    except Exception as e:
        # Show error message
        messagebox.showerror("Save Failed", f"An error occurred while saving the sheet: {e}")
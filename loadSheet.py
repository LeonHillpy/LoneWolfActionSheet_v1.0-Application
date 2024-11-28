
import csv
from tkinter import messagebox
import os
from imageLogic import display_image

def load(self):  # Function to load the latest CSV file into the app fields.
    try:
        # Get the folder containing the saved sheets
        folder_path = "SavedSheets"
        
        # Get the list of all files in the folder
        files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
        if not files:
            messagebox.showerror("Error", "No saved files found in the folder.")
            return
        
        # Find the most recently saved file (based on filename timestamp)
        files.sort()  # Assumes filenames are sorted by timestamp (your format ensures this)
        latest_file = os.path.join(folder_path, files[-1])  # Get the latest file
        
        # Load the content from the latest file
        with open(latest_file, mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
            if not rows:
                messagebox.showerror("Error", "The latest file is empty.")
                return

            # Parse the data into a dictionary
            data = {}
            for row in rows:
                if len(row) > 0:  # Ensure the row is not empty
                    key, value = row[0].split(": ", 1)  # Split into name and value
                    data[key] = value.strip()  # Trim whitespace

            # Set the ComboBox value (book name)
            self.book_name.set(data.get("book", ""))  # Set the selected book from the CSV

            # Manually trigger the image update after setting the ComboBox value
            display_image(self, data.get("book", ""))  # This will load and display the image for the selected book

            # Helper function to handle setting values and restoring placeholder
            def set_value(entry, value, placeholder_text):
                entry.delete(0, "end")
                if value:
                    entry.insert(0, value)  # Insert actual data
                else:
                    entry.insert(0, "")  # Leave blank if no data
                    entry.placeholder_text = placeholder_text  # Reset placeholder if empty

            # Update weapon fields
            set_value(self.weaponOne, data.get("weapon1", ""), "Weapon 1")
            set_value(self.weaponTwo, data.get("weapon2", ""), "Weapon 2")
            set_value(self.beltPouch, data.get("belt_pouch", ""), "Belt Pouch")
            set_value(self.meals, data.get("meals", ""), "Meals")
            set_value(self.deaths, data.get("deaths", ""), "Deaths")
            set_value(self.endurance, data.get("endurance", ""), "Endurance")
            set_value(self.combat_score, data.get("combat", ""), "Combat")
            set_value(self.original_endurance, data.get("original_endurance", ""), "Original Endurance")
            set_value(self.original_combat, data.get("original_combat", ""), "Original Combat")

            # Set disciplines
            for i, entry in enumerate(self.disciplineEntries):
                key = f"discipline_{i + 1}"
                set_value(entry, data.get(key, ""), f"Discipline {i + 1}")

            # Set backpack items
            for i, entry in enumerate(self.backpackEntries):
                key = f"backpack_{i + 1}"
                set_value(entry, data.get(key, ""), f"Backpack Item {i + 1}")

            # Set special items
            for i, entry in enumerate(self.specialEntries):
                key = f"special_{i + 1}"
                set_value(entry, data.get(key, ""), f"Special Item {i + 1}")

            messagebox.showinfo("Success", f"File '{files[-1]}' loaded successfully.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The specified folder or file does not exist.")
    except IndexError:
        messagebox.showerror("Error", "The file format is incorrect.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
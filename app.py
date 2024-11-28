
from tkinter import * # Main Tkinter module.
import customtkinter as ctk # type: ignore # Module for modernising Tkinter.
from imageLogic import display_image # Display_image function
from saveSheet import save # Save sheet function
from loadSheet import load # Load sheet function
from combat import combat # Combat function

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Main Class
class App(ctk.CTk):
    def __init__(self):
        super().__init__() # Initiates vairiables from parent class in ctk.

        # Sets the title of the interface and the size.
        self.title("Lone Wolf Character Sheet v1.1")
        self.geometry("870x730")

        # Load, save sheet
        self.load_sheet = ctk.CTkButton(self, text="Load Sheet", command=lambda: load(self)).place(x=10, y=10)
        self.save_sheet = ctk.CTkButton(self, text="Save Sheet", command=lambda: save(self)).place(x=160, y=10)

        # Death counter
        self.deaths_label = ctk.CTkLabel(self, text="Deaths:").place(x=310, y=10)
        self.deaths = ctk.CTkEntry(self, width=70, text_color="red")
        self.deaths.place(x=360, y=10)

        # Endurance
        self.endurance_label = ctk.CTkLabel(self, text="Endurance:").place(x=440, y=10)
        self.endurance = ctk.CTkEntry(self, width=80, text_color="lightgreen")
        self.endurance.place(x=510, y=10)

        # Origin Endurance
        self.original_endurance_label = ctk.CTkLabel(self, text="Max\nEndurance:").place(x=435, y=45)
        self.original_endurance = ctk.CTkEntry(self, width=80)
        self.original_endurance.place(x=510, y=50)

        # Combat Score
        self.combat_score_label = ctk.CTkLabel(self, text="Combat Score:").place(x=600, y=10)
        self.combat_score = ctk.CTkEntry(self, width=80)
        self.combat_score.place(x=690, y=10)

        # Origin Combat Score
        self.original_combat_label = ctk.CTkLabel(self, text="Max\nCombat:").place(x=630, y=45)
        self.original_combat = ctk.CTkEntry(self, width=80)
        self.original_combat.place(x=690, y=50)

        # Exit button
        self.exit_button = ctk.CTkButton(self, text="Exit", width=85, fg_color='red', hover_color="darkred",
                                          command=self.destroy).place(x=780, y=10)

        # Label to display the book cover
        self.book_image_label = ctk.CTkLabel(self, text="")
        self.book_image_label.place(x=430, y=90)

        # Sheet info
        self.books = [
            'Choose Book', 
            'Kai 1 - Flight from the Dark', 
            'Kai 2 - Fire on the Water',
            'Kai 3 - The Caverns of Kalte',
            'Kai 4 - The Chasm of Doom',
            'Kai 5 - Shadow on the Sand',
            'Magnakai 1 - The Kingdoms of Terror',
            'Magnakai 2 - Castle Death',
            'Magnakai 3 - The Jungle of Horrors',
            'Magnakai 4 - The Cauldron of Fear',
            'Magnakai 5 - The Dungeons of Torgar',
            'Magnakai 6 - Prisoners of Time',
            'Magnakai 7 - The Masters of Darkness',
            'Grand Master 1 - The Plague Lords of Reul',
            'Grand Master 2 - The Captives of Kaag',
            'Grand Master 3 - The Dark Crusade',
            'Grand Master 4 - The Legacy of Vashna',
            'Grand Master 5 - The Deathlord of Ixia',
            'Grand Master 6 - Dawn of the Dragons',
            "Grand Master 7 - Wolf's Bane",
            'Grand Master 8 - The Curse of Naar']

        self.book_name = ctk.CTkComboBox(self, width=200, values=self.books, 
                                         command=lambda selected_book: display_image(self, selected_book))
        self.book_name.place(x=10, y=50)

        # Combat
        self.openCombat = ctk.CTkButton(self, text="Open Combat", width=200, height=50, 
                                        command=lambda: combat(self, self.endurance.get(), self.combat_score.get())).place(x=215, y=50)

        # Kai Disciplines
        self.disciplinesLabel = ctk.CTkLabel(self, text="Disciplines:").place(x=10, y=80)
        self.disciplineEntries = []
        positions = [(10, 110), (10, 140), (10, 170), (10, 200), (10, 230), 
                     (215, 110), (215, 140), (215, 170), (215, 200), (215, 230)]
        # Create the Disciplines widgets dynamically
        for i, (x, y) in enumerate(positions):
            entry = ctk.CTkEntry(self, width=200)
            entry.place(x=x, y=y)
            self.disciplineEntries.append(entry)
        
        # Weapons
        self.weaponsLabel = ctk.CTkLabel(self, text="Weapons:").place(x=10, y=260)
        self.weaponOne = ctk.CTkEntry(self, width=200)
        self.weaponOne.place(x=10, y=290)
        self.weaponTwo = ctk.CTkEntry(self, width=200)
        self.weaponTwo.place(x=10, y=320)

        # Create the "Belt Pouch" label in gold
        self.belt_pouch_label = ctk.CTkLabel(self, text="Belt Pouch", text_color="gold")
        self.belt_pouch_label.place(x=215, y=260)
        self.beltPouch = ctk.CTkEntry(self, width=200, text_color="gold")
        self.beltPouch.place(x=215, y=290)

        # Create the "and Meals:" label with default text color
        self.meals_label = ctk.CTkLabel(self, text=" and Meals:")
        self.meals_label.place(x=275, y=260)
        self.meals = ctk.CTkEntry(self, width=200)
        self.meals.place(x=215, y=320)

        # Backpack
        self.backpackLabel = ctk.CTkLabel(self, text="Backpack:").place(x=10, y=350)
        self.backpackEntries = []
        backpackPositions = [(10, 380), (10, 410), (10, 440), (10, 470), 
                     (215, 380), (215, 410), (215, 440), (215, 470)]
        # Create the Backpack widgets dynamically
        for i, (x, y) in enumerate(backpackPositions):
            entry = ctk.CTkEntry(self, width=200)
            entry.place(x=x, y=y)
            self.backpackEntries.append(entry)

        # Special Items
        self.specialItemsLabel = ctk.CTkLabel(self, text="Special Items:").place(x=10, y=500)
        self.specialEntries = []
        specialPositions = [(10, 530), (10, 560), (10, 590), (10, 620), (10, 650), (10, 680),
                     (215, 530), (215, 560), (215, 590), (215, 620), (215, 650), (215, 680)]
        # Create the Backpack widgets dynamically
        for i, (x, y) in enumerate(specialPositions):
            entry = ctk.CTkEntry(self, width=200)
            entry.place(x=x, y=y)
            self.specialEntries.append(entry)

if __name__ == "__main__":
    app = App()
    app.resizable(False, False)
    app.mainloop() #Run the app
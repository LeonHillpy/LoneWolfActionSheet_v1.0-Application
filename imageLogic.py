
from tkinter import * # Main Tkinter module.
import customtkinter as ctk # Module for modernising Tkinter.
from PIL import Image # Module for image processing.
import os

def display_image(app_instance, selected_book):
        # Map book titles to filenames
        book_to_image = {
            'Kai 1 - Flight from the Dark': 'Kai1.jpg',
            'Kai 2 - Fire on the Water': 'Kai2.jpg',
            'Kai 3 - The Caverns of Kalte': 'Kai3.jpg',
            'Kai 4 - The Chasm of Doom': 'Kai4.jpg',
            'Kai 5 - Shadow on the Sand': 'Kai5.jpg',
            'Magnakai 1 - The Kingdoms of Terror': 'M-kai1.jpg',
            'Magnakai 2 - Castle Death': 'M-kai2.jpg',
            'Magnakai 3 - The Jungle of Horrors': 'M-kai3.jpg',
            'Magnakai 4 - The Cauldron of Fear': 'M-kai4.jpg',
            'Magnakai 5 - The Dungeons of Torgar': 'M-kai5.jpg',
            'Magnakai 6 - Prisoners of Time': 'M-kai6.jpg',
            'Magnakai 7 - The Masters of Darkness': 'M-kai7.jpg',
            'Grand Master 1 - The Plague Lords of Reul': 'GM-kai1.jpg',
            'Grand Master 2 - The Captives of Kaag': 'GM-kai2.jpg',
            'Grand Master 3 - The Dark Crusade': 'GM-kai3.jpg',
            'Grand Master 4 - The Legacy of Vashna': 'GM-kai4.jpg',
            'Grand Master 5 - The Deathlord of Ixia': 'GM-kai5.jpg',
            'Grand Master 6 - Dawn of the Dragons': 'GM-kai6.jpg',
            "Grand Master 7 - Wolf's Bane": 'GM-kai7.jpg',
            'Grand Master 8 - The Curse of Naar': 'GM-kai8.jpg',
            }
        
        if selected_book in book_to_image:
            image_path = os.path.join("images/BookCovers", book_to_image[selected_book])
            if os.path.exists(image_path):

                # Load and display the image
                img = ctk.CTkImage(
                    light_image=Image.open(image_path), 
                    dark_image=Image.open(image_path), 
                    size=(430, 630)
                )
                app_instance.book_image_label.configure(image=img)
                app_instance.book_image_label.image = img  # Keep a reference to prevent garbage collection
            else:
                print(f"Image not found: {image_path}")
        else:
            # Clear the image if "Choose Book" or invalid selection
            app_instance.book_image_label.configure(image=None)

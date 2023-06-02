import argparse
import os
import shutil
import tkinter as tk
from tkinter import filedialog
import glob
from PIL import ImageTk, Image

# Function to display images
def display_images(in_dir, out_dir):
    # Get the path to the image directory
    directory = in_dir

    # Get a list of image file names in the directory
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Display Images")

    # Create a label widget for displaying images
    image_label = tk.Label(window)

    # Function to update the image label
    def update_image_label(index, rot):
        # Load the image
        image_path = os.path.join(directory, image_files[index])
        image = Image.open(image_path)

        if rot == True:
            image = image.resize((1280, 900))
            image = image.rotate(90)
        else:      
            image = image.resize((1280, 900))

        # Create an ImageTk object
        image_tk = ImageTk.PhotoImage(image)

        # Update the label with the new image
        image_label.config(image=image_tk)
        image_label.image = image_tk  # Keep a reference to prevent image from being garbage collected

    # Initial image index
    current_image_index = 0

    # Function to handle button click
    def button_click_next():
        nonlocal current_image_index
        current_image_index = (current_image_index + 1) 
        update_image_label(current_image_index, rot=False)

    def button_click_prev():
        nonlocal current_image_index
        current_image_index = (current_image_index - 1) 
        update_image_label(current_image_index, rot=False)

    def button_click_save():
        nonlocal current_image_index
        # current_image_index = (current_image_index) % len(image_files)
        src_path = os.path.join(directory, image_files[current_image_index])
        dst_path = os.path.join(out_dir)
        os.makedirs(dst_path, exist_ok=True)
        shutil.copy2(src_path, dst_path)

    def button_click_rot():
        nonlocal current_image_index
        update_image_label(current_image_index, rot=True)
        file_name = image_files[current_image_index].split('.')
        name = [file_name[0], 'rotated', file_name[1]]
        file_name = '.'.join(name)

        dst_path = os.path.join(out_dir)

        # Operation
        rot = Image.open(image_files[current_image_index])
        rot = rot.rotate(90)
        rot.save(file_name)


    # Create a button widget
    button_next = tk.Button(window, text="Next", command=button_click_next)
    button_prev = tk.Button(window, text="Previous", command=button_click_prev)
    button_save = tk.Button(window, text="Save", command=button_click_save)
    button_rot = tk.Button(window, text="Rotate", command=button_click_rot)


    # Pack the button widget in the window
    button_next.pack()
    button_prev.pack()
    button_save.pack()
    button_rot.pack()

    # Pack the image label widget in the window
    image_label.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Call the display_images function

# select the in_and_out folders

window_ = tk.Tk()
infilepath = filedialog.askdirectory()
outfilepath = filedialog.askdirectory()
window_.mainloop()
# window_.destroy()

display_images(infilepath, outfilepath)    

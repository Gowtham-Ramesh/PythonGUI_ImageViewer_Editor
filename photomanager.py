import argparse
import os
import shutil
import tkinter as tk
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
    def update_image_label(index):
        # Load the image
        image_path = os.path.join(directory, image_files[index])
        image = Image.open(image_path)

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
        update_image_label(current_image_index)
        current_image_index = (current_image_index + 1) % len(image_files)

    def button_click_prev():
        nonlocal current_image_index
        update_image_label(current_image_index)
        current_image_index = (current_image_index - 1) % len(image_files)

    def button_click_save():
        nonlocal current_image_index
        current_image_index = (current_image_index) % len(image_files)
        src_path = os.path.join(directory, image_files[current_image_index])
        dst_path = os.path.join(out_dir)
        os.makedirs(dst_path, exist_ok=True)
        shutil.copy2(src_path, dst_path)

    # Create a button widget
    button_next = tk.Button(window, text="Next", command=button_click_next)
    button_prev = tk.Button(window, text="Previous", command=button_click_prev)
    button_save = tk.Button(window, text="save", command=button_click_save)

    # Pack the button widget in the window
    button_next.pack()
    button_prev.pack()
    button_save.pack()

    # Pack the image label widget in the window
    image_label.pack()

    # Start the Tkinter event loop
    window.mainloop()

# Call the display_images function

# Create the argument parser
parser = argparse.ArgumentParser(description='Example Argument Parser')

# Add arguments
parser.add_argument('-i', '--indir', help='Input file path')
parser.add_argument('-o', '--outdir', help='Input file path')


# Parse the command-line arguments
args = parser.parse_args()

# Access the argument values

display_images(args.indir, args.outdir)

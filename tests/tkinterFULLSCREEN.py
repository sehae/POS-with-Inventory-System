import os
import tkinter as tk
from tkinter import PhotoImage

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)

# Create the main window
root = tk.Tk()

# Configure the window to be full screen
root.attributes('-fullscreen', True)

# Function to create a frame with a given color
def create_colored_frame(parent, color):
    frame = tk.Frame(parent, bg=color, width=300, height=400)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    return frame

# Create frames with different colors
frame1 = create_colored_frame(root, 'white')
frame2 = create_colored_frame(root, 'white')
frame3 = create_colored_frame(root, 'white')

# Bind 'Escape' key to exit fullscreen
root.bind('<Escape>', exit_fullscreen)

# Load an image
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, '..', 'assets', 'logo1.png')

original_image = PhotoImage(file=image_path)

# Resize the image (adjust the factors as needed)
smaller_image = original_image.subsample(3, 3)  # Subsample by a factor of 3 in both dimensions

# Create a label to display the resized image in the green frame
image_label = tk.Label(frame2, image=smaller_image)
image_label.pack(expand=True)

# Start the Tkinter event loop
root.mainloop()

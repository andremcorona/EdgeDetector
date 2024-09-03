import cv2
from tkinter import filedialog

# Function to open a file dialog and load the selected image
def get_image():
    # Use Tkinter's filedialog to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    
    if filepath:
        img = cv2.imread(filepath)
        
        if img is None:
            print("Error: Unable to load image.")
            return
        
    return img

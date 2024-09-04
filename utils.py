import cv2
from tkinter import filedialog
import numpy as np

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

def noiseReduce(size, sigma):
    # Formula for gaussian filter kernel equation:
    # 1/2pi(sigma)^2 * exp(-(i-(k+1))^2+(j-(k+1))^2  /  2(simga)^2)
    # where 1 <= i and j <= (2k+1)
    size = int(size)
    x, y = np.mgrid[-size:size+1, -size:size+1]
    h = (1 / (2.0 * np.pi * sigma**2)) * np.exp(-((x**2 + y**2) / (2.0*sigma**2)))
    return h

def calcGradient(img):

    g = 1
    return g


def myBlur(img):
    img = 0

    return img

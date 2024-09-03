# Import necessary libraries
import cv2  # OpenCV library for image processing
import matplotlib.pyplot as plt  # Matplotlib for displaying images
from utils import * # Utils for functions created to keep main file clean

# Retrieve the image 
img = get_image()

# Reduce noise and smoothen the image using GaussianBlur
smoothed_img = cv2.GaussianBlur(img, (5, 5), 0)

# Apply the Canny edge detector
edges = cv2.Canny(smoothed_img, 5, 150, apertureSize = 3, L2gradient=True)

# Display the original image and the detected edges
plt.figure(figsize=(10, 10))

# Show original image
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for correct color display
plt.axis('off')

# Show detected edges
plt.subplot(2, 2, 2)
plt.title('Gaussian Blur')
plt.imshow(smoothed_img, cmap='gray')
plt.axis('off')

# Show detected edges
plt.subplot(2, 2, 3)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()
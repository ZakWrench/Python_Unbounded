import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpg")

# Define the grid parameters
grid_size = 50
grid_color = (255, 0, 0)
grid_thickness = 2

# Create a blank image with the same dimensions as the original image
grid_image = 255 * np.ones(image.shape, dtype=np.uint8)

# Iterate over the rows and columns of the image and draw the grid lines
for i in range(0, image.shape[1], grid_size):
    cv2.line(grid_image, (i, 0),
             (i, image.shape[0]), grid_color, grid_thickness)
for j in range(0, image.shape[0], grid_size):
    cv2.line(grid_image, (0, j),
             (image.shape[1], j), grid_color, grid_thickness)

# Combine the original image and the grid image using alpha blending
alpha = 0.5
beta = 1 - alpha
output = cv2.addWeighted(image, alpha, grid_image, beta, 0)

# Save the output image
cv2.imwrite("output.jpg", output)

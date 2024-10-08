import cv2
import numpy as np
import os

#Load the Amazon image

# Relative path to a folder above the root folder
pathOriginalImage = os.path.join("..", "images", "amazon01.jpeg")
image = cv2.imread(pathOriginalImage)

# Check if the image was loaded successfully
if image is not None:
    
    # Especificar o novo tamanho da imagem (por exemplo, 100x100 píxeis)
    newSizeOriginalImage = (700, 700)

    # Redimensionar a imagem
    originalImage = cv2.resize(image, newSizeOriginalImage)
    cv2.putText(originalImage, 'Original Image',(100,50), cv2.FONT_ITALIC, 1, (255,255,255),2, cv2.LINE_AA)

    # Convert the image to HSV color (Hue Saturation Value)
    hsv_image = cv2.cvtColor(originalImage, cv2.COLOR_BGR2HSV)

    # Set the lower limis and upper limits to the red color
    lower_red = np.array([0,100,100])
    upper_red = np.array([10, 255, 255])

    # Create a mask to identify only the pixels within the red range
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)

    # Apply the mask to the original image
    result_image = cv2.bitwise_and(originalImage, originalImage, mask=mask_red)
    cv2.putText(result_image, 'Fire Detection',(200,50), cv2.FONT_ITALIC, 1, (255,255,255),2, cv2.LINE_AA)

    # Combine the two images horizontally (side by side)
    combined_images = np.hstack((originalImage, result_image))

    # Show the original image and the processed image side by side
    cv2.imshow('Combined Images - Original Image x Fire Detection', combined_images)

    # Wait until the user presses any key to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error to load image.")
    


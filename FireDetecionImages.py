import cv2
import os
import FireDetection_Functions

#Load the Amazon image

# Relative path to a folder above the root folder
pathOriginalImage = os.path.join("..", "images", "amazon01.jpeg")
image = FireDetection_Functions.imread(pathOriginalImage)

# Check if the image was loaded successfully
if image is not None:
    
    # Especificar o novo tamanho da imagem (por exemplo, 100x100 píxeis)
    newSizeOriginalImage = FireDetection_Functions.newSizeOriginalImage(600,600)

    # Redimensionar a imagem
    originalImage = FireDetection_Functions.resize(image, newSizeOriginalImage)
    FireDetection_Functions.putText(originalImage, 'Original Image',(100,50), cv2.FONT_ITALIC, 1, (255,255,255),2, cv2.LINE_AA)

    # Convert the image to HSV color (Hue Saturation Value)
    hsv_image = FireDetection_Functions.hsvImageColor(originalImage, cv2.COLOR_BGR2HSV)

    # Set the lower limits and upper limits to the red color
    lower_red = FireDetection_Functions.npArray(0,100,100)
    upper_red = FireDetection_Functions.npArray(10, 255, 255)

    # Create a mask to identify only the pixels within the red range
    #mask_red = FireDetection_Functions.inRange(hsv_image, lower_red, upper_red)
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
 
    # Apply the mask to the original image
    #result_image = cv2.bitwise_and(originalImage, originalImage, mask_red)
    result_image = FireDetection_Functions.bitwise_and(originalImage, originalImage, mask_red)
       
    FireDetection_Functions.putText(result_image, 'Fire Detection',(200,50), cv2.FONT_ITALIC, 1, (255,255,255),2, cv2.LINE_AA)

    # Combine the two images horizontally (side by side)
    combined_images = FireDetection_Functions.hstack(originalImage, result_image)

    # Show the original image and the processed image side by side
    FireDetection_Functions.imshow('Combined Images - Original Image x Fire Detection', combined_images)

    # Wait until the user presses any key to close the windows
    FireDetection_Functions.waitKey(0)
    FireDetection_Functions.destroyAllWindows()
else:
    print("Error to load image.")
    

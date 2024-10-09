import cv2
import os
from AnalyseImage import AnalyseImage_Functions

#Check Image
def check_Image():
    # Check if the image was loaded successfully
    if image is not None:
        
        # Especificar o novo tamanho da imagem (por exemplo, 100x100 píxeis)
        newSizeOriginalImage = AnalyseImage_Functions.newSizeOriginalImage(600,600)

        # Redimensionar a imagem
        originalImage = AnalyseImage_Functions.resize(image, newSizeOriginalImage)
        AnalyseImage_Functions.putText(originalImage, 'Original Image',(100,50), cv2.FONT_ITALIC, 1, (255,255,255),2, cv2.LINE_AA)

        # Convert the image to HSV color (Hue Saturation Value)
        hsv_image = AnalyseImage_Functions.hsvImageColor(originalImage, cv2.COLOR_BGR2HSV)

        # Set the lower limits and upper limits to the red color
        lower_red = AnalyseImage_Functions.npArray(0,100,100)
        upper_red = AnalyseImage_Functions.npArray(10, 255, 255)

        # Create a mask to identify only the pixels within the red range
        mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
     
        # Apply the mask to the original image
        result_image = AnalyseImage_Functions.bitwise_and(originalImage, originalImage, mask_red)
           
        AnalyseImage_Functions.putText(result_image, 'Fire Detection',(200,50), cv2.FONT_ITALIC, 1, (255,255,255),2, cv2.LINE_AA)

        # Combine the two images horizontally (side by side)
        combined_images = AnalyseImage_Functions.hstack(originalImage, result_image)

        # Show the original image and the processed image side by side
        AnalyseImage_Functions.imshow('Combined Images - Original Image x Fire Detection', combined_images)

        # Wait until the user presses any key to close the windows
        AnalyseImage_Functions.waitKey(0)
        AnalyseImage_Functions.destroyAllWindows()
    else:
        print("Error to load image.")
        
# Relative path to a folder above the root folder
pathOriginalImage = os.path.join("..", "images", "amazon01.jpeg")
image = AnalyseImage_Functions.imread(pathOriginalImage)


    

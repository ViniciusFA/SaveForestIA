import cv2
import numpy as np

def newSizeOriginalImage(pixel01, pixel02):
  return (pixel01,pixel02)

# CV2 #
def resize(image, newSizeOriginalImage):
  return cv2.resize(image, newSizeOriginalImage)

def putText(originalImage, textImage, org, font, fontscale, color,  thicknessLine, lineType):
  return cv2.putText(originalImage, textImage,org, font, fontscale, color, thicknessLine, lineType)

def hsvImageColor(originalImage, color):
  return cv2.cvtColor(originalImage, color);

def inRange(hsv_image, lower_red, upper_red):
    return cv2.inRange(hsv_image, lower_red, upper_red)

def bitwise_and(originalImage01, originalImage02, mask):
    return cv2.bitwise_and(originalImage01, originalImage02, mask=mask)

def imread(image):
    return cv2.imread(image)

def imshow(fileName, image):
    return cv2.imshow(fileName, image)

def waitKey(number):
    return cv2.waitKey(number)

def destroyAllWindows():
    return cv2.destroyAllWindows()


# NP #
def npArray(arrayValue01,arrayValue02,arrayValue03):
    return np.array([arrayValue01, arrayValue02, arrayValue03])

def hstack(originalImage, result_image):
    return np.hstack((originalImage, result_image))


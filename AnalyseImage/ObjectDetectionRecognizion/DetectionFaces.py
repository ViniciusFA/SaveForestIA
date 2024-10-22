
import cv2
import sys
from tkinter import messagebox

# Function to detect and display faces and eyes
def detectAndDisplay(frame):    
        # Converting to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        # Detecting faces
        faces = face_cascade.detectMultiScale(frame_gray)
        for (x, y, w, h) in faces:
            center = (x + w//2, y + h//2)
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

            faceROI = frame_gray[y:y+h, x:x+w]
            # Detecting eyes on every face
            eyes = eyes_cascade.detectMultiScale(faceROI)
            for (ex, ey, ew, eh) in eyes:
                eye_center = (x + ex + ew//2, y + ey + eh//2)
                radius = int(round((ew + eh) * 0.25))
                frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)
      
            # Show the face and eyes image detection
            cv2.imshow('Capture - Face detection', frame)

# Confirm Action 
def confirm_action():
    # Confirmation box
    return messagebox.askquestion("Confirmation", "Do you allow access to your webcam?");

# Load classifiers
face_cascade_name = 'data/haarcascades/haarcascade_frontalface_alt.xml'
eyes_cascade_name = 'data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

# Check if files were uploaded correctly 
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error to load face cascade')
    sys.exit(-1)

if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    print('--(!)Error to load eyes cascade')
    sys.exit(-1)

# Starting the Video Capture
camera_device = 0
if(confirm_action() == 'yes'):
    capture = cv2.VideoCapture(camera_device)
    if not capture.isOpened():
        print('--(!)Error to open Video Capture')
        sys.exit(-1)

    while True:
        ret, frame = capture.read()
        if frame is None:
            print('--(!) No frame Captured -- Leaving...')
            break

        # Aplicando o classificador ao frame
        detectAndDisplay(frame)

        if cv2.waitKey(10) == 27:  # Press 'Esc' to leave
            break
    capture.release()
# Releasing video capture and closing windows

cv2.destroyAllWindows()

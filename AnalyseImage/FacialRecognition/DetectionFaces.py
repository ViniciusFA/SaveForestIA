import cv2
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

# Function to detect and display faces and eyes
def detectAndDisplay(frame, face_cascade, eyes_cascade):
    # Convert to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    # Detecting faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = frame_gray[y:y+h, x:x+w]
        # Detecting eyes in each face
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (ex, ey, ew, eh) in eyes:
            eye_center = (x + ex + ew//2, y + ey + eh//2)
            radius = int(round((ew + eh) * 0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)
    
    return frame

# Confirm Action 
def confirm_action():
    # Confirmation box
    return messagebox.askquestion("Confirmation", "Do you allow access to your webcam?");

# Function to start the video capture
def start_video_capture():
    # Create a new window to display the video feed
    video_window = tk.Toplevel(root)
    video_window.title("Face and Eyes Detection")

    # Create a label to display the video feed
    video_label = tk.Label(video_window)
    video_label.pack()

    # Load classifiers
    face_cascade_name = 'data/haarcascades/haarcascade_frontalface_alt.xml'
    eyes_cascade_name = 'data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'

    face_cascade = cv2.CascadeClassifier()
    eyes_cascade = cv2.CascadeClassifier()

    # Check if classifiers are loaded correctly
    if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
        print('--(!)Error loading face cascade')
        sys.exit(-1)
    if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
        print('--(!)Error loading eyes cascade')
        sys.exit(-1)

    # Start video capture
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        print('--(!)Error opening video capture')
        sys.exit(-1)

    def update_frame():
        ret, frame = capture.read()
        if ret:
            # Detect faces and eyes in the frame
            frame = detectAndDisplay(frame, face_cascade, eyes_cascade)

            # Convert the frame to RGB (from BGR) and display in Tkinter window
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the label with the new frame
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

        video_label.after(10, update_frame)

    # Start updating the frames
    update_frame()

    # Capture the current frame and save it
    def take_picture():
        ret, frame = capture.read()
        if ret:
            # Get the current date and time
            current_datetime = datetime.now()
            # Format the date and time as 'DD-MM-YYYY HH:MM:SS'
            formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')
            # File name
            file_path = 'captured_face_' + formatted_datetime + '.jpg'
            # Save the frame to a file (you can customize the file path)
            save_path = 'C:\\Users\\vinny\\Downloads\\' + file_path
            cv2.imwrite(save_path, frame)
            print(f"Picture saved as {file_path}")
            messagebox.showinfo("Image Capture", f"Image saved in {save_path}")
            
    # Capture Image
    action_button = tk.Button(video_window, text="Capture Image", command=take_picture)
    action_button.pack(pady=10)
    
    # Handle window close and release video capture
    def close_window():
        capture.release()       # Release the webcam
        cv2.destroyAllWindows() # Close any OpenCV windows
        video_window.destroy()  # Close the Tkinter window
        
    # Handle window close and release video capture
    video_window.protocol("WM_DELETE_WINDOW", close_window)


# Create main window
root = tk.Tk()
root.title("Face and Eye Detection")

# Create a frame to hold the widgets
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(padx=10, pady=10)

# Add a label inside the frame
label = tk.Label(main_frame, text="Press the button to start the webcam and detect faces and eyes.")
label.pack(pady=10)

# Add a button to start video capture
start_button = tk.Button(main_frame, text="Start Video", command=start_video_capture)
start_button.pack(pady=10)

# Run the system
root.mainloop()

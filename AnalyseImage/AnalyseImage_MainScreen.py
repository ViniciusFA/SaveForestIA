import tkinter as tk


# Object Recognition function 
def objectDetection_recognition():
    print('Object Detection and Recognition');

# Image Classification function
def image_classification():
    print('Image Classification');

# Image Segmentation function
def image_segmentation():
    print('Image Segmentation');

# Facial Recognition (OCR) function
def face_recognition():
    print('Facial Recognition (OCR)');

# Color Analysis
def color_analysis():
    print('Color Analysis');

# Emotion Sentiment Analysis
def emotion_sentiment_analysis():
    print('Emotion Sentiment Analysis');
    
# Scene Understanding
def scene_understanding():
    print('Scene Understanding');    

# Image Similarity Search
def image_similarity_search():
    print('Image Similarity Search');

# Anomaly Detection
def anomaly_detection():
    print('Anomaly Detection');

#3D Image Analysis
def image_3d_analysis():
    print('3D Image Analysis');

# Image Captioning
def image_captioning():
    print('Image Captioning');

# Action or Gesture Recognition
def action_gesture_recognition():
    print('Action or Gesture Recognition');
    
def main():
    # Creating the main window
    root = tk.Tk()
    root.title("Image Analysis")
    root.geometry("700x700")

    # Back Page 
    def back_application():
        root.destroy()  # Back the application

    # Exit program
    def exit_application():
        root.destroy()  # Close the application

    # Create a frame for the footer
    footer_frame = tk.Frame(root)
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X)  # Pack the frame at the bottom

    # Including a label
    label = tk.Label(root, text="Select one of the options below")
    label.pack(pady=10)

    # Object Detection and Recognition
    button = tk.Button(root, text="Object Detection and Recognition", command=objectDetection_recognition)
    button.pack(pady=10)

    # Image Classification
    button = tk.Button(root, text="Image Classification", command=image_classification)
    button.pack(pady=10)

    # Image Segmentation
    button = tk.Button(root, text="Image Segmentation", command=image_segmentation)
    button.pack(pady=10)

    # Facial Recognition (OCR)
    button = tk.Button(root, text="Facial Recognition (OCR)", command=face_recognition)
    button.pack(pady=10)

    # Color Analysis
    button = tk.Button(root, text="Color Analysis", command=color_analysis)
    button.pack(pady=10)

    # Emotion and Sentiment Analysis
    button = tk.Button(root, text="Emotion and Sentiment Analysis", command=emotion_sentiment_analysis)
    button.pack(pady=10)

    # Scene Understanding
    button = tk.Button(root, text="Scene Understanding", command=scene_understanding)
    button.pack(pady=10)

    # Image Similarity and Search
    button = tk.Button(root, text="Image Similarity and Search", command=image_similarity_search)
    button.pack(pady=10)

    # Anomaly Detection
    button = tk.Button(root, text="Anomaly Detection", command=anomaly_detection)
    button.pack(pady=10)

    # 3D Image Analysis
    button = tk.Button(root, text="3D Image Analysis", command=image_3d_analysis)
    button.pack(pady=10)

    # Image Captioning
    button = tk.Button(root, text="Image Captioning", command=image_captioning)
    button.pack(pady=10)

    # Action or Gesture Recognition
    button = tk.Button(root, text="Action or Gesture Recognition", command=action_gesture_recognition)
    button.pack(pady=10)
    
    # Create an back button
    button = tk.Button(root, text="Back", command=back_application)
    button.pack(pady=10)  # Add some padding

    # Create an exit button
    exit_button = tk.Button(footer_frame, text="Exit", command=exit_application)
    exit_button.pack(pady=20)  # Add some padding

    # Run the system
    root.mainloop()

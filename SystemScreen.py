import tkinter as tk
from Presentation.AnalyseImage import AnalyseImage_MainScreen
from Presentation.AnalyseImage import AnalyseImageImages


# Image Analysis function
def image_analysis():
    AnalyseImage_MainScreen.main()
    #AnalyseImageImages.check_Image()
    root.destroy()
    
# Object Detection function    
def object_detection():
    print('Object Detection')

# Object Recognition function 
def object_recognition():
    print('Object Recognition');

# Motion Detection function 
def object_recognition():
    print('Motion Detection');

# Exit program
def exit_application():
    root.destroy()  # Close the Application

# Creating the main window
root = tk.Tk()
root.title("IA System")
root.geometry("700x700")

# Create a frame for the footer
footer_frame = tk.Frame(root)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)  # Pack the frame at the bottom

# Including a label
label = tk.Label(root, text="Select one of the options below")
label.pack(pady=10)

# Including the Image Analysis button
button = tk.Button(root, text="Image Analysis", command=image_analysis)
button.pack(pady=10)

# Including the Object Detection button
button = tk.Button(root, text="Object Detection", command=object_detection)
button.pack(pady=10)

# Including the Object Recognition button
button = tk.Button(root, text="Object Recognition", command=object_recognition)
button.pack(pady=10)

# Including the Motion Detection button
button = tk.Button(root, text="Motion Detection", command=object_recognition)
button.pack(pady=10)

# Create an exit button
exit_button = tk.Button(footer_frame, text="Exit", command=exit_application)
exit_button.pack(pady=20)  # Add some padding

# Run the system
root.mainloop()

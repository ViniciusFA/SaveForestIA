import tkinter as tk
from AnalyseImage import AnalyseImageImages

# Image Analysis function
def image_analysis():
    AnalyseImageImages.check_Image()
    
# Object Detection function    
def object_detection():
    print('Object Detection')

# Object Recognition function 
def object_recognition():
    print('Object Recognition');

# Motion Detection function 
def object_recognition():
    print('Motion Detection');

# Creating the main window
root = tk.Tk()
root.title("IA System")
root.geometry("600x600")

# Including a label
label = tk.Label(root, text="Seleciona uma das opções abaixo:")
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

# Run the system
root.mainloop()

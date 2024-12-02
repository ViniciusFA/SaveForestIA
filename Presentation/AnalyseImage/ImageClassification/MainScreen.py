import tkinter as tk
from tkinter import filedialog


def display_fields():
    """Enable the fields according to the selected checkbox."""
    # Clean all the fields
    for widget in fields_frame.winfo_children():
        widget.destroy()

    if option_value.get() == "AWS":
        # Display fields to AWS Option
        tk.Label(fields_frame, text="Endpoint:").pack(anchor="w", pady=2)
        tk.Entry(fields_frame, width=30).pack(anchor="w", pady=2)

        tk.Label(fields_frame, text="Image to be classified:").pack(anchor="w", pady=2)
        image_field = tk.Label(fields_frame, text="Select Image", bg="lightgray", width=30, height=2)
        image_field.pack(anchor="w", pady=2)
        image_field.bind("<Button-1>", lambda e: load_image())

    elif option_value.get() == "Azure":
        # Display fields to Azure Option
        tk.Label(fields_frame, text="Endpoint:").pack(anchor="w", pady=2)
        tk.Entry(fields_frame, width=30).pack(anchor="w", pady=2)

        tk.Label(fields_frame, text="Key:").pack(anchor="w", pady=2)
        tk.Entry(fields_frame, width=30).pack(anchor="w", pady=2)

        tk.Label(fields_frame, text="Image to be classified:").pack(anchor="w", pady=2)
        image_field = tk.Label(fields_frame, text="Select Image", bg="lightgray", width=30, height=2)
        image_field.pack(anchor="w", pady=2)
        image_field.bind("<Button-1>", lambda e: load_image())


def load_image():
    """Abre um diálogo para selecionar uma imagem."""
    path = filedialog.askopenfilename(
        title="Selecionar imagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if path:
        print(f"Image selected: {path}")


# Main Window
root = tk.Tk()
root.title("Image Classification")
root.geometry("300x300")

# CheckBoxes Frame
frame_checkboxes = tk.Frame(root)
frame_checkboxes.pack(pady=10, padx=10)

# Variable to store the selected option
option_value = tk.StringVar(value="")

# Checkboxes
tk.Label(frame_checkboxes, text="Select one of the IA Service Provider below:").pack(anchor="w")
chk_a = tk.Radiobutton(frame_checkboxes, text="AWS", variable=option_value, value="AWS", command=display_fields)
print(option_value.get())
chk_a.pack(anchor="w")
chk_b = tk.Radiobutton(frame_checkboxes, text="Azure", variable=option_value, value="Azure", command=display_fields)
chk_b.pack(anchor="w")

# Dinamyc fields Frame 
fields_frame = tk.Frame(root)
fields_frame.pack(pady=10, padx=10)

# Run Application 
root.mainloop()

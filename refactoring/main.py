import os
import re
import shutil
import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def rename_images(input_folder, base_name, numbering_option, number_length=4):
    images = [f for f in os.listdir(input_folder) if
              re.search(r'\.(jpg|jpeg|png|gif|bmp|tiff|webp|avif)$', f, re.IGNORECASE)]
    images.sort()

    if not images:
        messagebox.showerror("Error", "No images found in the selected folder.")
        return

    for index, image in enumerate(images, start=1):
        ext = os.path.splitext(image)[1]
        if numbering_option == "Ordered":
            new_name = f"{base_name} {index}{ext}"
        else:  # Random numbers
            random_number = ''.join([str(random.randint(0, 9)) for _ in range(number_length)])
            new_name = f"{base_name} {random_number}{ext}"
        shutil.move(os.path.join(input_folder, image), os.path.join(input_folder, new_name))

    messagebox.showinfo("Success", f"Renamed {len(images)} images successfully.")


def open_gui():
    def start_renaming():
        input_folder = folder_var.get()
        base_name = name_var.get()
        numbering_option = numbering_var.get()
        number_length = int(length_var.get()) if numbering_option == "Random" else None

        if not input_folder or not base_name:
            messagebox.showerror("Error", "Please select a folder and enter a base name.")
            return

        rename_images(input_folder, base_name, numbering_option, number_length)

    def select_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            folder_var.set(folder_selected)

    root = tk.Tk()
    root.title("Image Renamer")
    root.geometry("450x300")
    root.resizable(False, False)
    root.configure(bg="#282c34")

    style = ttk.Style()
    style.configure("TLabel", foreground="white", background="#282c34", font=("Segoe UI", 10))
    style.configure("TButton", font=("Segoe UI", 10, "bold"), background="#61afef")
    style.configure("TEntry", font=("Segoe UI", 10))

    ttk.Label(root, text="Select Folder:").pack(pady=5)
    folder_var = tk.StringVar()
    folder_entry = ttk.Entry(root, textvariable=folder_var, width=50)
    folder_entry.pack()
    ttk.Button(root, text="Browse", command=select_folder).pack(pady=5)

    ttk.Label(root, text="Base Name:").pack(pady=5)
    name_var = tk.StringVar()
    name_entry = ttk.Entry(root, textvariable=name_var, width=50)
    name_entry.pack()

    numbering_var = tk.StringVar(value="Ordered")
    ttk.Label(root, text="Numbering Option:").pack(pady=5)
    numbering_combo = ttk.Combobox(root, textvariable=numbering_var, values=["Ordered", "Random"])
    numbering_combo.pack()

    ttk.Label(root, text="Random Number Length:").pack(pady=5)
    length_var = tk.StringVar(value="4")
    length_entry = ttk.Entry(root, textvariable=length_var, width=10)
    length_entry.pack()

    rename_button = ttk.Button(root, text="Rename Images", command=start_renaming)
    rename_button.pack(pady=20)
    rename_button.configure(style="TButton")

    root.mainloop()


if __name__ == "__main__":
    open_gui()
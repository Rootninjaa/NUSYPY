#translated by Deepl

import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

def save_code():
    # Get the filename and code from the user
    filename = filename_entry.get()
    code = code_entry.get("1.0", tk.END)

    if not filename:  # Show warning if the filename is empty
        messagebox.showwarning("Warning", "Please enter a filename.")
        return

    # Get the user directory and desktop path
    user_path = os.path.expanduser("~")
    desktop_path = os.path.join(user_path, "Desktop")
    file_path = os.path.join(desktop_path, filename + ".py")

    # Save the file
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        messagebox.showinfo("Success", f"{filename}.py has been saved to the desktop.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the file: {str(e)}")

# Create Tkinter window
window = tk.Tk()
window.title("NUSYPY")
window.geometry("800x600")
window.configure(bg="black")  # Background color

# Frame for the input area
frame = tk.Frame(window, bg="#ffffff", padx=10, pady=10)
frame.pack(pady=20)

# Label for the filename
filename_label = tk.Label(frame, text="Filename (without extension):", bg="#ffffff")
filename_label.pack(pady=5)

# Entry for filename
filename_entry = tk.Entry(frame, width=50)
filename_entry.pack(pady=5)

# Text area for code input with scrollbar
code_label = tk.Label(frame, text="Enter your Python code:", bg="#ffffff")
code_label.pack(pady=5)

code_entry = scrolledtext.ScrolledText(frame, width=100, height=20, wrap=tk.WORD)
code_entry.pack(pady=10)
code_entry.config(bg="gray")

# Save button
save_button = tk.Button(frame, text="Save My Code", font="Courier 12 bold", command=save_code, bg="#4CAF50", fg="white")
save_button.pack(pady=20)

window.mainloop()

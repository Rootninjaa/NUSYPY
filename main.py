#translated by Deepl

import tkinter as tk
from tkinter import messagebox, scrolledtext
import os
import webview


def Chatgpt():
    webview.create_window('ChatGpt', 'https://chatgpt.com')
    webview.start()

def package_add():
    os.system("start cmd")
    messagebox.showinfo("pip for NUSYPY", "add the library you want to add with pip example: pip install xyz")


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

window = tk.Tk()
window.title("NUSYPY")
window.geometry("800x600")
window.configure(bg="#9370db")

# Frame for the input area
frame = tk.Frame(window, bg="#9370db", padx=10, pady=10)
frame.pack()

filename_label = tk.Label(frame, text="Filename (without extension):", bg="#ffffff", font="Courier 15 bold")
filename_label.pack(pady=5)
filename_label.config(bg="#9370db")

filename_entry = tk.Entry(frame, width=50)
filename_entry.pack(pady=5)

code_label = tk.Label(frame, text="Enter your Python code:", bg="#ffffff", font="Courier 15 bold")
code_label.pack(pady=5)
code_label.config(bg="#9370db")

code_entry = scrolledtext.ScrolledText(frame, width=100, height=20, wrap=tk.WORD)
code_entry.pack(pady=10)
code_entry.config(bg="gray")

save_button = tk.Button(frame, text="Save My Code", font="Courier 14 bold", command=save_code, bg="#4CAF50", fg="white")
save_button.pack(pady=20)

packege_add = tk.Button(frame, text="NusyPip", font="Courier 14 bold", command=package_add)
packege_add.place(x=0, y=50)
packege_add.config(bg="#4CAF50", fg="white")

copilot = tk.Button(frame, text="chatgpt", font="Courier 14 bold", command=Chatgpt)
copilot.place(x=0, y=0)
copilot.config(bg="#4CAF50", fg="white")

window.mainloop()

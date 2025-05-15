import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            result_var.set("Length must be ≥ 4")
            return
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(chars, k=length))
        result_var.set(password)
    except ValueError:
        result_var.set("Enter a valid number")

# GUI setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x150")

tk.Label(window, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack()

tk.Button(window, text="Generate", command=generate_password).pack(pady=5)

result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var, width=30).pack(pady=5)

window.mainloop()


#!/usr/bin/python3

import time
import secrets
import string
import tkinter as tk
import pyperclip

# Color codes for the welcome message
WELCOME_COLOR = '\033[1;32m'
SELECT_COLOR = '\033[1;34m'
RESET_COLOR = '\033[0m'

def create_pw(pw_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False

    while not pw_strong:
        pwd = ''
        for i in range(pw_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
            sum(char in digits for char in pwd) >= 2):
            pw_strong = True

    return pwd

def generate_password():
    password = create_pw()
    password_label.config(text=password)

def select_option():
    option = option_var.get()
    if option == 1:
        password = create_pw()
        password_label.config(text=password)
    elif option == 2:
        version_text = "genpass, Python password generator\nVersion 1.0\nCoded by: astrohippie"
        password_label.config(text=version_text)
    elif option == 3:
        window.destroy()

def copy_password():
    pyperclip.copy(password_label.cget('text'))

window = tk.Tk()
window.title("genpass")

welcome_label = tk.Label(window, text="Welcome to genpass, the Python Password Generator!", fg="lime")
welcome_label.pack(pady=10)

option_var = tk.IntVar()

option_frame = tk.Frame(window)
option_frame.pack(pady=10)

generate_button = tk.Radiobutton(option_frame, text="Generate password", variable=option_var, value=1, fg="lime")
generate_button.pack()

version_button = tk.Radiobutton(option_frame, text="Check version", variable=option_var, value=2, fg="lime")
version_button.pack()

exit_button = tk.Radiobutton(option_frame, text="Exit", variable=option_var, value=3, fg="lime")
exit_button.pack()

password_label = tk.Label(window, text="", fg="lime")
password_label.pack(pady=10)

submit_button = tk.Button(window, text="Submit", command=select_option, fg="lime")
submit_button.pack(pady=10)

copy_button = tk.Button(window, text="Copy Password", command=copy_password, fg="lime")
copy_button.pack(pady=10)

window.mainloop()

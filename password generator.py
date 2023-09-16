import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_scale.get()
    complexity = complexity_scale.get()

    if length <= 0:
        messagebox.showerror("Invalid", "Password length is greater than zero.")
        return

    if complexity <= 0:
        messagebox.showerror("Invalid", "Password complexity is greater than zero.")
        return

    characters = ""
    if complexity >= 1:
        characters += string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password) 
def reset_password():
    length_scale.set(10)
    complexity_scale.set(2)
    password_entry.delete(0, tk.END)
root = tk.Tk()
root.title("Password Generator")
heading_label = tk.Label(root, text=" Random Password Generator", font=("bold", 30))
heading_label.pack(pady=12)
user_label = tk.Label(root, text="User Name:", font=("bold", 26))
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack(pady=7)
length_label = tk.Label(root, text="Password Length:",font=("bold", 26))
length_label.pack()
length_scale = tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, length=200,bg="pink")
length_scale.set(10)
length_scale.pack(pady=7)
complexity_label = tk.Label(root, text="Password Complexity:",font=("bold", 26))
complexity_label.pack()
complexity_scale = tk.Scale(root, from_=1, to=3, orient=tk.HORIZONTAL, length=200,bg="pink")
complexity_scale.set(2)
complexity_scale.pack(pady=7)
generate_button = tk.Button(root, text="Generate Password",bg="skyblue", command=generate_password)
generate_button.pack(pady=12)
password_label = tk.Label(root, text="Password:",font=("bold", 30))
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack(pady=7)
reset_button = tk.Button(root, text="Reset Password", command=reset_password,bg="yellow")
reset_button.pack(pady=12)

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

def generate_password(length):
    characters=("qwertyuiopasdfghjklzxcvbnm"
        "QWERTYUIOPASDFGHJKLZXCVBNM"
        "!@#$%^&*()_+=\:;,.?/<>")
    password= ''.join(random.choice(characters) for _ in range(length))
    return password
message = f"YOUR PASSWORD IS: \n"
def display_password():
    try:
        pass_length = int(len_entry.get())
        if pass_length<=0:
            message=f"PLEASE INPUT THE LENGTH OF PASSWORD GREATER THAN 0"
            messagebox.showinfo("I know your password hehe.",message)
        else:
            password=generate_password(pass_length)
            message=f"Your Password is: {password}"
            messagebox.showinfo("I know your password hehe.",message)

           
    except ValueError:
         message="VALUE ERROR PLEASE USE CORRECT VALUE AND TYPE"
         messagebox.showinfo("I know your password hehe.",message)


root= tk.Tk()
root.geometry("350x200")
root.configure(bg="pink")
root.title("Password Generator")
len_label=tk.Label(root,text="Enter the length of the password: ",bg="pink",fg="blue",font=("arial",15))
len_label.pack(pady=12)
len_entry=tk.Entry(root,font=("arial",15))
len_entry.pack(pady=10)
btn=tk.Button(root,text="Generate Password",bg="yellow",fg="green" ,command=display_password)
btn.pack(pady=12)

root.mainloop()
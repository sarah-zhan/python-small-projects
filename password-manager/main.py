import tkinter
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# label
website_lable = Label(text="Website: ")
website_lable.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# input
website_input = tkinter.Text(width=35, height=1)
website_input.grid(column=1, row=1, columnspan=2)

email_input = tkinter.Text(width=35, height=1)
email_input.grid(column=1, row=2, columnspan=2)

password_input = tkinter.Text(width=21, height=1)
password_input.grid(column=1, row=3)



window.mainloop()
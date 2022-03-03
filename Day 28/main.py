from tkinter import *
import random
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    nr_letters = 4
    nr_symbols = 4
    nr_numbers = 4
    total_length = nr_numbers+nr_letters+nr_symbols
    hard_password = []
    for i in range(0, nr_letters):
        hard_password.append(random.choice(letters))

    for i in range(0, nr_symbols):
        hard_password.append(random.choice(symbols))

    for i in range(0, nr_numbers):
        hard_password.append(random.choice(numbers))

    hardpass = ""
    random.shuffle(hard_password)
    for i in hard_password:
        hardpass += i
    pasw = password_entry.get()
    password_entry.delete(0, END)
    password_entry.insert(0, hardpass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open(os.path.join("Day 27", "password.txt"), "a") as f:
        f.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}"+"\n")
    f.close()

# ---------------------------- UI SETUP ------------------------------- #

# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file=os.path.join("Day 27","logo.png"))
logo = canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Text setup
website = Label(text="Website:")
website.grid(column=0, row=1)

emuser = Label(text="Email/Username:")
emuser.grid(column=0, row=2)

passw = Label(text="Password:")
passw.grid(column=0, row=3)

# Buttons Setup
genpass = Button(text="Generate Password", command=gen_password)
genpass.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save_password)
add.grid(column=1, row=4, columnspan=2)

# Entry Boxes
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column = 1, columnspan=2)

email_entry = Entry(width=50)
email_entry.insert(0, "fsaiyad990@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Window Mainloop
window.mainloop()

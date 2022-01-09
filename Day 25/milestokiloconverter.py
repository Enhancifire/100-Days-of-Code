from tkinter import *

window = Tk()
window.minsize(width=300, height=100)

text = Label(text="is equal to", font=("Arial", 20, "normal"))
text.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 20, "normal"))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("Arial", 20, "normal"))
km.grid(column=2, row=1)

converted = Label(text="0", font=("Arial", 20, "normal"))
converted.grid(column=1, row=1)

def convert():
    mile = input.get()
    kim = float(mile) * 1.60934
    converted.config(text=kim)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

input = Entry()
input.grid(column=1, row=0)

window.mainloop()
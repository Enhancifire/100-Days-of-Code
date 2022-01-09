import tkinter

window = tkinter.Tk()
window.title("TKinter First GUI")

window.minsize(width=600, height=600)

# Label

my_label = tkinter.Label(text="I am a Label")
my_label.pack()

# Loop for Window
window.mainloop()
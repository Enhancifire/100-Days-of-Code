import tkinter
import os
from tkinter import Tk, filedialog
from PIL import Image, ImageTk

watermark_path = ""
image_path = ""

def main():
    window = Tk()

    window.title("Watermarking App")
    window.config(padx = 100, pady = 50)

    def selectImage():

        filetypes = (
                ('text files', '*.txt'),
                ('All Files', '*.*')
                )

        global image_path

        file_path = filedialog.askopenfilename(
                title = "Open Image",
                filetypes = filetypes
                )

        image = Image.open(file_path)
        img = ImageTk.PhotoImage(image)

        canvas.create_image(10, 10, image = img, anchor = "center")

        canvas.config(width= image.size[0], height= image.size[1])
        image_entry.delete(0, tkinter.END)
        image_entry.insert(0, file_path)
        image_path = file_path

    def selectWatermark():

        filetypes = (
                ('jpg', '*.jpg'),
                ('All Files', '*.*')
                )

        global watermark_path

        watermark_path = filedialog.askopenfilename(
                title = "Open Image",
                filetypes = filetypes
                )
        watermark_entry.delete(0, tkinter.END)
        watermark_entry.insert(0, watermark_path)

        watermark_path = watermark_path


    image_select_button = tkinter.Button(text= "Select Image", command= selectImage)
    image_select_button.grid(column= 0, row= 1)

    image_entry = tkinter.Entry(width= 50)
    image_entry.grid(column = 1, row = 1)


    watermark_select_button = tkinter.Button(text= "Select Watermark", command= selectWatermark)
    watermark_select_button.grid(column= 0, row= 2)

    watermark_entry = tkinter.Entry(width= 50)
    watermark_entry.grid(column = 1, row = 2)

    canvas = tkinter.Canvas(window, width= 800, height= 800)
    canvas.grid(column = 0, row = 0)

    window.mainloop()

if __name__ == "__main__":
    main()

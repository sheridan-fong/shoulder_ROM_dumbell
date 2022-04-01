from tkinter import *
from PIL import ImageTk, Image

import global_var


def btn_clicked():
    print("Button Clicked")

def home():
    window.destroy()
    import main


window = Tk()

window.geometry("792x612")
window.configure(bg = "#ffffff")
f = ("Times bold", 14)
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 612,
    width = 792,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file =f"results_bkgd.png")
background = canvas.create_image(
    396.0, 306.0,
    image=background_img)

img0 = PhotoImage(file =f"home_btn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = home,
    relief = "flat")

b0.place(
    x = 666, y = 8,
    width = 175,
    height = 44)

img = Image.open("euler.png")
img = img.resize((250,250), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
label1 = Label(image=img)
label1.image = img
label1.place(x=26,y=299)

Label(
    window,
    text=global_var.rom_value_text,
    font=f,
    # padx=20,
    # pady=50,
    bg='#FDF6EC'
).place(x=375, y = 195)

window.resizable(False, False)
window.mainloop()

from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("792x612")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 612,
    width = 792,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = -267, y = 21,
    width = 200,
    height = 76)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = -267, y = 107,
    width = 200,
    height = 76)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = -267, y = 193,
    width = 200,
    height = 76)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    -572.0, 330.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()

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
    x = 526, y = 65,
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
    x = 526, y = 171,
    width = 200,
    height = 76)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    220, 306.5,
    image=background_img)

window.resizable(
    False, False)
window.mainloop()

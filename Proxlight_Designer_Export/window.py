from tkinter import *

def btn_clicked():
    print("Button Clicked")

window = Tk()

window.geometry("1440x960")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 960,
    width = 1440,
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
    x = 3172, y = -883,
    width = 161,
    height = 75)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    3862.0, -431.0,
    image=background_img)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 4390, y = -883,
    width = 161,
    height = 75)

window.resizable(False, False)
window.mainloop()
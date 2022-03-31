from tkinter import *


def btn_clicked():
    print("Button Clicked")

def results():
    window.destroy()
    import end_pg


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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    207.5, 307.5,
    image=background_img)

img0 = PhotoImage(file =f"start2_btn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 493, y = 56,
    width = 200,
    height = 76)

img1 = PhotoImage(file =f"end2_btn.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = results,
    relief = "flat")

b1.place(
    x = 493, y = 155,
    width = 200,
    height = 76)

window.resizable(False, False)
window.mainloop()

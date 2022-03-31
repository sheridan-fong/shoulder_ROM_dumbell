from tkinter import *


def btn_clicked():
    print("Button Clicked")

def home():
    window.destroy()
    import main


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

window.resizable(False, False)
window.mainloop()

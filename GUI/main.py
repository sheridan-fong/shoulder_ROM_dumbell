from tkinter import *
import global_var
from PIL import ImageTk, Image

# ----- functions ------
def btn_clicked():
    print("Button Clicked in main")

def side_lying():
    set_exercise_one_off()
    print(global_var.exercise_one)
    window.destroy()
    import exercise_two_pg

def reverse_fly():
    set_exercise_one_on()
    print(global_var.exercise_one)
    window.destroy()
    import exercise_one_pg
    print("made it past import")

def set_exercise_one_off():
    global_var.exercise_one = False

def set_exercise_one_on():
    exercise_one = True

# ----- setting up the window --------
window = Tk()
window.title('main')

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

# --- commented out for testing
# global background_img
# background_img = ImageTk.PhotoImage(Image.open("main_bkgd.png"))
# background = canvas.create_image(
#     400.5, 306.0,
#     image=background_img)

# ---- trying to create the image as a label instead
background_img = ImageTk.PhotoImage(Image.open("main_bkgd.png"))
label1 = Label(image=background_img)
label1.image = background_img
label1.place(x=0,y=0)

img0 = PhotoImage(file =f"reverse_fly_btn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    # command = lambda:[global_var.set_exercise_one_on(),reverse_fly],
    command = reverse_fly,
    relief = "flat")

b0.place(
    x = 329, y = 422,
    width = 200,
    height = 76)

img1 = PhotoImage(file =f"side_lying_btn.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = side_lying,
    # command = lambda:[global_var.set_exercise_one_off(),side_lying],
    relief = "flat")

b1.place(
    x = 561, y = 422,
    width = 200,
    height = 76)

print("in main page")
window.resizable(False, False)
window.mainloop()
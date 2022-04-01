from tkinter import *
import global_var

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

def set_exercise_one_off():
    global_var.exercise_one = False

def set_exercise_one_on():
    exercise_one = True


# ----- setting up the window --------
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

background_img = PhotoImage(file =f"main_bkgd.png")
background = canvas.create_image(
    400.5, 306.0,
    image=background_img)

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

window.resizable(False, False)
window.mainloop()
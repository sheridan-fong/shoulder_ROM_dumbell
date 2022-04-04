import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


window = tk.Tk()

# ---- functions -----

# shows the frame to the screen
def show_frame(frame):
    frame.tkraise()

# make sures that the window will expand
window.geometry("792x612")
window.configure(bg="#ffffff")

# --- creating/initializing all of our frames ---
home = tk.Frame(window)
exercise_one = tk.Frame(window)
exercise_two = tk.Frame(window)
result = tk.Frame(window)

for frame in (home, exercise_one, exercise_two, result):
    frame.grid(row=0, column=0, sticky='nsew')

# setting the first frame that you see ---
show_frame(home)

# -------- setting up home page ------------

# --- background image --
background_img = ImageTk.PhotoImage(Image.open("main_bkgd.png"))
frame1_title = tk.Label(home, text="this is frame one", image = background_img)
frame1_title.pack(fill = 'x')

# -- buttons --

img0 = PhotoImage(file =f"reverse_fly_btn.png")
img1 = PhotoImage(file =f"side_lying_btn.png")

b0 = Button(home,image = img0, borderwidth = 0,highlightthickness = 0,
    command = exercise_one,relief = "flat")
b0.place(x = 329, y = 422,width = 200,height = 76)

b1 = Button(home,image = img1, borderwidth = 0,highlightthickness = 0,
    command = exercise_two, relief = "flat")
b1.place(x = 561, y = 422,width = 200, height = 76)


window.mainloop()
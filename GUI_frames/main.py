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
background_img = ImageTk.PhotoImage(Image.open("main_bkgd.png"))
label1 = Label(home, image=background_img)
label1.image = background_img
label1.place(x=0,y=0)




window.mainloop()
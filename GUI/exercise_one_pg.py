# solved prominent invalid command name : https://stackoverflow.com/questions/36402134/tkinter-root-after-cancel
# stackoverflow instead of using destory hide https://stackoverflow.com/questions/60364577/i-want-to-destroy-a-window-and-then-re-open-it-tkinter#:~:text=After%20you%20destroy%20this%20window,make%20it%20hide%20or%20show.


from tkinter import *
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import global_func
import data_analysis
from PIL import ImageTk, Image

# ----- Main gui code ------------
import global_var

window = Tk()
window.geometry("792x612")
window.configure(bg="#ffffff")
canvas_bkg = Canvas(
    window,
    bg="#ffffff",
    height=612,
    width=792,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas_bkg.place(x=0, y=0)

background_img = PhotoImage(file=f"reverse_fly_bkgd.png")
background = canvas_bkg.create_image(
    220, 306.5,
    image=background_img)

# background_img = ImageTk.PhotoImage(Image.open("reverse_fly_bkgd.png"))
# label1 = Label(image=background_img)
# label1.image = background_img
# label1.place(x=220,y=306.5)

# ----- create a figure plot object on GUI --------
fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Degrees vs. # of Data Points')
# ax.set_title('Live ROM (Degrees vs. Data Points)')
# ax.set_xlabel('Data Points')
ax.set_ylabel('Degrees')
ax.set_ylim(-180, 360)
ax.set_xlim(0, 50)
lines = ax.plot([], [])[0]  # this gives an array that is varying moved as global variable

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea
canvas.get_tk_widget().place(x=475, y=250, width=300, height=325)
canvas.draw()

# ------------ functions from yt video -----
data = np.array([])
condition = False


def plot_data():
    global condition
    global data

    if condition:
        arduinoString = global_func.arduinoData.readline()
        data_array = arduinoString.decode().split(',')  # split on comma

        # keeps only 100 data points
        if len(data) < 50:
            data = np.append(data, float(data_array[0]))
        else:
            data[0:49] = data[1:50]
            data[49] = float(data_array[0])

        global_var.euler_data.append(float(data_array[0]))
        # force data
        global_var.force_data.append(float(data_array[1]))

        lines.set_xdata(np.arange(start=0, stop=len(data), step=1))
        lines.set_ydata(data)
        canvas.draw()

    global AFTER
    AFTER = window.after(1, plot_data)


def plot_start():
    global condition
    global_var.data_on()
    condition = True
    global_func.arduinoData.reset_input_buffer()


def plot_end():
    global condition
    condition = False
    data_analysis.rom_analysis()
    btn_clicked()


# ------ functions for button clicking ------
def btn_clicked():
    print("Button Clicked")


# https://stackoverflow.com/questions/63628566/how-to-handle-invalid-command-name-error-while-executing-after-script-in-tk
def results():
    # window.quit()
    window.withdraw()
    import end_pg


def callback():
    global after_id
    var.set(var.get() + 1)
    after_id = window.after(500, callback)
    # print('in callback function')
    window.protocol('WM_DELETE_WINDOW', quit)


def quit():
    global AFTER
    "Cancel all scheduled callbacks and quit."
    window.after_cancel(AFTER)
    window.destroy()
    print("made it to quit")
    import end_pg


def open_end_pg():
    print("before here")
    import end_pg
    # print("after issue")
    # import end_pg2
    # print("made it to second after")
    # import main
    # print("failed to import main in exercise_one")


# ------ no functions just tkinter window stuff ------
img0 = PhotoImage(file=f"start_btn.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=plot_start,
    relief="flat")

b0.place(
    x=526, y=20,
    width=200,
    height=76)

img1 = PhotoImage(file=f"end_btn.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=plot_end,
    # command = lambda:[plot_end(), callback()],
    # command = lambda:[plot_end(), data_analysis.rom_analysis(), results(), btn_clicked()],
    relief="flat")

b1.place(
    x=526, y=105,
    width=200,
    height=76)

img2 = PhotoImage(file=f"results_btn.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=quit,
    # command = lambda:[plot_end(), callback()],
    # command = lambda:[plot_end(), data_analysis.rom_analysis(), results(), btn_clicked()],
    relief="flat")

b2.place(
    x=526, y=190,
    width=200,
    height=76)

window.resizable(
    False, False)

# # # ---- code from stackoverflow
var = tk.IntVar()
# window.pack_propagate(False)
# tk.Label(window, textvariable=var).pack()
# callback()
# window.protocol('WM_DELETE_WINDOW', quit)

# ----- plotting code from youtube ------
window.after(1, plot_data)
window.mainloop()
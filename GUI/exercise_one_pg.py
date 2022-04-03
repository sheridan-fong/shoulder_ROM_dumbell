from tkinter import *
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import global_func
import data_analysis


# ----- Main gui code ------------
import global_var

window = Tk()
window.geometry("792x612")
window.configure(bg = "#ffffff")
canvas_bkg = Canvas(
    window,
    bg = "#ffffff",
    height = 612,
    width = 792,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_bkg.place(x = 0, y = 0)

background_img = PhotoImage(file =f"reverse_fly_bkgd.png")
background = canvas_bkg.create_image(
    220, 306.5,
    image=background_img)

# ----- create a figure plot object on GUI --------
fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Degrees vs. # of Data Points')
# ax.set_title('Live ROM (Degrees vs. Data Points)')
# ax.set_xlabel('Data Points')
ax.set_ylabel('Degrees')
ax.set_ylim(-180, 360)
ax.set_xlim(0,50)
lines = ax.plot([],[])[0]  # this gives an array that is varying moved as global variable

canvas = FigureCanvasTkAgg(fig, master=window)    # A tk.DrawingArea
canvas.get_tk_widget().place(x = 475, y = 250, width = 300, height = 325)
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
    

        lines.set_xdata(np.arange(start=0, stop=len(data),step=1))
        lines.set_ydata(data)
        canvas.draw()

    window.after(1, plot_data)

def plot_start():
    global condition
    global_var.data_on()
    condition = True
    global_func.arduinoData.reset_input_buffer()

def plot_end():
    global condition
    condition = False

    data_analysis.rom_analysis()
    results()
    btn_clicked()


# ------ functions for button clicking ------
def btn_clicked():
    print("Button Clicked")

#https://stackoverflow.com/questions/63628566/how-to-handle-invalid-command-name-error-while-executing-after-script-in-tk
def results():
    window.destroy()
    import end_pg

def callback():
    global after_id
    var.set(var.get() + 1)
    after_id = window.after(500,callback)

def quit():
    "Cancel all scheduled callbacks and quit."
    window.after_cancel(after_id)
    window.destroy()


# ------ no functions just tkinter window stuff ------


img0 = PhotoImage(file =f"start_btn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:[plot_start()],
    relief = "flat")

b0.place(
    x = 526, y = 65,
    width = 200,
    height = 76)

img1 = PhotoImage(file =f"end_btn.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = plot_end,
    # command = lambda:[plot_end(), data_analysis.rom_analysis(), results(), btn_clicked()],
    relief = "flat")

b1.place(
    x = 526, y = 171,
    width = 200,
    height = 76)


window.resizable(
    False, False)

window.after(1, plot_data)
window.mainloop()
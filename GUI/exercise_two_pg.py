from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import global_func
import data_analysis
import global_var

# ---------- Main GUI code ------
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

 # -- create a figure plot object on GUI -----

fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Degrees vs. # of Data Points')
# ax.set_title('Live ROM (Degrees vs. Data Points)')
# ax.set_xlabel('Data Points')
ax.set_ylabel('Degrees')
ax.set_ylim(-180, 360)
ax.set_xlim(0,100)
lines = ax.plot([],[])[0]  # this gives an array that is varying moved as global variable

canvas = FigureCanvasTkAgg(fig, master=window)    # A tk.DrawingArea
canvas.get_tk_widget().place(x = 440, y = 250, width = 300, height = 325)
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
        if len(data) < 100:
            data = np.append(data, float(data_array[0]))
        else:
            data[0:99] = data[1:100]
            data[99] = float(data_array[0])

        global_var.euler_data.append(float(data_array[0]))
        # force data
        global_var.force_data.append(float(data_array[1]))

        lines.set_xdata(np.arange(start=0, stop=len(data),step=1))
        lines.set_ydata(data)
        canvas.draw()

    window.after(1, plot_data)

def plot_start():
    global condition
    condition = True
    global_func.arduinoData.reset_input_buffer()

def plot_end():
    global condition
    condition = False

# ---- original functions ---
def btn_clicked():
    print("Button Clicked")

def results():
    window.destroy()
    import end_pg


img0 = PhotoImage(file =f"start2_btn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = plot_start,
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
    command = lambda:[plot_end(), data_analysis.rom_analysis(), results()],
    relief = "flat")

b1.place(
    x = 493, y = 155,
    width = 200,
    height = 76)

window.resizable(False, False)

window.after(1, plot_data)
window.mainloop()

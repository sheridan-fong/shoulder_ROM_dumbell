from tkinter import *
import threading
import arduino_live
import global_var
from arduino_live import *
from global_var import *

# --- imports from yt video -----
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time

# ----- Main gui code ------------
root = tk.Tk()
root.geometry('600x600')  # set the windows size
root.title('Live Graphing')
# root.configure(background = 'light blue')
root['bg'] = '#ffbf00'

f = ("Times bold", 14)

# ----- create a figure plot object on GUI --------
fig = Figure()
ax = fig.add_subplot(111)

ax.set_title('Live Range of Motion Euler Angles')
ax.set_xlabel('Data Points')
ax.set_ylabel('Degrees')
ax.set_ylim(-180, 360)
ax.set_xlim(0,100)
lines = ax.plot([],[])[0]  # this gives an array that is varying moved as global variable

canvas = FigureCanvasTkAgg(fig, master=root)    # A tk.DrawingArea
canvas.get_tk_widget().place(x = 100, y = 110, width = 400, height = 400)
canvas.draw()

 # -------------------------- youtube video --------------------------
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

        # storing in variables and storing it as floating point data
        print(data)

        lines.set_xdata(np.arange(start=0, stop=len(data),step=1))
        lines.set_ydata(data)
        canvas.draw()

    root.after(1, plot_data)

def plot_start():
    global condition
    condition = True
    global_func.arduinoData.reset_input_buffer()

def plot_end():
    global condition
    condition = False

def start_data_collection():
    threading.Thread(target=arduino_live.collect_data(global_var.collecting_data)).start


def endPage():
    root.destroy()
    import end_pg

# ------------ creating title and buttons -----------------
Label(
    root,
    text="Reverse Fly Exercise",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).place(x = 200, y = 40)

Button(
    root,
    text="Start",
    font=f,
    command=lambda:[plot_start()],
    # command=lambda:[global_var.data_on(),global_var.data_status(), start_data_collection()]
).pack(fill=X, expand=TRUE, anchor = 's',side=LEFT)

Button(
    root,
    text="End",
    font=f,
    command= lambda:[plot_end(),endPage()],
    # command=lambda:[global_var.data_off(),arduino_live.collect_data(global_var.collecting_data), arduino_live.rom_analysis_exercise_one(), endPage()]
).pack(fill=X, expand=TRUE,anchor = 's', side=LEFT)

root.after(1, plot_data)
root.mainloop()
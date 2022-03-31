## @file arduino_live.py
#  @author Group 31
# @brief Main code for ROMbell
# @date 04/08/2022

# Sheridan note to self - see if you can import figures in pygame live?

# importing libraries to do python code
import serial # serial library to connect arduino serial monitor to python
import matplotlib.pyplot as plt  # shortcut
import matplotlib.dates as mdates
import numpy as np
from drawnow import *  # import all of drawnow library
from datetime import date
import datetime
# creating objects
import global_var
import matplotlib


matplotlib.use("TkAgg")  # the backend of matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import tkinter as tk

arduinoData = serial.Serial('com6', 115200) # where the information is coming from and the baud rate
euler_x_array = []
euler_z_array = []
plt.ion()  # tell matplotlib that you want interactive mode to plot live data
count = 0  # counter for data points

# --------- youtube tutorial for live plotting
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time


data = np.array([])
condition = False

def plot_data():
    global condition
    global data

    if condition:
        arduinoString = arduinoData.readline()
        data_array = arduinoString.decode().split(',')  # split on comma

        # keeps only 100 data points
        if len(data) < 100:
            data = np.append(data, float(data_array[0]))
        else:
            data[0:99] = data[1:100]
            data[99] = float(data_array[0])

        # storing in variables and storing it as floating point data
        euler_x_point = float(data_array[0])

        global_var.lines.set_xdata(np.arrange(start=0, stop=len(data),step=1))
        global_var.lines.set_ydata(data)

        global_var.canvas.draw()

    global_var.root.after(1, plot_data)

def plot_start():
    global condition
    condition = True
    arduinoData.reset_input_buffer()

def plot_end():
    global condition
    condition = False



## @brief Creates a function that makes our desired plots
def plot_graph():

    # setting parameters and labels for plt 1
    # plt.ylim(-180,180)  # this would depend on the exercise!
    plt.xlim(0,50)
    plt.title("x-axis euler angle live streaming sensor data")
    plt.ylabel("x-axis euler angle")
    plt.grid(True)  # turns the grid on

    # setting up plt2
    # plt2 = plt.twinx()  # twins the settings and creates a second y-axis
    # plt.ylim(-180, 180) # setting plot 2's y-limit on the right.
    # plt2.set_ylabel("z-axis euler angle")

    # plotting the graphs
    plt.plot(global_var.euler_data, "ro-", label='x-axis angles in degrees')  # plot x-axis data and makes it red with dots
    # plt2.plot(euler_z_array, "b^-", label='z-axis euler angle')  # plot z-axis data and make it blue triangles
    # plt2.ticklabel_format(useOffset=False)  # forces matplotlib to not autoscale the y-axis

    plt.legend(loc='upper left')
    # plt2.legend(loc='upper left')


def collect_data(collecting_data):
    count = 0
    euler_x_array = []
    euler_z_array = []


    while collecting_data: # loop always runs

        while (arduinoData.inWaiting() == 0):   # wait here until there is data make a separate conditional for when the person presses the button
            pass  # do nothing

        arduinoString = arduinoData.readline()  # reads the data coming in
        data_array = arduinoString.decode().split(',')  # split on comma

        # storing in variables and storing it as floating point data
        euler_x_point = float(data_array[0])
        euler_z_point = float(data_array[1])

        # appending values to the array
        global_var.euler_data.append(euler_x_point)
        # euler_z_array.append(euler_z_point)

        drawnow(plot_graph)  # call drawnow to update our live graph
        plt.pause(.00001)
        count += 1

        # getting rid of the first element if the array is longer than 50 so data does not get squished over time
        if(count > 50):
            global_var.euler_data.pop(0)
            # euler_z_array.pop(0)

        # print(len(euler_x_array))

def end_graph():
    f = Figure(figsize=(5, 5), dpi = 100)
    a = f.add_subplot(111)  # means there is only one chart
    a.plot([1,2,3,4,5],[5,6,1,3,2,9])

    canvas = FigureCanvasTkAgg(f)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)




def rom_analysis_exercise_one():
    plt.close()

    # getting maximum and minimum values and finding the difference
    minimum = min(global_var.euler_data)
    maximum = max(global_var.euler_data)
    global_var.rom = abs(maximum - minimum)
    global_var.rom_value_text = "Your range of motion is: {}".format(global_var.rom)

    # choosing the correct phrase to output to the screen
    if global_var.rom >= 90:
        global_var.rom_phrase = "Congrats, you have FANTASTIC ROM"
    elif global_var.rom >= 75:
        global_var.rom_phrase = "You're almost there, you're doing AMAZING"
    elif global_var.rom >= 45:
        global_var.rom_phrase = "Keep going, you are more than halfway there!"
    else:
        global_var.rom_phrase = "You still have quite a ways to go, but I believe in you"

    # have a counter that plots your data over time - or figure out how to plot without it

    # writing the value to a text file ** Sheridan needs to add date
    with open('reverse_fly_history.txt', 'a') as file:
        rom_text = "{},{}".format(global_var.rom, date.today())
        file.write(rom_text)
        file.write("\n")

    # printing to the screen to test splitting
    rom_graph()

def test_figure():
    f = Figure

def rom_graph():
    # reading the text file
    value_data = []
    date_data = []

    my_file = open("reverse_fly_history.txt", "r")
    content = my_file.read().splitlines()

    # converting into x and y data sets
    # print(content)

    for data_point in content:
        data = data_point.split(',')
        value_data.append(data[0])
        date_data.append(data[1])

    value_data_float = []
    for value in value_data:
        value_data_float.append(float(value))

    print("this is the value_data_float",value_data_float)

    x_values = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in date_data]
    y_values = value_data_float

    global_var.x_data = x_values
    global_var.y_data = y_values

    ax = plt.gca()

    formatter = mdates.DateFormatter("%Y-%m-%d")

    ax.xaxis.set_major_formatter(formatter)

    locator = mdates.DayLocator()

    ax.xaxis.set_major_locator(locator)

    plt.plot(x_values, y_values, "go-")

    # plt.ylim(0, 360)
    plt.title("Range of Motion Data over Time")

    plt.savefig('euler.png')

def collect_data_slow(collecting_data):
    count = 0

    while collecting_data:  # loop always runs

        while (
                arduinoData.inWaiting() == 0):  # wait here until there is data make a separate conditional for when the person presses the button
            pass  # do nothing

        arduinoString = arduinoData.readline()  # reads the data coming in
        data_array = arduinoString.decode().split(',')  # split on comma

        # storing in variables and storing it as floating point data
        euler_x_point = float(data_array[0])

        # appending values to the array
        global_var.euler_data.append(euler_x_point)

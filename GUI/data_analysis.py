import matplotlib.dates as mdates
import global_var
import matplotlib
import global_func
from drawnow import *  # import all of drawnow library
from datetime import date
import datetime

def rom_analysis_exercise_one():
    plt.close()  # could maybe take out

    # getting maximum and minimum values and finding the difference
    minimum = min(global_var.euler_data)
    maximum = max(global_var.euler_data)
    global_var.rom = abs(maximum - minimum)
    global_var.rom_value_text = "{}".format(global_var.rom)

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

def rom_graph():
    # reading the text file
    value_data = []
    date_data = []


    if global_var.exercise_one:
        my_file = open("reverse_fly_history.txt", "r")
    else:
        my_file = open("rotation_history.txt","r")

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

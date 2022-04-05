import matplotlib.dates as mdates
import global_var
import matplotlib
import global_func
from drawnow import *  # import all of drawnow library
from datetime import date
import datetime


def rom_analysis():
    # plt.close()  # could maybe take out

    # getting maximum and minimum values and finding the difference
    minimum = min(global_var.euler_data)
    maximum = max(global_var.euler_data)
    global_var.rom = abs(maximum - minimum)
    answer = str(round(global_var.rom, 2))
    global_var.rom_value_text = "{}".format(answer)
    print("rom value text",global_var.rom_value_text)

    # choosing the correct phrase to output to the screen for reverse fly and side-lying rotation
    # sheridan to separate into new line
    print("exercise one status",global_var.exercise_one)

    if global_var.exercise_one:
        print("exercise_one_phrases")
        if global_var.rom >= 90:
            global_var.rom_phrase = "Congrats, you have \n FANTASTIC ROM"
        elif global_var.rom >= 75:
            global_var.rom_phrase = "You're almost there, \n you're doing AMAZING"
        elif global_var.rom >= 45:
            global_var.rom_phrase = "Keep going, you are \n more than halfway there!"
        else:
            global_var.rom_phrase = "You still have quite a \n ways to go,\n but I believe in you"
    elif global_var.exercise_one != True:
        print("exercise_two_phrases")
        if global_var.rom >= 180:
            global_var.rom_phrase = "Congrats, you have \n FANTASTIC ROM"
        elif global_var.rom >= 135:
            global_var.rom_phrase = "You're almost there, \n you're doing AMAZING"
        elif global_var.rom >= 90:
            global_var.rom_phrase = "Keep going, you are \n more than halfway there!"
        else:
            global_var.rom_phrase = "You still have quite a \n ways to go,\n but I believe in you"

    # sheridan to call in force function to do analysis and then write to data
    global_var.force_value_text = force_analysis()
    avg_force_value = global_var.force_value_text

    # writing the force sensor data to a text file
    with open('force_history.txt', 'a') as file:
        force_text= "{},{}".format(avg_force_value, date.today())
        file.write(force_text)
        file.write("\n")
        file.close

    # writing the RM values to a text file
    if global_var.exercise_one:
        with open('reverse_fly_history.txt', 'a') as file:
            rom_text = "{},{}".format(global_var.rom, date.today())
            file.write(rom_text)
            file.write("\n")
            file.close()
    else:
        with open('rotation_history.txt', 'a') as file:
            rom_text = "{},{}".format(global_var.rom, date.today())
            file.write(rom_text)
            file.write("\n")
            file.close()

    # saves graph for results page to read in
    save_graph()
    force_save_graph()


def force_analysis():
    # sorting the values in descending
    sorted_force_data = sorted(global_var.force_data, reverse=True)

    total = 0
    # take top five data points

    if(len(sorted_force_data) < 5):
        sorted_force_data = [0,0,0,0,0]

    for i in range(5):
        total = sorted_force_data[i]

    average = total/5

    # print("this is the avg: force_data: ", str(round(average,2)))

    return str(round(average, 2))

def force_save_graph():
    # reading the text file
    value_data = []
    date_data = []

    my_file = open("force_history.txt", "r")

    content = my_file.read().splitlines()

    # converting into x and y data sets
    for data_point in content:
        data = data_point.split(',')
        value_data.append(data[0])
        date_data.append(data[1])

    value_data_float = []
    for value in value_data:
        value_data_float.append(float(value))

    x_values = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in date_data]
    y_values = value_data_float

    # global_var.x_data = x_values
    # global_var.y_data = y_values

    ax = plt.gca()

    formatter = mdates.DateFormatter("%Y-%m-%d")

    ax.xaxis.set_major_formatter(formatter)

    locator = mdates.DayLocator()

    ax.xaxis.set_major_locator(locator)

    plt.plot(x_values, y_values, "bo-")

    # plt.ylim(0, 360)
    plt.title("Force Data over Time")

    # Sheridan figure out why it's graphing the incorrect text file
    plt.savefig('force.png')

    plt.close()


def save_graph():
    # reading the text file
    value_data = []
    date_data = []

    # reading the appropriate text file
    if global_var.exercise_one:
        my_file = open("reverse_fly_history.txt", "r")
    else:
        my_file = open("rotation_history.txt", "r")

    content = my_file.read().splitlines()

    # converting into x and y data sets
    for data_point in content:
        data = data_point.split(',')
        value_data.append(data[0])
        date_data.append(data[1])

    value_data_float = []
    for value in value_data:
        value_data_float.append(float(value))

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
    if global_var.exercise_one:
        plt.title("Reverse Fly ROM Data over Time")
    else:
        plt.title("Rotation ROM Data over Time")

    if global_var.exercise_one:
        plt.savefig('euler_reverse.png')
    else:
        plt.savefig('euler_rotation.png')

    plt.close()
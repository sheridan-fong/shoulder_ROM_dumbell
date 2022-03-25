import serial
import time
import tkinter


# link: https://stackpython.medium.com/today-ive-made-a-really-simple-project-the-main-idea-of-this-project-is-to-build-a-gui-app-to-c5884263971c

collecting = False # data is not collecting unless the start button has been pressed

#  setting up serial communication and the com port
ser = serial.Serial('com7', 9600)  # set up based on baud rate and com port


#  creating functions for changing the state
def quit():
    global tkTop  # creating a global vairable
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button_state():
    collecting = True
    ser.write(bytes('O','UTF-8')) # O for 'ON'



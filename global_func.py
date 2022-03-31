import serial

# ------------- serial monitor -------------
arduinoData = serial.Serial('com6', 115200)

# # -------------- to indicate which graph to show ---------------
# def exercise_one_start():
#     global_var.exercise_one = True
#
# def exercise_two_start():
#     global_var.exercise_one = False
#
# def exercise_page():
#     if global_var.exercise_one:
#         exercise_one_pg
#     elif(global_var.exercise_one != True):
#         exercise_two_pg
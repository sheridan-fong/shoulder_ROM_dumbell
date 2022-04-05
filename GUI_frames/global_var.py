euler_data = []
force_data = []
rom = 0
rom_value_text = "0"
rom_phrase = "You still have quite a \n ways to go,\n but I believe in you"
force_value_text="0"
exercise_one = True


def set_exercise_one_off():
    exercise_one = False
    print(exercise_one)

def set_exercise_one_on():
    exercise_one = True
    print(exercise_one)

# used once the start button has been pressed, it restarts the variables
def data_on():
    global euler_data
    global force_data
    global rom_value_text

    # resetting variables back to default for new collection
    euler_data = []
    force_data = []
    rom_value_text = " "

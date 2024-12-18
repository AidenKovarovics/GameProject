
from Level1 import level_one
from Level2 import level_two
from Level3 import end_screen
from StartScreen import start_screen
from InstructionScreen import show_instructions


# Track the current level
current_level = 0

while True:
    if current_level == 0:
        result = start_screen()
        if result == False:
            current_level = 1
    elif current_level == 1:
        result = show_instructions()
        if result == False:
            current_level = 2

    elif current_level == 2:
        result = level_one()
        if result == True:
            current_level = 3
        elif result == "restart":
            continue  # Restart level one

    elif current_level == 3:
        result = level_two()
        if result == "restart":
            continue  # Restart level two
        elif result == True:
            current_level = 4

    elif current_level == 4:
        result = end_screen()


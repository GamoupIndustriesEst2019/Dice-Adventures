import os, sys
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/start')
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/other')
from other import choice_detect
from start import global_variables

def kitchen_interaction():
    if global_variables.pocket_knife_counter == 1:
        kitchen_interact = input("Usable commands are: n, s, check fridge, get knife:")
    else:
        kitchen_interact = input("Usable commands are: n, s, fridge:")
    choice_detect.choice_kitchen()

def kitchen_description():
    os.system('cls')
    if global_variables.pocket_knife_counter == 1:
        print(
        "Location: Kitchen\n\n\n\n"


        
        "You are in a kitchen. There is a pocket knife on the counter.\n"
        "There is also a refrigerator. Unfortunately, there is no table.\n"
        "To the north of the kitchen, there is a living room, and Tristan's\n"
        "room is to the south.\n\n"

        "What will you do?"
        )
    else:
        "Location: Kitchen\n\n\n\n"


        
        "You are in a kitchen.\n"
        "There is a refrigerator. Unfortunately, there is no table.\n"
        "To the north of the kitchen, there is a living room, and Tristan's\n"
        "room is to the south.\n\n"

        "What will you do?"
    kitchen_interaction()

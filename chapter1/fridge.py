import os, sys
def fridge_interaction():
    if get_milk == True:
        fridge_interact = input("Usable commands are: get bread, out")
        if get_bread == True:
            fridge_interact = input("Usable commands are: out")
    elif get_bread == True:
        fridge_interact = input("Usable commands are: get milk, out")
    else:
        fridge_interact = input("Usable commands are: get bread, get milk, out")
            

def fridge():
    if get_milk == True:
        print(
            "Location: Refrigerator\n\n\n\n"
            "You are looking in a refrigerator.\n"
            "There is 5 slices of bread in here.\n\n"
            "What do you do?"
            )
        if get_bread == True:
            print(
                "Location: Refrigerator\n\n\n\n"
                "You are looking in a refrigerator.\n"
                "There is nothing in here.\n\n"
                "What do you do?"
                )
    elif get_bread == True:
        print(
        "Location: Refrigerator\n\n\n\n"
        "You are looking in a refrigerator.\n"
        "There is a milk carton in here.\n\n"
        "What do you do?"
            )
    else:
        print(
        "Location: Refrigerator\n\n\n\n"
        "You are looking in a refrigerator.\n"
        "There is 5 slices of bread and a milk carton"
        "in here.\n\n"
        "What do you do?"
            )
    fridge_interaction()

import os, sys
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/chapter1')
from chapter1 import kitchen, fridge, tristan_room, living_room, frontyard, backyard, shed, shed_outside, trail, trail_end, camp

def title_choice_detect():
    if title_screen.title_choice == 's' or title_screen.title_choice == 'start':
        dream.dream_scene()
    elif title_screen.title_choice == 'l' or title_screen.title_choice == 'load':
        load.load_file()
    elif title_screen.title_choice == 'q' or title_screen.title_choice == 'quit':
        quit()
    else:
        os.system('cls')
        title_screen.title()

def choice_kitchen():
    if kitchen.kitchen_interact == 'n' or kitchen.kitchen_interact == 'north':
        living_room.living_room()
    elif kitchen.kitchen_interact == 's' or kitchen.kitchen_interact == 'south':
        tristan_room.tristan_room()
    elif kitchen.kitchen_interact == 'check fridge':
        fridge.fridge()
    elif kitchen.kitchen_interact == 'get knife':
        global item_get_id
        item_get_id = "xx"
        item_get.item_get()
def choice_living_room():
    pass
def choice_fridge():
    pass
def choice_tristan_room():
    pass
def choice_backyard():
    pass
def choice_frontyard():
    pass
def choice_shed_outside():
    pass
def choice_shed():
    pass
def choice_trail():
    pass
def choice_trail_end():
    pass
def choice_camp():
    pass

import msvcrt as ms, os, sys
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/chapters/chapter1')
from chapter1 import kitchen
def wakeup_scene():
    os.system('cls')
    print("Jord wakes up in the kitchen.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Tristan: Well, look who's awake!")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Jordan: Since when did I wake up in the kitchen?!")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("GGF: You passed out after you got what seemed like a drink of water, which was actually a Sleep Tonic.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Jordan: Tristan, I remember what happened, but I'd rather not say.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Tristan: Oh, I was just seeing if you were alright.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Tristan: Anyways, I'll be in my room. See ya!")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    print("You are now in Chapter 1! Press 1 to continue.")
    key_press = ms.getch()
    while key_press != b'1':
        key_press = ms.getch()
        if key_press == b'1':
            break
    kitchen.kitchen_description()

import msvcrt as ms, os, sys
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/start')
from start import wakeup
def dream_scene():
    os.system('cls')
    print("You hear a voice far in the distance.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("???: Hello, there.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Jordan: Who are you?")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("???: I'm your great-grandfather.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Jordan: Hey, I remember you! You died when I was 2!")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("GGF: And I'm a spirit to assist you in your journey!")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Jordan: Journey? What journey?")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("GGF: Don't you have to go on a walk with Bandit?")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    os.system('cls')
    print("Jordan: Aw, shoot! See ya, pops!")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    wakeup.wakeup_scene()

import msvcrt as ms, sys
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/start')

from start import title_screen

def command_beginning():
    print("Use (help) outside of battle to see the available commands.")
    print("Use (menu) outside of battle to access the menu.")
    print("Press enter to continue within dialogue.")
    key_press = ms.getch()
    while key_press != b'\r':
        key_press = ms.getch()
        if key_press == b'\r':
            break
    title_screen.title()

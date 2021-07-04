import os, sys
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/start')
sys.path.insert(0, '/Downloads/ZWMC/games/Dice Adventures/other')
from start import global_variables
from other import choice_detect

def title_select():
    global title_choice
    title_choice = input("Type (s)tart, (l)oad, or (q)uit.")
    choice_detect.title_choice_detect()

def title():
    os.system('cls')
    print("                  DDDD ", "IIIII", " CCC ", "EEEEE")
    print("                  D   D", "  I  ", "C   C", "E    ")
    print("                  D   D", "  I  ", "C    ", "EEEEE")
    print("                  D   D", "  I  ", "C   C", "E    ")
    print("                  DDDD ", "IIIII", " CCC ", "EEEEE")
    print()
    print(" AAA ", "DDDD ", "V   V", "EEEEE", "N   N", "TTTTT", "U   U", "RRRR ", "EEEEE", " SSSS")
    print("A   A", "D   D", "V   V", "E    ", "NN  N", "  T  ", "U   U", "R   R", "E    ", "S    ")
    print("AAAAA", "D   D", "V   V", "EEEEE", "N N N", "  T  ", "U   U", "RRRR ", "EEEEE", " SSS ")
    print("A   A", "D   D", " V V ", "E    ", "N  NN", "  T  ", "U   U", "R   R", "E    ", "    S")
    print("A   A", "DDDD ", "  V  ", "EEEEE", "N   N", "  T  ", " UUU ", "R   R", "EEEEE", "SSSS ")
    title_select()

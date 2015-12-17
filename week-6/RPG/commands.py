from character import Character
from random import randint

player = Character()


def new_game():
    player.name = input('Give me your name: ')
    print(player.name)
    input('Press enter to continue')

def load():
    print("load")

def save_and_exit():
    print("save_and_exit")
    exit()# save function!

def enter_submenu():
    print("submenu")

def exit():
    pass

# ---------------- name menu commands -----------------
def continue_game():
    print('continue_game')

def save():
    print('save_and_exit')

def quit():
    pass
# ---------------- roll_stat menu commands -----------------
def roll_stat():
    print()
    player.hp = randint(1,6) + randint(1,6) + 12
    player.dexterity = randint(1,6) + 6
    player.luck = randint(1,6) + 6
    print(player)

# ---------------- potion_menu menu commands -----------------
def potion(x):
    selection = int(input('Please choose an option: '))
    if selection == 1:
        print('Potion of Health')
    elif selection == 2:
        print('Potion of Dexterity')
    elif selection == 3:
        print('Potion of Luck')
    else:
        print('else ag')

# ---------------- potion_menu menu commands -----------------

def fight():
    

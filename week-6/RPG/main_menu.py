from menu import MenuItem
from menu import Menu
from commands import *

def main():
    main_items = Menu([
            MenuItem(1, 'New Game', name_m),
            MenuItem(2, 'Load Game', load),
            MenuItem(3, 'Save and Exit', save_and_exit)
            ])
    main_items.print_menu()
    main_items.choose()

# ---------------- name menu  ----------------
def name_m():
    new_game()
    name_items = Menu([
            MenuItem(1, 'Reenter name', name_m),
            MenuItem(2, 'Continue', roll_stat_menu),
            MenuItem(3, 'Save', save),
            MenuItem(4, 'Quit', quit)
            ])
    name_items.print_menu()
    name_items.choose()

# ---------------- name menu  ----------------
def roll_stat_menu():
    roll_stat(player)
    name_items = Menu([
            MenuItem(1, 'reroll_stat', roll_stat_menu),
            MenuItem(2, 'Continue', potion_select_menu),
            MenuItem(3, 'Save', save),
            MenuItem(4, 'Quit', save)
            ])
    name_items.print_menu()
    name_items.choose()

# ---------------- potion menu  ----------------
def potion_select_menu():

    name_items = Menu([
            MenuItem(1, 'Potion of Health', lambda: potion_menu(1)),
            MenuItem(2, 'Potion of Dexterity', lambda: potion_menu(2)),
            MenuItem(3, 'Potion of Luck', lambda: potion_menu(3)),
            ])
    name_items.print_menu()
    name_items.choose()

def potion_menu(selection):
    print() #empty line
    if selection == 1: print('choosed pitoion: Potion of Health')
    elif selection == 2: print('choosed pitoion: Potion of Dexterity')
    elif selection == 3: print('choosed pitoion: Potion of Luck')
    else: print('else ag')

    name_items = Menu([
            MenuItem(1, 'Reselect the Potion', potion_select_menu),
            MenuItem(2, 'Continue', begin_menu),
            MenuItem(3, 'Quit', quit),
            ])
    name_items.print_menu()
    name_items.choose()

# ---------------- begin menu  ------------------
def begin_menu():
    print(player)
    roll_stat(opponent)

    name_items = Menu([
            MenuItem(1, 'Begin', fight_menu),
            MenuItem(2, 'Save', save),
            MenuItem(3, 'Quit', quit),
            ])
    name_items.print_menu()
    name_items.choose()

# ---------------- fight menu  ------------------
def fight_menu():
    print("Test your Sword in a test fight")
    print(player)
    print(opponent)
    name_items = Menu([
            MenuItem(1, 'Strike', strike_menu),
            MenuItem(2, 'Retreat', save),
            MenuItem(3, 'Quit', quit),
            ])
    name_items.print_menu()
    name_items.choose()

# ---------------- strike menu  ------------------
def strike_menu():
    roll_cube(player)
    roll_cube(opponent)

    if player.roll > opponent.roll:
        print(player)
        print(opponent)
        print('You hits monster')
        opponent.hp -= 2
        print(player)
        print(opponent)

    else:
        print(player)
        print(opponent)
        print('Monster hits you')
        player.hp -= 2
        print(player)
        print(opponent)

    name_items = Menu([
            MenuItem(1, 'Try your luck', try_your_luck_menu),
            MenuItem(2, 'Retreat', strike_menu),
            MenuItem(3, 'Quit', quit),
            ])
    name_items.print_menu()
    name_items.choose()

# ---------------- Try your luck menu  ------------------
def try_your_luck_menu():
    luck_roll = randint(1,6) + randint(1,6)
    if player.luck > luck_roll:
        if player.roll < opponent.roll:
            player.hp -= 2
        else:
            opponent.hp -= 1
    else:
        if player.roll < opponent.roll:
            player.hp -= 1
        else:
            opponent.hp -= 4

    print(player)
    print(opponent)


if __name__ == "__main__": main()

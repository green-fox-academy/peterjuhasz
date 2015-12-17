from menu import MenuItem
from menu import Menu
from commands import *

def sub_m():
    main_items = Menu([
            MenuItem(1, 'sub item1', new_game),
            MenuItem(2, 'sub item1', load),
            MenuItem(0, 'sub item1', save_and_exit)
            ])
    main_items.print_menu()
    main_items.choose()

if __name__ == "__main__": sub_m()

from commands import *

class Menu_basic:
    def __init__(self, menu_items = []):
        self.menu_items = menu_items

    def print_menu(self):
        for i, item in enumerate(self.menu_items):
            print(i+1, item[0])

    def get_menu(self):
        selected_item = int(input("please choose a menu:  ")) - 1
        commands_func = self.menu_items[selected_item][1]
        return commands.commands_func()

def main():

menu_items = [
        {'Name': 'New Game',  'func':'new_game'}
        {'Name': 'Load', 'func': 'load'},
        {'Name': 'Save and Exit', 'func':'save_and_exit'}
]

main_menu = Menu_basic()

if __name__ == "__main__": main()

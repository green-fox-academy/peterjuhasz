import commands

class Menu_basic():
    def __init__(self, menu_items = []):
        self.menu_items = menu_items

    def print_menu(self):
        for i, item in enumerate(self.menu_items):
            print(i+1, item)

    def get_menu(self):
        menu_index = int(input("please choose a menu:  ")) - 1
        return menu_index

class Menu_functions():
    def __init__(self):
        pass

def main():
    menu_starting_items = ["New Game", "Load", "Save and Exit"]
    main_menu = Menu_basic(menu_starting_items)
    main_menu.print_menu()
    main_menu.get_menu()

if __name__ == "__main__": main()

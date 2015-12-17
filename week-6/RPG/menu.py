class Menu:
    def __init__(self, items = []):
        self.items = items

    def screen_clear(self):
        print() #print("\033c")

    def print_menu(self):
        self.screen_clear()
        for item in self.items:
            print(item)

    def choose(self, number = 0):
        number = int(input('Please choose an option: '))
        try:
            if type(number) == str or number > len(self.items):
                raise ValueError
        except ValueError:
            print('You entered a wrong value.')
            self.choose()

        for item in self.items:
            if item.num == number:
                return item.func()

class MenuItem:
    def __init__(self, num, name, func):
        self.num = num
        self.name = name
        self.func = func

    def __repr__(self):
        return '{} {}'.format(self.num, self.name)

import commands
import sys
csv_input = "todo_list.csv"
csv_complete = "complete_list.csv"

def menu():
    print("\033c")
    print('*************************************')
    print('* * *       1 List items        * * *')
    print('* *         2 Add nem item        * *')
    print('*           3 Remove item           *')
    print('* *         4 Complete Item       * *')
    print('* * *       Q Exit Program      * * *')
    print('*************************************')

    choosen = input("Choose an option: ")

    if choosen == '1':
        print()
        print("\033c")
        commands.list_items(csv_input)
        input('For main menu hit enter ')
        menu()
    elif choosen == '2':
        commands.add_new()
        commands.list_items(csv_input)
        input('For main menu hit enter ')
        menu()
    elif choosen == '3':
        commands.remove_item()
        print()
        commands.list_items(csv_input)
        input('For main menu hit enter ')
        menu()
    elif choosen == '4':
        commands.list_items(csv_input)
        commands.make_complete()
        commands.list_items(csv_input) #???!
        commands.list_items(csv_complete)
        input('For main menu hit enter ')
        menu()
    elif choosen.upper() == 'Q':
        pass


menu()

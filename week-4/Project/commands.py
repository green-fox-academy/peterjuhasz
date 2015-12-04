import sys
import csv
import time

import sys
from colors import red, green, yellow

from datetime import datetime

csv_input = "todo_list.csv"
csv_complete  = "complete_list.csv"

def list_items(csvfile):
    my_todo = open(csvfile, "r")
    lines = csv.reader(my_todo, delimiter = "|")

    print(' Priority:  Description:       Deadline: '  )
    for index, line in enumerate(lines):
        print()
        pr_color = line[0] # szinezéshez
        if line[0] == "  High   ":
            print(index+1, red(line[0]), line[1], line[2])
        elif line[0] == " Medium  ":
            print(index+1, yellow(line[0]), line[1], line[2])
        else:
            print(index+1, line[0], line[1], line[2])

    print()
    print()
    my_todo.close()

# list_items()

def add_new():
    with open(csv_input, "a") as csvfile:
        # new = input('Add meg az új elemet: ')
        lines = csv.writer(csvfile, delimiter = "|")
        # status = 'active'
        priority = input('Coose a priority: H - High, M - Medium, L - Low: ').upper()
        if priority == 'H':
            priority_mod = "  High   "
        elif priority == 'M':
            priority_mod = " Medium  "
        elif priority == 'L':
            priority_mod = "  Low    "
        else:
            priority_mod = " Medium  "

        description = input('Give the description: ')
        deadline = input('Please give the deadline: ')
        date = datetime.now().strftime('%d/%m/%Y %H:%M')

        data = [ priority_mod, description, deadline, date]
        lines.writerow(data)


# add_new()

def remove_item():
    #open list
    my_todo = open(csv_input, "r")
    lines = list(csv.reader(my_todo, delimiter = "|"))
    list_items(csv_input) # print actual list
    rm = int(input('Which one do you want to delete? Give a number: '))

    # fill temp list
    temp_list = list(lines)

    print() #empty line
    print('Are you sure? Y/N:')
    print(temp_list[rm-1])
    yes = input('')
    if yes == 'y':
        temp_list.remove(temp_list[rm-1])
        with open(csv_input, "w") as csvfile:
            lines = csv.writer(csvfile, delimiter = "|")
            for line in temp_list:
                lines.writerow(line)
            print("\033c")
            print('Remove completed')
    elif yes == 'n':
        print('Remove aborted')
    else:
        print('')

def make_complete():
        my_todo = open(csv_input, "r")
        lines = list(csv.reader(my_todo, delimiter = "|"))
        rm = int(input('Which one is complete? '))
        temp_list = list(lines)

        print() #empty line
        print('Are you sure? Y/N:')
        print(temp_list[rm-1])
        yes = input('')

        if yes == 'y':
            # add item to the comlete list csv
            with open(csv_complete, "a") as csvfile:
                lines = csv.writer(csvfile, delimiter = "|")
                lines.writerow(temp_list[rm-1])

            temp_list.remove(temp_list[rm-1])
            with open(csv_input, "w") as csvfile:
                lines = csv.writer(csvfile, delimiter = "|")

                for line in temp_list:
                    lines.writerow(line)

                print("\033c") #screen clr
                print('Todo is completed')

        elif yes == 'n':
            print('Abort')
        else:
            print('')





























# make_complete()

# remove_item()
# my_todo = open(csv_input, "r")
# lines = csv.reader(my_todo, delimiter = "|")
# print(list(lines)[2])



# list_items()
# rm = int(input('Melyiket szeretnéd törölni? Adj meg egy számot: '))




#     lines.append(item+'\n')
#
#     my_todo.write("\n")
#     my_todo.write(item_str)
#
#
#
# teszt = open(csv_input, "a")
# teszt.write('alma'+'\n')



# alist.remove(alist[input])
#
# my_todo = open(csv_input, "r")
# lines = csv.reader(my_todo, delimiter = "|")
# my_todo.close()
# print(lines)
#
# lines.append('hello'+'\n')
# f =  open('todo_list.txt', 'w')
# f.write("".join(lines))



# lines_new = lines.append('csá\n')

# print(lines)

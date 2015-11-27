
sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,5,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,7,2,8,4],
          [0,0,0,4,1,9,0,3,5],
          [0,0,0,0,8,0,0,7,9]]

compare_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

check_list = []
def correct_check_list():
    pass

def zero_rowindexes(row):
    zeros_indexes_in_row = []
    for i in range(len(sudoku[row])):
        if sudoku[row][i] == 0:
            zeros_indexes_in_row.append(i)
    return zeros_indexes_in_row

# print(zero_rowindexes(0))
#-----------collect numbers fom row------------------
def collect_numbers_row(row):
    collected_numbers_in_row = []
    for i in range(len(sudoku[row])):
        if sudoku[row][i] != 0:
            collected_numbers_in_row.append(sudoku[row][i])
    return collected_numbers_in_row

# print(collect_numbers_row(0))

# -----------collect numbers from Column---------------
def collect_numbers_column(column):
    collected_numbers_in_column = []
    for i in range(len(sudoku[column])):
        if sudoku[i][column] != 0:
            collected_numbers_in_column.append(sudoku[i][column])
    return collected_numbers_in_column

# print(collect_numbers_column(0))

def collect_numbers_square(row,column):
#  select sarting row position
    if row < 3:
        s_row = 0
    elif row < 6:
        s_row = 3
    else:
        s_row = 6

#  select sarting column position
    if column < 3:
        s_column = 0
    elif column < 6:
        s_column = 3
    else:
        s_column = 6

    square_column = 0
    collected_numbers_in_square = []
    while square_column < 3 :
        for r in range(len(sudoku[:3])):
            if sudoku[s_row][s_column+r] != 0:
                collected_numbers_in_square.append(sudoku[s_row][s_column+r])
        s_row += 1
        square_column += 1
    return collected_numbers_in_square

# print(collect_numbers_square(7,9))

# -----------------------------------------------------------
# 1. sor első nulla eleméhez tartozó számok számok
###################################################
#-------------------LAYER 2.-----------------------
###################################################
def collect_numbers_for_zero(row, column):

    a = collect_numbers_column(column)
    # print (a)

    b = collect_numbers_row(row)
    # print (b)

    c = collect_numbers_square(row, column)
    # print (c)

    all_number_for_zero = a + b + c
    # print(all_number_for_zero)

    # print( "the missing numbers are: ")
    missing_numbers=(set(compare_list) - set(all_number_for_zero))
    # print(missing_numbers)

    return len(set(all_number_for_zero)) #remove duplicates

# 1. sor első nulla eleméhez tartozó számok számok
def missing_numbers(row, column):

    a = collect_numbers_column(column)
    # print (a)

    b = collect_numbers_row(row)
    # print (b)

    c = collect_numbers_square(row, column)
    # print (c)

    all_number_for_zero = a + b + c
    # print(all_number_for_zero)

    # print( "the missing numbers are: ")
    missing_number=(set(compare_list) - set(all_number_for_zero))
    print(missing_numbers)

    return missing_number #remove duplicates


# print (collect_numbers_for_zero(0, 0))

###################################################
#-------------------LAYER 3.-----------------------
###################################################
row = 0
column = zero_rowindexes(0)[0]

while row < 9:
    zero_value = []
    # row_zero_value = []
    for r in range(len(zero_rowindexes(row))):
        zero_value.append(collect_numbers_for_zero(row, zero_rowindexes(row)[r]))
    row += 1
    print (zero_value)

# print(collect_numbers_for_zero(0,2))


row = 0
column = zero_rowindexes(0)[0]

while row < 9:
    zero_value = []
    # row_zero_value = []
    for r in range(len(zero_rowindexes(row))):
        if (collect_numbers_for_zero(row, zero_rowindexes(row)[r])) = 8;
            sudoku[row][column] =
    row += 1
    print (zero_value)

print(missing_numbers(7, 7))
sudoku[0][0]= int(missing_numbers(7, 7))

print(zero_rowindexes(0,sudoku))
print(zero_rowindexes(1,sudoku))
print(zero_rowindexes(2,sudoku))
print(zero_rowindexes(3,sudoku))
print(zero_rowindexes(4,sudoku))
print(zero_rowindexes(5,sudoku))
print(zero_rowindexes(6,sudoku))
print(zero_rowindexes(7,sudoku))
print(zero_rowindexes(8,sudoku))



####

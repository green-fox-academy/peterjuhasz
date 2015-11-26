
sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

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

def collect_numbers_square(row):


    square_column=0
    collected_numbers_in_square = []
    while square_column < 3 :
        for r in range(len(sudoku[:3])):
            if sudoku[row][r] != 0:
                collected_numbers_in_square.append(sudoku[row][r])
        row += 1
        square_column +=1
    return collected_numbers_in_square


print(collect_numbers_square(0))
# -----------------------------------------------------------
# 1. sor első nulla eleméhez tartozó számok számok

# collect items for zeros
# def collect_numbers_for_zero(column, row):
#
#     a = collect_numbers_column(column)
#     print (a)
#     b = collect_numbers_square(row)
#     print (b)
#     # c = collect_numbers_square(square_nr)
#     # print (c)
#     mind = a + b
#     print(mind)
#     return mind
#
# print (collect_numbers_for_zero(0, 0))

# temp_list = []
# for item in range(sudoku[1])
#     pass

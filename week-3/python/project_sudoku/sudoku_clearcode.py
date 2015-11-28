
sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# to compare printed result:
sudoku_basic = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# to remove duplicates
compare_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

###################################################
#-------------------LAYER 1.-----------------------
###################################################
def zero_rowindexes(row, matrix):
    zeros_indexes_in_row = []
    for i in range(len(matrix[row])):
        if matrix[row][i] == 0:
            zeros_indexes_in_row.append(i)
    return zeros_indexes_in_row

#-----------collect numbers fom row----------------
def collect_numbers_row(row, matrix):
    collected_numbers_in_row = []
    for i in range(len(matrix[row])):
        if matrix[row][i] != 0:
            collected_numbers_in_row.append(matrix[row][i])
    return collected_numbers_in_row

# -----------collect numbers from Column-----------
def collect_numbers_column(column, matrix):
    collected_numbers_in_column = []
    for i in range(len(matrix[column])):
        if matrix[i][column] != 0:
            collected_numbers_in_column.append(matrix[i][column])
    return collected_numbers_in_column

def collect_numbers_square(row,column, matrix):
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

    # collect the numbers from square
    square_column = 0
    collected_numbers_in_square = []
    while square_column < 3 :
        for r in range(len(matrix[:3])):
            if matrix[s_row][s_column+r] != 0:
                collected_numbers_in_square.append(matrix[s_row][s_column+r])
        s_row += 1
        square_column += 1
    return collected_numbers_in_square

###################################################
#-------------------LAYER 2.-----------------------
###################################################

#--------------- collect numbers ------------------
def collect_numbers_for_zero(row, column, matrix):

    a = collect_numbers_column(column, matrix)
    b = collect_numbers_row(row, matrix)
    c = collect_numbers_square(row, column, matrix)

    all_number_for_zero = a + b + c

    return len(set(all_number_for_zero))

#------------------ missing numbers ---------------
def missing_numbers(row, column, matrix):

    a = collect_numbers_column(column, matrix)
    b = collect_numbers_row(row, matrix)
    c = collect_numbers_square(row, column, matrix)

    all_number_for_zero = a + b + c

    #remove duplicates with compared list(defined at the beginning)
    missing_number=(set(compare_list) - set(all_number_for_zero))

    return missing_number

#------------------ print function ----------------
def matrix_print(a):

    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    print(a[5])
    print(a[6])
    print(a[7])
    print(a[8])
    print('\n')

###################################################
#-------------------LAYER 3.-----------------------
###################################################
def optimum_list(row, matrix):
    # Print the priority for the zeros
    row = 0
    while row < 9:
        zero_value = []
        row_zero_value = []
        for r in range(len(zero_rowindexes(row,matrix))):
            zero_value.append(collect_numbers_for_zero(row, zero_rowindexes(row, matrix)[r], matrix))
        row += 1
        print (zero_value)
    return(zero_value)
# optimum_list(1, sudoku)

def solution(matrix):

    row = 0
    run = 0
    while row < 9:

        change = 0
        szam = 0
        r = 0
        while r < len(zero_rowindexes(row, matrix)):
            if collect_numbers_for_zero(row, zero_rowindexes(row, matrix)[r], matrix) == 8:

                # just to keep it simple :D :D
                sudoku[row][zero_rowindexes(row, matrix)[r]] = (missing_numbers(row, zero_rowindexes(row, matrix)[r], matrix)).pop()

                #-#-#-#-#-#-#---the 3 lines below is equivalent with the one above--#-#-#-#-#-#-#
                #
                # ---------- check the missing number in th current position --------------------
                # szam = missing_numbers(row, zero_rowindexes(row, matrix)[r], matrix)
                #
                # ---------- pop it from the set ------------------------------------------------
                # change = (szam.pop())
                #
                # ---------- paste it to the matrix ---------------------------------------------
                # sudoku[row][zero_rowindexes(row, matrix)[r]] = change
                #
                #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

                #-------------------to see the steps--------------------
                # matrix_print(sudoku)
                # input("pause")
                #-------------------------------------------------------
            else:
                r += 1
        row += 1
    return sudoku

# -----------------------Magic------------------------------
# check if there are more zeros
def is_solved(matrix):
    for n in range(len(matrix)):
        for i in range(len(matrix[n])):
            if matrix[n][i] == 0:
                return False
    return True

# run solution until finish sudoku
while is_solved(sudoku) == False:
    sudoku = solution(sudoku)
# --------------------Print Results-------------------------
print('\n')
print ("Sudoku start:")
matrix_print(sudoku_basic)
print ("Solved:")
matrix_print(sudoku)

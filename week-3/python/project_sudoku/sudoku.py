
sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku_mod = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


compare_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def zero_rowindexes(row, matrix):
    zeros_indexes_in_row = []
    for i in range(len(matrix[row])):
        if matrix[row][i] == 0:
            zeros_indexes_in_row.append(i)
    return zeros_indexes_in_row
# print(zero_rowindexes(0, sudoku))

#-----------collect numbers fom row------------------
def collect_numbers_row(row, matrix):
    collected_numbers_in_row = []
    for i in range(len(matrix[row])):
        if matrix[row][i] != 0:
            collected_numbers_in_row.append(matrix[row][i])
    return collected_numbers_in_row
# print(collect_numbers_row(0, sudoku))

# -----------collect numbers from Column---------------
def collect_numbers_column(column, matrix):
    collected_numbers_in_column = []
    for i in range(len(matrix[column])):
        if matrix[i][column] != 0:
            collected_numbers_in_column.append(matrix[i][column])
    return collected_numbers_in_column
# print(collect_numbers_column(0,sudoku))

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

    square_column = 0
    collected_numbers_in_square = []
    while square_column < 3 :
        for r in range(len(matrix[:3])):
            if matrix[s_row][s_column+r] != 0:
                collected_numbers_in_square.append(matrix[s_row][s_column+r])
        s_row += 1
        square_column += 1
    return collected_numbers_in_square
# print(collect_numbers_square(7,9,sudoku))

###################################################
#-------------------LAYER 2.-----------------------
###################################################
def collect_numbers_for_zero(row, column, matrix):

    a = collect_numbers_column(column, matrix)
    # print (a)

    b = collect_numbers_row(row, matrix)
    # print (b)

    c = collect_numbers_square(row, column, matrix)
    # print (c)

    all_number_for_zero = a + b + c
    # print(all_number_for_zero)

    # print( "the missing numbers are: ")
    missing_numbers=(set(compare_list) - set(all_number_for_zero))
    # print(missing_numbers)

    return len(set(all_number_for_zero)) #remove duplicates

# print(collect_numbers_for_zero(0, 0, sudoku))

#------------------ missing numbers --------------------
def missing_numbers(row, column, matrix):

    a = collect_numbers_column(column, matrix)
    # print (a)

    b = collect_numbers_row(row, matrix)
    # print (b)

    c = collect_numbers_square(row, column, matrix)
    # print (c)

    all_number_for_zero = a + b + c
    # print(all_number_for_zero)

    # print( "the missing numbers are: ")
    missing_number=(set(compare_list) - set(all_number_for_zero)) #remove duplicates
    print(missing_numbers)

    return missing_number
# print (missing_numbers(7, 7, sudoku))

def matrix_print(a):
    print('\n')
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    print(a[5])
    print(a[6])
    print(a[7])
    print(a[8])

###################################################
#-------------------LAYER 3.-----------------------
###################################################
def wtf_length(row, matrix):
    # Print the priority for the zeros
    row = 0 # ne kommenteld ki, mert a lenti is használja
    while row < 9:
        zero_value = []
        row_zero_value = []
        for r in range(len(zero_rowindexes(row,matrix))):
            zero_value.append(collect_numbers_for_zero(row, zero_rowindexes(row, matrix)[r], matrix))
        row += 1
        # print (zero_value)
    return(zero_value)
    # Print the priority for the zeros
# wtf_length(1, sudoku)

def solution(matrix):
    row = 0
    column = zero_rowindexes(0, matrix)[0]
    run=0
    while row < 9:
        change = 0
        r = 0
        while r < len(zero_rowindexes(row, matrix)):
            if collect_numbers_for_zero(row, zero_rowindexes(row, matrix)[r], matrix) == 8:

                #----------------------debug----------------------------
                # print("if condition:")
                # print(collect_numbers_for_zero(row, zero_rowindexes(row, matrix)[r], matrix))
                #
                # print("zero_rowindexes aktuális")
                # print(zero_rowindexes(row, matrix)[r])
                #
                # print("zero_rowindexes hossza r-hez képest")
                # print(len(zero_rowindexes(row, matrix)))
                #
                # print(zero_rowindexes(0,matrix))
                # print(zero_rowindexes(1,matrix))
                # print(zero_rowindexes(2,matrix))
                # print(zero_rowindexes(3,matrix))
                # print(zero_rowindexes(4,matrix))
                # print(zero_rowindexes(5,matrix))
                # print(zero_rowindexes(6,matrix))
                # print(zero_rowindexes(7,matrix))
                # print(zero_rowindexes(8,matrix))
                #
                # print("zero_rowindexes következő")
                # print(zero_rowindexes(row, matrix)[r+1])
                #
                #
                # print("zero_rowindexes(row, matrix)[r]")
                #
                #----------------------debug----------------------------
                # print("mukodik")
                # a = zero_rowindexes(row, matrix)[r]
                # b = missing_numbers(row, a, matrix)
                # print(b)
                print(missing_numbers(row, zero_rowindexes(row, matrix)[r], matrix) ) #nyomtasd ki a
                change = int(input("ha cserélni szeretnél írd be a számot:"))
                sudoku_mod[row][zero_rowindexes(row, matrix)[r]] = change
                matrix_print(sudoku_mod)
                change = 0
            r += 1
        row += 1
    # matrix_print(sudoku)
    return sudoku_mod

# --------------------Magic-------------------------
solution(solution(solution(solution(solution(solution(solution(solution(solution(solution(sudoku))))))))))



# while (not ( is_solved(sudoku)):
#     sudoku = solution (sudoku)
#
# solve():
#
#     if (is_solved(s) ):
#         return sudok
#     else:
#         return solve( )

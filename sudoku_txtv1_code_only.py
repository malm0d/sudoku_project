# board = [
#------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
#------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
#------------------------------
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
# [0, 1, 2, 3, 4, 5, 6, 7, 8],
#------------------------------
# ]
#Navigate Sudoku board by board[row][column]
#Vertical lines to separate after board[row][2]; and horizontal lines to separate after board[2]
#Vertical and horizontal lines to define the 9units x 9units Sudoku grid (81 squares total)
sudoku_board = [
    [5, 0, 0, 1, 8, 0, 0, 7, 0],
    [0, 0, 7, 2, 9, 0, 5, 4, 3],
    [0, 0, 0, 0, 0, 4, 0, 0, 1],
    [0, 5, 0, 6, 0, 0, 9, 8, 0],
    [7, 0, 0, 9, 0, 0, 3, 0, 4],
    [0, 9, 6, 3, 0, 8, 2, 1, 5],
    [0, 0, 5, 8, 0, 0, 0, 0, 6],
    [1, 4, 0, 0, 6, 0, 0, 0, 2],
    [0, 3, 0, 0, 2, 7, 1, 0, 0]]     #sample sudoku board, 0 means empty

#Global Constraints:
# One 9x9 global grid with 9 subgrids with 9 sub-subgrids (cells).
# Numbers 1-9 for every row, every column, and every subgrid.
# The solution to the Sudoku board must be globally correct.

#define function that takes a board as an argument and returns a printed
#9x9 board fashioned as a Sudoku board.
def make_board(board):
    for row in range(len(board)):
        if row % 3 == 0:      
            print ("-------------------------")
        for column in range(len(board[row])):
            if column % 3 == 0:
                print ("|", board[row][column], end = " ")        
            elif column == 8:
                print (board[row][column], "|")
            else:
                print (board[row][column], end = " ")
        if row == 8:
            print ("-------------------------")
        else:
            continue


#define function that allows us to locate position of all empty cells,
#by returning a list of coordinates of empty cells.
def find_empty_cells(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                empty_cell = (row, column)
                return empty_cell
    return None


#define function that checks if the solution to the board is globally correct.
#This means, we need to check, for the cell that we are working on, there is harmony across the cell's row.
#We also need to check, for the cell that we are working on,there is harmony down the cell's column.
#And we also need to check, for the cell we are working on, there is harmony within each subgrid that the cell is a part of.
def harmony(board, choice, emptycell_coord):
    #check harmony in row of empty cell::
    for x in range(len(board[0])):
        if board[emptycell_coord[0]][x] == choice and x != emptycell_coord[1]:
            return False


    #check harmony in column of empty cell:                                                           
    for y in range(len(board)):
        if board[y][emptycell_coord[1]] == choice and y != emptycell_coord[0]:
            return False

    #check harmony in subgrid of empty cell:
    subgrid_row = emptycell_coord[0] // 3
    subgrid_column = emptycell_coord[1] // 3

    #subgrid row & col value falls as either: 0, 1, or 2.
    for row in range(subgrid_row * 3, (subgrid_row * 3) + 3):
        for col in range (subgrid_column * 3, (subgrid_column * 3) + 3):
            if board[row][col] == choice and (row, col) != emptycell_coord:
                return False

    return True


#Define fucntion that solves Sudoku board - runs above 3 functions:
def solve_sudoku(board):
    emptycell_location = find_empty_cells(board)
    if emptycell_location is None:
        return True
    else:
        (row, column) = emptycell_location
    for n in range(1, 10):
        if harmony(board, n, emptycell_location) == True:
            board[row][column] = n


            if solve_sudoku(board) == True:
                return True

            board[row][column] = 0
 
    return False



make_board(sudoku_board)
solve_sudoku(sudoku_board)
make_board(sudoku_board)
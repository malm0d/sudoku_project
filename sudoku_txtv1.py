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
            print ("-------------------------")             #prints a horizontal line before row % 3 == 0, which includes topmost border.
        for column in range(len(board[row])):
            if column % 3 == 0:
                print ("|", board[row][column], end = " ")  #prints vertical line before column % 3 == 0; end parameter replaces '\n' with " " so that after board[row][column],...        
            elif column == 8:                               #...the print statement ends on " ", and this allows other iteration variables to append to the print statement.
                print (board[row][column], "|")             #prints board[row][8] and the rightmost border of the sudoku board.
            else:
                print (board[row][column], end = " ")       #for column % 3 != 0, iteration variable will continue to append to the same print statement since '\n' is replaced
        if row == 8:                                        #...with " ". Print statement will not have any '\n' , so more iteration variables can still append to the same statement.
            print ("-------------------------")             #prints lowest border of sudoku board, comes last so row[8] can be populated first.
        else:
            continue


#define function that allows us to locate position of all empty cells,
#by returning a list of coordinates of empty cells.
def find_empty_cells(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:                     #an empty cell is denoted by the integer (neutral) zero.
                empty_cell = (row, column)                  #empty_cell holds the coordinates of an empty cell, as in (row, column), in the form of a Tuple.
                return empty_cell
            return None


#define function that checks if the solution to the board is globally correct.
#This means, we need to check, for the cell that we are working on, there is harmony across the cell's row.
#We also need to check, for the cell that we are working on,there is harmony down the cell's column.
#And we also need to check, for the cell we are working on, there is harmony within each subgrid that the cell is a part of.
def harmony(board, choice, emptycell_coord):                                            #choice argument is the number we want to put in an empty cell. And emptycell_coord argument is a Tuple (row, column).
    #check harmony in row of empty cell::
    for x in range(len(board[0])):                                                      #board has a fixed length, so we can opt for board[0] as every row in the board will yield range(9)->[0,1,..,7,8].
        if board[emptycell_coord[0]][x] == choice and x != emptycell_coord[1]:          #access x-coord of empty cell via index notation: emptycell_coord[0] = row. The second conditional: x != emptycell_coord[1], allows the function to
            return False                                                                #skip checking the empty cell against the empty cell. Since every empty cell will be x == emptycell_coord[1] and the function is going to iterate through the
                                                                                        #entire row, it needs to skip the empty cell and not return False if we just inserted a number into an empty cell and are checking for duplicates in the row. 
                                                                                        #Conditionals will be met if there are duplicates in the row and x is not the column of an empty cell; only then harmony function returns False.
    #check harmony in column of empty cell:                                                           
    for y in range(len(board)):                                                         #yields: [0,1,2,3,4,5,6,7,8], since len(board) is 9. This checks for harmony every column down the nine rows.
        if board[y][emptycell_coord[1]] == choice and y != emptycell_coord[0]:          #access y-coor of empty cell via index notation: emptycell_coord[1] = column. The second conditional: y != emptycell_coord[0], allows the function to 
            return False                                                                #skip checking the empty cell against the empty cell. Every empty cell will be y == emptycell_coord[0], so function needs to be able to skip the empty cell
                                                                                        #and not return False if we just inserted a number into an empty cell. If condtionals are both met, returns False, meaning there is no harmony in the column.
    #check harmony in subgrid of empty cell:
    subgrid_row = emptycell_coord[0] // 3                                   #since there are 3 subgrids row-wise & column-wise, group each row & column into 3 subgrids, and each subgrid is composed of 3 rows and 3 columns.
    subgrid_column = emptycell_coord[1] // 3                                #floor division (//) returns only the quotient (integer) of the division. So, (0 to 2) // 3 = 0; (3 to 5) // 3 = 1; (6 to 8) // 3 = 2.
                                                                            #Subgrids are, starting from top leftmost of Sudoku board (row, column): (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2).
    #subgrid row & col value falls as either: 0, 1, or 2.
    for row in range(subgrid_row * 3, (subgrid_row * 3) + 3):                 #checks subgrid in downwards y direction. For subgrid_row = 0, 1, 2, range = (0, 3), (3, 6), (6, 9) respectively.
        for col in range (subgrid_column * 3, (subgrid_column * 3) + 3):      #checks subgrid in forward x direction. For subgrid_column = 0, 1, 2, range = (0, 3), (3, 6), (6, 9) respectively.
            if board[row][col] == choice and (row, col) != emptycell_coord:   #same as before, we want to skip checking the empty cell against the empty cell, as every empty cell will be (row, col) == emptycell_coord.
                return False

    return True                                                             #if the arguments do not trigger any return False, we know that the current board is valid, globally.


#Define fucntion that solves Sudoku board - runs above 3 functions:
def solve_sudoku(board):                                                    #returns True if board is complete, if not operates to solve the board recursively, via backtracking algorithm.
    emptycell_location = find_empty_cells(board)                            #find_empty_cells(board) takes in a board and scans for empty cells. Returns empty cells as (row, column), and assigns Tuple to the variable emptycell_location.
    if emptycell_location is None:                                          #find_empty_cells(board) returns None if there are no empty cells; if so, all empty cells would be occupied. 
        return True
    else:                                                                   #emptycell_location holds a Tuple (row, column), which is the coordinates of an empty cell.
        (row, column) = emptycell_location                                  #Unpack and assign tuple (row, column) to variables: row = row & column = column, so we can use double index to access value of the empty cell.
    for n in range(1, 10):                                                  #Iteration variable n will take on integers 1-9, so it inserts all possible sudoku-integers as a choice argument for every empty cell. 
        if harmony(board, n, emptycell_location) == True:
            board[row][column] = n                                          #If the choice argument allows harmony function to yield True, it means that the choice argument has met all constraints in
                                                                            #the row, column and subgrid of the sudoku board. Replace the value of the empty cell with the value of the choice argument.
                                                                            #Then we need to recursively try to solve the sudoku board again with the choice argument (n) that we just inserted into the empty cell.
            if solve_sudoku(board) == True:                                 #By calling the solve_sudoku function again, we will look at a NEW empty cell and try to solve the board with the newly inserted choice argument
                return True                                                 #as a dependency for the board to be valid. And if solve_sudoku(board) returns False with the newly inserted choice argument, meaning the next empty cell
                                                                            #cannot find a solution for n = 1-9, it will reset the previous empty cell to be 0 (empty) and then try again with another value of n, for the range of n = 1-9.
            board[row][column] = 0                                          #Note that board[row][column] = 0 refers to the location of the previous empty cell (the one we worked on before calling solve_sudoku the second time).
                                                                            #(board[row][column] = 0 only runs when the last line of the function - 'return False' is executed).    
    return False                                                            #If we loop though all possible sudoku-integers and none of them can return harmony() == True, solve_sudoku will return False, and that means the
                                                                            #solution is not True. Also note, figuratively, the recursive algorithm runs a function within a function, so it has multiple layers of code running at the same time.


make_board(sudoku_board)
solve_sudoku(sudoku_board)
make_board(sudoku_board)
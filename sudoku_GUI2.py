import pygame
import time
pygame.font.init()

#Functions from sudoku_txt: find_empty_cells, harmony, solve_sudoku.

def find_empty_cells(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                empty_cell = (row, column)
                return empty_cell
    return None


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

#--------------------------------------------------------------------------------------------------
#Begin constructing GUI

class Single_Cell:

    rows = 9
    columns = 9
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.temporary_value = 0
        self.selectedcell = False

    def insert_temporary_value(self, value):
        self.temporary_value = value

    def insert_value(self, value):
        self.value = value

    def draw_single_cell(self, screen):
        cell_measuremt = self.width / 9
        cell_x = self.column * cell_measuremt
        cell_y = self.row * cell_measuremt
        gray = (128, 128, 128)
        green = (0, 250, 140)
        white = (255, 255, 255)
        fnt = pygame.font.SysFont("times", 32)

        if self.selectedcell == True:
            pygame.draw.rect(screen, green, (cell_x, cell_y, cell_measuremt, cell_measuremt), 4)

        if self.temporary_value != 0 and self.value == 0:
            text = fnt.render(str(self.temporary_value), True, gray)
            screen.blit(text, (cell_x + 5, cell_y + 5))
        
        elif self.value != 0:
            text = fnt.render(str(self.value), True, white)
            screen.blit(text, (cell_x + (cell_measuremt/2 - text.get_width()/2), cell_y + (cell_measuremt/2 - text.get_height()/2)))

    def draw_outcome(self, screen, outcome):
        aqua = (77, 255, 255)
        fuchsia = (255, 0, 255)
        black = (0, 0, 0)
        white = (255, 255, 255)
        fnt = pygame.font.SysFont("times", 32)
        cell_measuremt = self.width / 9
        cell_x = self.column * cell_measuremt
        cell_y = self.row * cell_measuremt
        pygame.draw.rect(screen, black, (cell_x, cell_y, cell_measuremt, cell_measuremt), 0)

        text = fnt.render(str(self.value), True, white)
        screen.blit(text, (cell_x + (cell_measuremt/2 - text.get_width()/2), cell_y + (cell_measuremt/2 - text.get_height()/2)))

        if outcome == True:
            pygame.draw.rect(screen, aqua, (cell_x, cell_y, cell_measuremt, cell_measuremt), 4)
        else:
            pygame.draw.rect(screen, fuchsia, (cell_x, cell_y, cell_measuremt, cell_measuremt), 4)



class Global_Grid:

    sudoku_board = [
    [5, 0, 0, 1, 8, 0, 0, 7, 0],
    [0, 0, 7, 2, 9, 0, 5, 4, 3],
    [0, 0, 0, 0, 0, 4, 0, 0, 1],
    [0, 5, 0, 6, 0, 0, 9, 8, 0],
    [7, 0, 0, 9, 0, 0, 3, 0, 4],
    [0, 9, 6, 3, 0, 8, 2, 1, 5],
    [0, 0, 5, 8, 0, 0, 0, 0, 6],
    [1, 4, 0, 0, 6, 0, 0, 0, 2],
    [0, 3, 0, 0, 2, 7, 1, 0, 0]]

    def __init__(self, rows, columns, width, height, screen):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.screen = screen
        self.singlecells = [[Single_Cell(self.sudoku_board[row][column], row, column, width, height) for column in range(columns)] for row in range(rows)]
        self.updatedgrid = None
        self.update_board()
        self.selected = None

    def solve_sudoku(self):
        emptycell_location = find_empty_cells(self.updatedgrid)
        if not emptycell_location:
            return True
        else:
            (row, column) = emptycell_location
        for n in range(1, 10):
            if harmony(self.updatedgrid, n, emptycell_location) == True:
                self.updatedgrid[row][column] = n


                if self.solve_sudoku() == True:
                    return True

                self.updatedgrid[row][column] = 0
 
        return False


    def update_board(self):
        self.updatedgrid = [[self.singlecells[row][column].value for column in range(self.columns)] for row in range(self.rows)]
        
    def commit_value(self, value):
        (row, column) = self.selected
        if self.singlecells[row][column].value == 0:
            self.singlecells[row][column].insert_value(value)
            self.update_board()
            
            if harmony(self.updatedgrid, value, (row, column)) and self.solve_sudoku() == True:
                return True

            else:
                self.singlecells[row][column].insert_value(0)
                self.singlecells[row][column].insert_temporary_value(0)
                self.update_board()
                return False

    def clear_cell(self):
        (row, column) = self.selected
        if self.singlecells[row][column].value == 0:
            self.singlecells[row][column].insert_temporary_value(0)

    def sketch_cell(self, value):
        (row, column) = self.selected
        self.singlecells[row][column].insert_temporary_value(value)

    def draw_grid(self):
        white = (255, 255, 255)
        gray = (128, 128, 128)
        cell_width = (self.width / 9)
        for n in range(self.columns + 1):
            if n % 3 == 0:
                line_width = 3
            else:
                line_width = 1
            if line_width == 3:
                pygame.draw.line(self.screen, white, (int((cell_width * n)), 0), (int((cell_width * n)), self.height), line_width)
                pygame.draw.line(self.screen, white, (0, int((cell_width * n))), (self.width, int((cell_width * n))), line_width)
            elif line_width == 1:
                pygame.draw.line(self.screen, gray, (int((cell_width * n)), 0), (int((cell_width * n)), self.height), line_width)
                pygame.draw.line(self.screen, gray, (0, int((cell_width * n))), (self.width, int((cell_width * n))), line_width)
        #draws each cell
        for row in range(self.rows):
            for column in range(self.columns):
                self.singlecells[row][column].draw_single_cell(self.screen)

    def reset_and_select(self, row, column):
        for x in range(self.rows):
            for y in range(self.columns):

                self.singlecells[x][y].selectedcell = False

        self.singlecells[row][column].selectedcell = True
        self.selected = (row, column)

    def user_click(self, position):
        if position[0] < self.width and position[1] < self.height:
            cell_width = (self.width / 9)
            row = int (position[0] // cell_width)
            column = int (position[1] // cell_width)
            return (column, row)
        else:
            return None

    def check_complete(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.singlecells[row][column].value == 0:
                    return False
        return True

    def solve_sudoku_GUI(self):
        emptycell_location = find_empty_cells(self.updatedgrid)
        if not emptycell_location:
            return True
        else:
            (row, column) = emptycell_location
        for n in range(1, 10):
            if harmony(self.updatedgrid, n, emptycell_location) == True:
                self.updatedgrid[row][column] = n
                self.singlecells[row][column].insert_value(n)
                self.singlecells[row][column].draw_outcome(self.screen, True)
                self.update_board()
                pygame.display.update()
                pygame.time.delay(80)

                if self.solve_sudoku_GUI() == True:
                    return True

                self.updatedgrid[row][column] = 0
                self.singlecells[row][column].insert_value(0)
                self.update_board()
                self.singlecells[row][column].draw_outcome(self.screen, False)
                pygame.display.update()
                pygame.time.delay(80)
        return False

def redraw_window(screen, board, time):
    screen.fill((0,0,0))
    # Draw time
    fnt = pygame.font.SysFont("times", 32)
    text = fnt.render("Time: " + format_time(time), True, (255,255,255))
    screen.blit(text, (540 - 160, 560))
    # Draw grid and board
    board.draw_grid()


def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60
    display_time = " " + str(minute) + ":" + str(sec)
    return display_time

def main_window():
    
    screenwidth = 540
    screenheight = 600
    screen = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("Sudoku!")
    board = Global_Grid(9, 9, 540, 540, screen)
    start = time.time()
    key = None
    mainloop = True
    
    #construct pygame events handler:
    while mainloop:
        play_time = round(time.time() - start)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                mainloop = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_BACKSPACE:
                    board.clear_cell()
                    key = None

                if event.key == pygame.K_RETURN:
                    (row, column) = board.selected
                    if board.singlecells[row][column].temporary_value != 0:
                        if board.commit_value(board.singlecells[row][column].temporary_value) == True:
                            print ("Passed.")
                        else:
                            print ("Failed.")
                        key = None

                        if board.check_complete() == True:
                            print ("Sudoku is completed. Thanks for testing the program.")

                if event.key == pygame.K_SPACE:
                    board.solve_sudoku_GUI()
                    print ("Try harder next time.")

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                cell_position = board.user_click(position)
                if cell_position:
                    board.reset_and_select(cell_position[0], cell_position[1])
                    key = None

        if board.selected and key != None:
            board.sketch_cell(key)

        redraw_window(screen, board, play_time)
        pygame.display.update()

main_window()
pygame.quit()


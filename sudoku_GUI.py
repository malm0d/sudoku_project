#Construct and implement GUI for Sudoku solver, using pygame.
import pygame
from sudoku_txtv1 import find_empty_cells, harmony, solve_sudoku
import time
pygame.init()

#Create classes for global grid (9x9), and single cell.
class Global_Grid:

    sudoku_board = [                                    #Adjust board manually if user wants to change the board/difficulty.
    [5, 0, 0, 1, 8, 0, 0, 7, 0],                        #sudoku_board object represents the starting grid of filled cells.
    [0, 0, 7, 2, 9, 0, 5, 4, 3],
    [0, 0, 0, 0, 0, 4, 0, 0, 1],
    [0, 5, 0, 6, 0, 0, 9, 8, 0],
    [7, 0, 0, 9, 0, 0, 3, 0, 4],
    [0, 9, 6, 3, 0, 8, 2, 1, 5],
    [0, 0, 5, 8, 0, 0, 0, 0, 6],
    [1, 4, 0, 0, 6, 0, 0, 0, 2],
    [0, 3, 0, 0, 2, 7, 1, 0, 0]]

    def __init__(self, row, column, width, height):
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.selection = None

    def selection(self, row, column):                       #Define a function that selects a cell.
        for x in range(self.row):
            for y in range(self.column):
                ???


    white = (255, 255, 255)
    gray = (128, 128, 128)                                   #pygame.draw.line(surface, color, start_pos, end_pos, width) -> Rect. start_pos & end_pos receive (x, y) coordinates (as Tuples or List).
    def draw_grid(self, main_window):                        #Draw grid lines. Major grid lines are white, minor grid lines are gray.
        cell_width = (self.width / 9)                        #Divide width into 9 equal cells.
        for n in range(self.column + 1):                     #There are 10 vertical and horizontal lines dividing cells equally, so self.column + 1 includes very last vertical & horizontal line to iterator: [0,1,2,3,4,5,6,7,8,9].
            if n % 3 == 0:                                   #Apply same logic in make_board() function from sudoku_txtv1.py to modulo operations. Thicker lines are n = 0, 3, 6, 9. Thin lines are the remaining n values.
                line_width = 3                               #Default line width = 1.  Width < 1 = nothing will be drawn.
            else:
                line_width = 1
            if line_width == 3:                                                                                               #First vertical and horizontal line: cellwidth*0, last vertical and horizontal line: cellwidth*9.
                pygame.draw.line(main_window, white, ((cell_width * n), 0), ((cell_width * n), self.height), line_width)      #Draws vertical major grid lines, starting from y = 0.
                pygame.draw.line(main_window, white, (0, (cell_width * n)), (self.width, (cell_width * n)), line_width)      #Draws horizontal major grid lines, starting from x = 0.
            elif line_width == 1:
                pygame.draw.line(main_window, gray, ((cell_width * n), 0), ((cell_width * n), self.height), line_width)       #Draws vertical minor grid lines, starting from y = 0.
                pygame.draw.line(main_window, gray, (0, (cell_width * n)), (self.width, (cell_width * n)), line_width)       #Draws horizontal minor grid lines, starting from x = 0.


class Single_Cell:
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width
        self.height = height





def main_window():
    #Construct a visible screen interface:
    screenwidth = 800
    screenheight = 920
    screen = pygame.display.set_mode([screenwidth, screenheight])           #set_mode(size=(0, 0), flags=0, depth=0, display=0) -> set screen size.
    background = pygame.Surface(screen.get_size())                          #Surface((width, height), flags=0, depth=0, masks=None) -> create background surface. #get_size() -> (width, height)
    background.fill((0, 0, 0))                                              #fill(color, rect=None, special_flags=0) -> Rect color = (r, g, b)
    background.convert()                                                    #change the pixel format of an image; convert(Surface=None) -> Surface
    screen.blit(background, (0,0))                                          #background surface is not visible on its own. blit background surface to the screen.
                                                                            #blit(source, dest, area=None, special_flags=0) -> Rect. Upper left corner of 'background' is on position (0, 0) on the screen.
    
    mainloop = True                                                         #mainloop represents pygame window.
    #construct pygame events handler:
#    while mainloop == True:                                                 #If pygame window is still running:
#        for event in pygame.event.get():                                    #get events from the queue, get(eventtype=None) -> Event List
#            if event.type == pygame.QUIT:                                   #if event.type is a QUIT event, uninitialize all pygame modules, 
#                mainloop = False                                            #pygame window closed by user.
#            elif event.type == pygame.KEYDOWN:                              #else & if event.type is a KEYDOWN event, i.e, a key is pressed, set function of pressed keys, using pygame key constants.
#                if event.key == pygame.K_1:                                 #every KEYDOWN event has a key and a mod. Refer to pygame.key documentation for list of constants and their representations.
#                    key = 1
#                if event.key == pygame.K_2:
#                    key = 2
#                if event.key == pygame.K_3:
#                    key = 3
#                if event.key == pygame.K_4:
#                    key = 4
#                if event.key == pygame.K_5:
#                    key = 5
#                if event.key == pygame.K_6:
#                    key = 6
#                if event.key == pygame.K_7:
#                    key = 7
#                if event.key == pygame.K_8:
#                    key = 8
#                if event.key == pygame.K_9:
#                    key = 9
                #needs 2 more keys: enter(return) and delete (to reset all empty cells) - see pygame.key for documentation.
                #needs event.type == pygame.MOUSEBUTTONDOWN - refer to pygame.mouse for documentation.





main_window() #test function
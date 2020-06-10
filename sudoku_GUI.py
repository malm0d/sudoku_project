#Construct and implement GUI for Sudoku solver, using pygame.
import pygame
from sudoku_txtv1 import find_empty_cells, harmony, solve_sudoku
import time
pygame.init()

#Create classes for global grid, and single cell.

class Single_Cell:
    rows = 9                                                           #Class Variables present in all SIngle_Cell instances.
    columns = 9                                                        #Class Variables will be used as arguments for parameters: rows & columns in the Global_Grid Instance.
    def __init__(self, value, row, column, width, height):
        self.value = value
        self.row = row
        self.column = column
        self.width = width                                             #Both self.width & self.height attributes will be same as the self.width & self.height attributes in Global_Grid instance,
        self.height = height                                           #because it not realistic to determine the exact dimensions of each Single_Cell instance.
        self.selection = False
        self.temporary_value = 0

    def insert_temporary_value(self, value):                           #Method sets a temporary value in the selected cell if inserted value does not satisfy global constaints,
        self.temporary_value = value                                   #or, if user wants to put a value in the selected cell but does not want to commit the value in the selected cell (sketch).
    
    def insert_value(self, value):                                     #Method inserts a value in the selected cell.
        self.value = value

    def draw_single_cell(self, screen):                                #The draw_single_cell function highlights the selected cell, and blits a number (image) onto the surface of a single cell.
        cell_measuremt = (self.height / 9)                             #Divide either self.width or self.height by 9 to get width or height (dimensions) of a Single_Cell instance, which is a square.         
        cell_x = (self.column * cell_sides_measurement)                #Calculate x & y coordinates of the Single_Cell, coordinates are not indices but actual measurement values.
        cell_y = (self.row * cell_sides_measurement)
        gray = (128, 128, 128)
        some_blue = (0, 170, 204)
        white = (255, 255, 255)
        font = pygame.font.SysFont("Times", 32)                        #SysFont(name, size, bold=False, italic=False) -> Font. Set the Font and Font size to be used.
        if self.selection == True:                                                                      #self.selection == True when a single cell is selected. If so draw a rectangle to higlight cell borders.
            pygame.draw.rect(screen, some_blue, (cell_x, cell_y, cell_measuremt, cell_measuremt), 2)    #rect(surface, color, rect, width=0, border_radius=0...) -> Rect. rect=(posn:x & y and dimnsn: width & height).
                                                                                                        #If width > 0, used for line thickness.
        if self.value != 0:                                                               #Draws self.value onto a single cell, of which is not an empty cell. That is, self.value is a number already present in the board. 
            text = font.render(str(self.value), True, white)                              #render(text, antialias, color, background=None) -> Surface. Font.render() creates an image(Surface) of the text, & blits it onto another Surface. The
            screen.blit(text, (cell_x +(cell_measuremt/2), cell_y +(cell_measuremt/2)))   #antialias argument is a boolean: if true, characters will have smooth edges. blit(source, dest, area=None, special_flags=0) -> Rect. 
                                                                                    #Dest can be coordinates repping upper left corner of the source. So, add (cell_measuremt/2) to x & y to place self.value in exact middle of a single cell.
        elif self.value == 0 and self.temporary_value != 0:                             
            text = font.render(str(self.temporary_value), True, gray)                     #Draws self.temporary_value onto an empty cell (self.value == 0). So, self.temporary_value is a number that has yet to be committed to an empty cell,
            screen.blit(text, (cell_x +(cell_measuremt/2), cell_y +(cell_measuremt/2)))   #or what can be described as the number that is 'sketched' into an empty cell as the user's workings.

    def 




class Global_Grid:                                                      #A Global_Grid instance will hold all Single_Cell instances.

    sudoku_board = [                                                    #Adjust board manually if user wants to change the board/difficulty.
    [5, 0, 0, 1, 8, 0, 0, 7, 0],                                        #sudoku_board object represents the starting grid of filled cells.
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
        self.selection = None

    white = (255, 255, 255)
    gray = (128, 128, 128)                                      #pygame.draw.line(surface, color, start_pos, end_pos, width) -> Rect. start_pos & end_pos receive (x, y) coordinates (as Tuples or List).
    def draw_grid(self, screen):                                #Draw grid lines. Major grid lines are white, minor grid lines are gray.
        cell_width = (self.width / 9)                           #Divide width into 9 equal cells.
        for n in range(self.column + 1):                        #There are 10 vertical and horizontal lines dividing cells equally, so self.column + 1 includes very last vertical & horizontal line to iterator: [0,1,2,3,4,5,6,7,8,9].
            if n % 3 == 0:                                      #Apply same logic in make_board() function from sudoku_txtv1.py to modulo operations. Thicker lines are n = 0, 3, 6, 9. Thin lines are the remaining n values.
                line_width = 3                                  #Default line width = 1.  Width < 1 = nothing will be drawn.
            else:
                line_width = 1
            if line_width == 3:                                                                                       #First vertical and horizontal line: cellwidth*0, last vertical and horizontal line: cellwidth*9.
                pygame.draw.line(screen, white, ((cell_width * n), 0), ((cell_width * n), self.height), line_width)     #Draws vertical major grid lines, starting from y = 0.
                pygame.draw.line(screen, white, (0, (cell_width * n)), (self.width, (cell_width * n)), line_width)      #Draws horizontal major grid lines, starting from x = 0.
            elif line_width == 1:
                pygame.draw.line(screen, gray, ((cell_width * n), 0), ((cell_width * n), self.height), line_width)      #Draws vertical minor grid lines, starting from y = 0.
                pygame.draw.line(screen, gray, (0, (cell_width * n)), (self.width, (cell_width * n)), line_width)       #Draws horizontal minor grid lines, starting from x = 0.

    def selection(self, row, column):
        for x in range(self.rows):                              #method assigns (row, column) coordinates to self.selection.
            for y in range(self.columns):
                ???



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
#Construct and implement GUI for Sudoku solver, using pygame.
import pygame
from sudoku_txtv1 import make_board, find_empty_cells, harmony, solve_sudoku
import time
pygame.init()

#Create classes for global grid (9x9), and single cell.
class Global_Grid:

    sudoku_board = [                                    #adjust board manually if user wants to change the board/difficulty.
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
        



class Single_Cell:
    pass


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
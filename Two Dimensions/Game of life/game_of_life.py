import functions
import pygame
import time
import numpy as np


ROWS = 50
COLUMNS = 70

WINDOW_X = COLUMNS * functions.BLOCK_SIZE
WINDOW_Y = ROWS * functions.BLOCK_SIZE


grid = np.zeros(shape=(COLUMNS, ROWS))

pygame.init()
pygame.display.set_caption('Game of Life. Click to change the state of the blocks. Press enter to start/pause.')

displaysurf = pygame.display.set_mode((WINDOW_X, WINDOW_Y))


on_cycle = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Checks for left click(1) mousedown event.
            
            (mouseX, mouseY) = pygame.mouse.get_pos()
            
            block_X = mouseX // functions.BLOCK_SIZE    # Calculate the indices of the block clicked in the grid array.
            block_Y = mouseY // functions.BLOCK_SIZE

            if grid[block_X][block_Y] == 0:      # Change the state of the block that was clicked.
                grid[block_X][block_Y] = 1
            elif grid[block_X][block_Y] == 1:
                grid[block_X][block_Y] = 0

        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):   # Checks for whenever the enter key is pressed.
            on_cycle = not on_cycle
            
    if on_cycle:
        new_grid = functions.UpdateGrid(grid, COLUMNS, ROWS)

        if (new_grid == grid).all():
            grid = new_grid
            on_cycle = False
        else:
            grid = new_grid
            on_cycle = True
            time.sleep(0.125)    


    functions.PaintGrid(grid, displaysurf, COLUMNS, ROWS)
    pygame.display.update()
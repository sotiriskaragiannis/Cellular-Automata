import numpy as np
import pygame 
# from pygame.locals import *

BLOCK_SIZE = 25 # in pixels


# set up colors
BLACK = (  0,  0,  0)
WHITE = (255,255,255)

def PaintGrid(grid, screen, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                DeleteBlock(screen, i*BLOCK_SIZE, j*BLOCK_SIZE)
            if grid[i][j] == 1:
                PaintBlock(screen, i*BLOCK_SIZE, j*BLOCK_SIZE)


def PaintBlock(screen, x, y):
    pygame.draw.rect(screen, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))

def DeleteBlock(screen, x, y):
    pygame.draw.rect(screen, BLACK, (x, y, BLOCK_SIZE, BLOCK_SIZE))

def UpdateGrid(grid, rows, columns):
    new_grid = np.zeros(shape=(rows,columns))

    for i in range(rows):
        for j in range(columns):
            
            count = grid[i-1][j-1] + grid[i][j-1] + grid[(i+1)%rows][j-1] + grid[i-1][j] + grid[(i+1)%rows][j] + grid[i-1][(j+1)%columns] + grid[i][(j+1)%columns] + grid[(i+1)%rows][(j+1)%columns]

            if grid[i][j] == 1 and (count == 2 or count == 3):
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and count == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = 0
            
    return new_grid

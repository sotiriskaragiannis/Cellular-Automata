import numpy as np
from PIL import Image


def CalculateAccordingToRule(index_of_rule):
    
    rule = getbinary(RULE, 8)       # convert decimal number of rule to binary from to be able to decode it (based on: https://mathworld.wolfram.com/ElementaryCellularAutomaton.html)
    rule = rule[::-1]   # reverse the string

    return int(rule[index_of_rule])

def CalculateNextGeneration(cells):

    newcells = []
    for i in range(len(cells)):  # Get all triplets(neighborhoods) of the array to calculate the next generations
                                 # For the first and last bits we include the last and the first bit (as if the array is a circle)
        if i+1 != len(cells):   
            neighborhood = f'{cells[i-1]}{cells[i]}{cells[i+1]}'  
        else:
            neighborhood = f'{cells[i-1]}{cells[i]}{cells[0]}'

        index_of_rule = int(neighborhood, 2)     # Turn triplets from binary to decimal to relate them to the rule
        newcell = CalculateAccordingToRule(index_of_rule)
        newcells.append(newcell)
    
    return newcells

getbinary = lambda x, n: format(x, 'b').zfill(n)

# main

Image_size = (5080,2600)   # (x,y image size)

block_size = 2  # (in pixels)
rows = int(Image_size[1] / block_size)  # calculate rows and columns of the grid based on Image size and the block size
columns = int(Image_size[0] / block_size)

img = Image.new("RGB", size=Image_size, color=(255, 255, 255))  # define Image object

  

cells = np.array([], dtype=int)  # Create a numpy array of integer type

for i in range(columns):
    if i == columns // 2:
        cells = np.append(cells, 1)    # Append numpy array
    else:
        cells = np.append(cells, 0)


RULE = int(input("Rule?(0-255) "))


for y in range(0, Image_size[1], block_size): # iterate for every row in the photo
    x = 0
    for i in range(len(cells)):                 # iterate for every cell in the array
        if cells[i] == 1:
            for k in range(x, x+block_size):
                for j in range(y, y+block_size):
                    img.putpixel((k, j), (0,0,0))       # paint black active cells 
        x = x + block_size                          # increment x dimension of photo by block_size
    cells = CalculateNextGeneration(cells)          # Calculate the next generation of cells based on the rule

im = img.save(f"filepath\elm_ca{RULE}.jpg")        # Enter the full filepath to the directory you want the photo to be

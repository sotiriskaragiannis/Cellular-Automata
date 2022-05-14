import PySimpleGUI as sg
import numpy as np

SIZE_Y = 1300 
SIZE_X = 2540 

block_size = 5  #(in pixels)
rows = int(SIZE_Y / block_size)
columns = int(SIZE_X / block_size)

# Turns an 1d array of 0,1,2,3 to different colors.
def PrintCells(cells, graph, y):
    x = 0
    for cell in cells:
        if cell == 0:
            background = 'black'
        if cell == 1:
            background = 'cyan'
        if cell == 2:
            background = 'magenta'
        if cell == 3:
            background = 'blue'   
        graph.DrawRectangle((x,y), (x+block_size, y+block_size), fill_color=background)
        x = x + block_size


cells = np.array([], dtype=int)  # Create a numpy array of integer type

for i in range(columns):
    if i == columns // 2:
        cells = np.append(cells, 3)    # Append numpy array
    else:
        cells = np.append(cells, 0)
layout = [[sg.Graph(canvas_size=(SIZE_X,SIZE_Y), graph_bottom_left=(0,SIZE_Y), graph_top_right=(SIZE_X,0), background_color='white', key='graphs')]]

window = sg.Window('Test', layout, finalize=True)
graph = window['graphs']


y = 0
j = 0

while(j < rows):     # Number of rows(generations) of the output
    PrintCells(cells, graph, y)
    newcells = np.array([], dtype=int)
    for i in range(len(cells)):  # Get all triplets(neighborhoods) of the array to calculate the next generations
                                 # For the first and last bits we include the last and the first bit (as if the array is a circle)
        if i+1 != len(cells):   
            newcell = (cells[i-1]+cells[i]+cells[i+1]) % 4          # New generation cell is created by the sum of the top 3 blocks.
        else:                                                       # We use mod 4 to ensure the state is within the range of the 4 states
            newcell = (cells[i-1]+cells[i]+cells[0]) % 4
        
        newcells = np.append(newcells, newcell)
    
    cells = newcells
    j += 1
    y = y + block_size


# GUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
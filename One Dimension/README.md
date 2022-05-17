# One-dimensional cellular automata
## Simplest cellular automata
Inspired by Wolfram's Elemntary Cellular Automata (https://mathworld.wolfram.com/ElementaryCellularAutomaton.html), [simplest_ca.py](simplest_ca.py) is a terminal program written
in python that can create all different 256 rules. The program asks the user for the number of the rule and it creates the pattern with initial conditions of one active block in
the center.
<br />
![](https://github.com/sotiriskaragiannis/Cellular-Automata/blob/main/One%20Dimension/wolfram%20images/ElementaryCARules_900.png)
<br />
The graphics are created with colorama for background color in windows and linux terminal. By writing space characters and changing the background color
the black and white blocks are created. For pictures click [here](https://github.com/sotiriskaragiannis/Cellular-Automata/tree/main/One%20Dimension/wolfram%20images)
<br />

## Four State Sum of neighborhood cellular automata
This is another one dimensional CA, but is now projected in a new gui window ([four_state_sum_of_neighborhood_ca.py](four_state_sum_of_neighborhood_ca.py)).
Each block has four states 0-black, 1-cyan, 2-magenta, 3-blue.
In the code you can change the size of the window and the block size:
```
SIZE_Y = ... 
SIZE_X = ... 

block_size = ...  #(in pixels)
```
### New generations
The state of each block of the new generation is produced by taking sum of the top three blocks (nearest neighborhood) and calculating the mod 4 to ensure that the new state is within the range of the four states.
```
newcell = (cells[i-1]+cells[i]+cells[i+1]) % 4
```
### Initialization
The initial conditions are one block in the middle with state 3.
```
for i in range(columns):
    if i == columns // 2:
        cells = np.append(cells, 3)    # Append numpy array
    else:
        cells = np.append(cells, 0)
```
### Images
- Block size 10 and window size 1270x650
 
![block_size_10](https://user-images.githubusercontent.com/87957685/168443419-002d91c3-4945-4fbf-ab8a-b03c7670e590.png)

- Block size 5 and window size 1270x650
 
![block_size_5](https://user-images.githubusercontent.com/87957685/168443417-badf8d8f-8dd1-4a1e-aab2-d5fd89a04e89.png)

- Block size 2 and window size 1270x650
 
![block_size_2](https://user-images.githubusercontent.com/87957685/168443414-a5c31472-66bc-474c-91ac-51478d4e345b.png)

### Changing the number of state using the same rule for the next generations
You can easily change the number of block states and keep the same algorithm.
For example these are the modifications of the ([four_state_sum_of_neighborhood_ca.py](four_state_sum_of_neighborhood_ca.py)) that would make it ten state.
```
def PrintCells(cells, graph, y):
    x = 0
    colors = ['black', 'green',
          'red', 'blue', 'yellow', 'white', 'purple', 'grey',
          'orange', 'cyan']
    for cell in cells:
        background = colors[cell]   
        graph.DrawRectangle((x,y), (x+block_size, y+block_size), fill_color=background)
        x = x + block_size
```

```
if i+1 != len(cells):   
            newcell = (cells[i-1]+cells[i]+cells[i+1]) % 10          # New generation cell is created by the sum of the top 3 blocks.
        else:                                                       # We use mod 10 to ensure the state is within the range of the 10 states
            newcell = (cells[i-1]+cells[i]+cells[0]) % 10
```

#### Results

![ten_state_block_size_5](https://user-images.githubusercontent.com/87957685/168742854-4e83f434-a16e-48e1-8621-da15d271f11f.png)
![ten_state_block_size_10](https://user-images.githubusercontent.com/87957685/168742871-44ae4903-7903-4e23-92b0-d0de9f3de62d.png)

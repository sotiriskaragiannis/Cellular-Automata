import colorama


# Turns an 1d array of 1 and 0 to black and white squares in the terminal.
def PrintCells(cells):
    for cell in cells:
        if cell == 0:
            background = colorama.Back.WHITE
        if cell == 1:
            background = colorama.Back.BLACK
        print(background + '  ' + colorama.Style.RESET_ALL, end="")
    print("")

getbinary = lambda x, n: format(x, 'b').zfill(n)  

def CalculateAccordingToRule(index_of_rule):
    rule = getbinary(RULE, 8)
    rule = rule[::-1]   # reverse the string

    return int(rule[index_of_rule])

cells = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]


RULE = int(input("Rule? "))
j = 0

while(j < 65):    
    PrintCells(cells)
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
    
    cells = newcells
    j += 1

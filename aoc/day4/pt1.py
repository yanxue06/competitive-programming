
# i think this is a graph problem 
# i also should be able to get the dimensions too, so maybe i can just iterate through every  
# index and check its 8 surrounding indexes   
# now that i think of it, it might be easier to just do a 2d array traversal lol 
'''
111
101
111

In this case I would only look at 0, and look at its surroundings, so looks from 
1 to col - 1, in this case 1 to 1 
and  1 to row - 1, in this case 1 to 1 
'''

f = open('./input.txt', 'r').read().split('\n')

grid = [list(line) for line in f]

print("# cols:", len(grid[0]))
print("# rows:", len(grid))


# store a set of tuples, a set becase these tuples 
# set will reset to nothing at every new iteartion 
total = 0 
allIndexes = set() 

for i in range(len(grid)): 
    for j in range(len(grid[0])): 
        
        count = 0 
        # iterate in the surrounding 8 
        # in a square i guess 
        if grid[i][j] != "@": 
            continue 
        
        # left center  
        if (j - 1) >= 0: 
            if grid[i][j-1] == "@": 
                count+= 1 
        
        if (j + 1) < len(grid[0]):
        # right center 
            if grid[i][j+1] == "@": 
                count+= 1 
        
        # top row 
        if (i - 1) >= 0:
            for k in range(-1, 2): 
                if 0 <= (j + k) < len(grid[0]) and grid[i - 1][j + k] == "@": 
                    count+= 1 

        # bottom row 
        if (i + 1) < len(grid): 
            for k in range(-1, 2):
                if 0 <= (j + k) < len(grid[0]) and grid[i + 1][j + k] == "@": 
                    count+=1 
            
        if count < 4: 
            allIndexes.add((i, j))

print(len(allIndexes))

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

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

num_rows = len(grid)
num_cols = len(grid[0])

for i in range(num_rows):
    for j in range(num_cols):

        if grid[i][j] != "@":
            continue

        count = 0
        
        for dr, dc in directions:
            
            ni, nj = i + dr, j + dc

            if 0 <= ni < num_rows and 0 <= nj < num_cols:
                
                if grid[ni][nj] == "@":
                    count += 1
        
        if count < 4:
            allIndexes.add((i, j))

print(len(allIndexes))
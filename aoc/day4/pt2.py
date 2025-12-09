f = open('./input2.txt', 'r').read().split('\n')

grid = [list(line) for line in f]

print("# cols:", len(grid[0]))
print("# rows:", len(grid))

# store a set of tuples, a set becase these tuples 
# set will reset to nothing at every new iteartion 
total = 0 
indexes = set() 

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

num_rows = len(grid)
num_cols = len(grid[0])
count = 0 
totalCount = 0
first = True 

while first or indexes: 

    first = False 
    tmp = indexes.copy()
    for index in tmp: 
        if grid[index[0]][index[1]] == "@": 
            grid[index[0]][index[1]] = "."
        indexes.remove(index)
        count += 1 

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
                indexes.add((i, j))
                totalCount += 1 

print(totalCount)
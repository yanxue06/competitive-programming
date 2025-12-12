
arr = [] 

with open('./input2.txt', 'r') as f: 
    for line in f: 
        arr.append(list(line.strip()))

# find s starting 
# use memoization for optimization 

start = 0 

for i in range(len(arr[0])): 
    if arr[0][i] == 'S': 
        start = i 

paths = 0 

def dfs(r, c): 
    global paths

    # should be only two base cases: 
    if c < 0 or c >= len(arr[0]) or r < 0 or r >= len(arr): 
        return 
    elif r == len(arr) - 1: 
        # final row 
        paths += 1
        return

    if arr[r][c] == '^': 
        dfs(r, c - 1)
        dfs(r, c + 1)
    else: 
        dfs(r + 1, c)
    

dfs(0, start)

print(paths)

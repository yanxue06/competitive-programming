# let's first load everything into a 2d array

arr = list(open('./input.txt', 'r').read().split('\n'))

for i in range(len(arr)): 
    arr[i] = list(arr[i])

# START AT INDEX OF S AND THEN DO DFS 
# find where S starts 

start = 0 

for i in range(len(arr[0])): 
    
    if arr[0][i] == 'S':
        start = i 

split = 0 

def dfs(row, col): 
    global split 

    # base case 
    if row < 0 or row >= len(arr) or col < 0 or col >= len(arr[0]):
        print("hi")
        return 

    if arr[row][col] == "poo": 
        # went down this path, just return
        return

    if arr[row][col] == '^': 
        split += 1 
        # then we want to go to the left and right cell, same row 
        arr[row][col] = "poo" # mark it once i visit so no double count

        dfs(row, col-1)
        dfs(row, col+1)
    else: 
        arr[row][col] = "poo" # mark it once i visit so no double count
        dfs(row+1, col)

dfs(0, start)

print(split)


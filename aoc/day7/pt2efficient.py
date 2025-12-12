
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

memo = {} 

def count_paths(r, c): 
    # 1. Base Case: Out of Bounds
    if c < 0 or c >= len(arr[0]) or r < 0 or r >= len(arr): 
        return 0 # 0 paths from out of bounds
    
    # 2. Check Memoization Table
    if (r, c) in memo:
        return memo[(r, c)] # Return the stored result instantly

    # 3. Base Case: Success (Final Row)
    if r == len(arr) - 1: 
        return 1 # 1 path found
    
    # 4. Recursive Step: Calculate paths from the next step(s)
    total_paths = 0
    current_char = arr[r][c]

    if current_char == 'S' or current_char == '^': 
        # Split: Sum of paths from Left AND Right
        total_paths += count_paths(r, c - 1)
        total_paths += count_paths(r, c + 1)
    else: 
        # Straight: Paths from Down
        total_paths += count_paths(r + 1, c)
        
    # 5. Store the result before returning
    memo[(r, c)] = total_paths
    
    return total_paths

# Start the counting
total_timelines = count_paths(0, start) 

print(f"Total Timelines (Paths): {total_timelines}")
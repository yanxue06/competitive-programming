import re 

with open('./input.txt', 'r') as f:
    instructions = f.read().split(',')

total = 0 

for instruction in instructions: 

    groups = instruction.split('-')

    start = int(groups[0])
    end = int(groups[1])

    for i in range(start, end): 
        
        # detect if some number is repeating 
        num = str(i)
        
        if len(num) % 2 != 0: 
            continue 
        
        half = len(num) // 2 

        if num[:half] == num[half:]: 
            total += i 
    
print(total) 



    




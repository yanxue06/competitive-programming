# I HATE RTHIS WHAT IS GOING ON 

f = open('./input2.txt', 'r').read().splitlines()

ops = f[-1]
f = f[:-1]

total = 0 
subTotal = 0 

for i in range(len(ops)): 
    # number of times i'm going to perform an operation 
    # how do i know what the numbers are? 
    # I think its best to leave them as strings here so I can index
    
    # lets figure out where to start in a column
    start = 0 

    for j in range(len(f)): 
        if len(f[j][i]) > start: 
            start = len(f[j][i]) - 1 
    
    for j in range(start, -1, -1): 

        num = "" 

        for k in range(len(f)): 
            if len(f[k][i].strip()) < j: 
                num += f[k][j]
        
        if j == start: 
            subTotal = int(num)
        elif ops[i] == "*": 
            subTotal *= int(num)
        else: 
            subTotal += int(num)

    total += subTotal 

print(total) 






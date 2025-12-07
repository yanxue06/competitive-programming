
f = open('input2.txt', 'r').read().split(',')

instructions = [list(map(int, i.split('-'))) for i in f]
total = 0 

for instruction in instructions: 
    print(instruction)

    # if there is an odd number of characters, then it must be the case 
    # that all letters are the same

    # is there a smart way of identifying if a number is valid or not (continously repeating patterns)

    start = instruction[0] 
    end = instruction[1] 
    for i in range(start, end + 1): 

        s = str(i)

        if len(s) < 2:
            continue
        # check if invalid 
        # case 1: number has odd number of characters, then all characters have to be the same
        if i % 2 != 0 and len(set(str(i))) == 1: 
            total += i
            continue 
    
        # case 2: even number of charcters, must actually check if it has a repeating pattern :( or maybe case 1 can be shoved in this 
        for k in range(1, len(str(i)) // 2 + 1): 

            subset = s[:k] 

            if len(s) % k == 0: 
                multiple = len(s) // k

                newStr = subset*multiple

                if newStr == s: 
                    # invalid 
                    total += i 
                    break 
    
print(total)

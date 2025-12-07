f = open('./input.txt', 'r').read().split('\n') # Use splitlines for safer input

total = 0

for bank in f: 

    # lets find the largest digit and track its value and index 
    # then after that we can start searching for the second largest from 
    # one after the index of the largest value 
    largest = int(bank[0]) 
    index = 0 

    for i in range(len(bank) - 1): 
        
        cur = int(bank[i])

        if cur > largest: 
            largest = cur 
            index = i 
    
    secondLargest = int(bank[index + 1])

    for i in range(index + 1, len(bank)): 

        cur = int(bank[i])
        if cur > secondLargest: 
            secondLargest = cur 
        
    subTotal = int(str(largest) + str(secondLargest))
    total += subTotal

print(total) 


# answer: 17613
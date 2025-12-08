
f = open('./input2.txt', 'r').read().split('\n')

# my solution for part 1 would technically work but be very brute force 
# choose from most signficant digit to least significant 
# i could technically do a giga for loop 
# i could loops through every bank 12 times, honestly not a horrible idea 
# let's try this brute force

total = 0 

for bank in f: 
        
    # get top 12 largest numbers where for some largest number n at N, 
    # the (n + 1)'th largest number as an index P > N 
    subTotal = '' 

    largestIndex = -1 
    largest = '_'

    for j in range(12): 
        
        largest = '-1' 
        for k in range(largestIndex + 1, len(bank) - 11 + j):
            cur = bank[k]
            if cur > largest: 
                largest = cur 
                largestIndex = k 

            if cur == '9': break 

        subTotal += largest 
    
    total += int(subTotal)

print(total)
# since I know that the numbers only exist in the first 4 rows, 
# I can like of do a scan horizontally with a vertical bar that checks each of the 4 rows. 
# If the bar scans no numbers, that means that I am at the seperation column between
# the latest operation and the next  

f = open('input.txt', 'r').read().splitlines()

nums = [list(map(int, line.split())) for line in f[:-1]]

print(nums)
ops = f[-1].split()

print(ops)

total = 0 

for i in range(len(ops)): 
    subTotal = nums[0][i]

    for j in range(1, len(nums)): 
        if ops[i] == "*": 
            subTotal *= nums[j][i]
        else: 
            subTotal += nums[j][i]

    total += subTotal

print(total)

# i need to parse all the ranges first 

ranges = [] 
to_test = [] 

with open('./input2.txt', 'r') as f: 

    for line in f: 

        if line.strip() == "": 
            break
        
        # these are the ranges 
        start, _, end = line.partition('-')
        ranges.append(list(map(int, [start, end])))

# there are probbaly many overlapping intervals, so goign through all olf them 
# and all the duplicate numbers would be a very  
# bad idea. Instead, let's do something smart 
# the idea is to first sort intervals based on their starting...
# then we can iterate through all intervals and then  like use a queue maybe 
# like if the end of interval 0 is greater or equal to the start of intenral 1,  
# then we can combine that interval into a single interval. 
# on second thought, maybe we use a stack for this. 

ranges.sort(key=lambda r: r[0])

merged = [] 
start, end = ranges[0]

for next_range in ranges[1:]:  
    next_start, next_end = next_range

    if next_start <= end + 1: 
        end = max(end, next_end)
    else: 
        merged.append([start, end])

        start, end = next_start, next_end 

# if it gets merged in in the last i teration then this is perfect! just add the new merged interval
# if the last one is a gap, then start and end were updated to ranges[last index] so we are good, just 
# append that disjoint interval 

merged.append([start, end])

fresh = 0 

for range in merged: 

    fresh += range[1] - range[0] + 1 

print(fresh)


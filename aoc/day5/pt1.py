# i need to parse all the ranges first 

ranges = [] 
to_test = [] 

with open('./input.txt', 'r') as f: 

    # i want to get all the range first 
    after = False 

    for line in f: 

        if line.strip() == "": 
            after = True 
            continue
        
        if not after: 
            # these are the ranges 
            start, _, end = line.partition('-')
            ranges.append(list(map(int, [start, end])))
        else: 
            to_test.append(int(line.strip()))

fresh = 0 

for n in to_test: 
    for start, end in ranges: 
        if n >= start and n <= end: 
            fresh += 1 
            break 

print(fresh)


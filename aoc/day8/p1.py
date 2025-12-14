# disjoint set union
# resource (thanks Koral): https://usaco.guide/gold/dsu
# article: https://csacademy.com/lesson/disjoint_data_sets

f = open('./input.txt', 'r').read().splitlines()

# the distance between any two junction boxes can be 
# determined by using the euclidian distance formula 
# once a junfction box is added to a set of another junction boxes, we 
# must consider them in the same set and a part of one group 

# i think we must first calculate the distance from every junction box 
# to every junction box and then sort to determine the 10 connections to make 
# for every conection we make, we should be grouping them together. 
# and then, we can sort that grouped array once more, and then take the 
# top three groups and multiply 

# turn to integers first 
nodes = [list(map(int, line.split(','))) for line in f]

# calculate the distance between current node and all other nodes 
# make sure not to double count, distance node 1 to node 2 is same as 
# distance node 2 to node 1 

edges = [] 
n = len(nodes) 

# we can fill edges up with tuples (dist, node x, node y)

for i in range(n): 
    for j in range(i+1, n): 
        # i + 1 ensures we never double count I think 

        node = nodes[i]
        node2 = nodes[j] 
        d = (node[0] - node2[0])**2 + (node[1] - node2[1])**2 + (node[2] - node2[2])**2 
    
        edges.append((d, i, j))

edges.sort(key=lambda x: x[0])

# now we take the top 1000 connetions and group them, can use DSU's here 

parent = list(range(n)) # parent[i] represents the parent of node i 
size = [1] * n 

def find(node) -> int: 

    if parent[node] != node: 
        parent[node] = find(parent[node])

    return parent[node] 

def merge(i, j) -> bool: 
    # root of smaller should always point to root of bigger to 
    # prevent cursed long trees 
    root1 = find(i)
    root2 = find(j)

    if root1 != root2: 
        # then we want to merge 
        # merge the smaller tree into the bigger tree 
        if size[root2] > size[root1]: 
            parent[root1] = root2 

            size[root2] += size[root1]
        else: 
            parent[root2] = root1 

            size[root1] += size[root2]
    
        return True 
    return False 

connections_made = 0 
connections_limit = 1000 

for dist, u, v in edges: 
    if connections_made >= connections_limit:
        break
        
    merge(u, v)
    connections_made += 1

size.sort(reverse=True)

print(size[0] * size[1] * size[2])

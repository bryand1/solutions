from collections import defaultdict

edges = defaultdict(list)
V = int(input())
for vertex in range(2, V + 1):
    parent = int(input())
    edges[parent].append(vertex)

def is_spruce(parent):
    leafs = 0
    for child in edges[parent]:
        if child in edges: 
            if not is_spruce(child):
                return False
        else:
            leafs += 1
    return leafs >= 3

print("Yes" if is_spruce(1) else "No")

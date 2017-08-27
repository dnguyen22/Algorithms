# HW3: Min Cut Graph


# Set up adjacency
graph = {}
with open('kargerMinCut.txt') as f:
    for line in f:
        split_line = line.split()
        graph[int(split_line[0])] = set(split_line[1:])

print(graph)
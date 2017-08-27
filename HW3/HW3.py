# HW3: Min Cut Graph
import random


# Returns randomized calculation of min cut graph algorithm
def calculate_min_cut(graph):
    # Iterate until only two vertices remain
    while len(graph) > 2:
        # Pop random vertex
        random_vertex = graph.pop(random.choice(list(graph)))
    return 0


# Set up adjacency list as dictionary with keys as vertices, values as set of edges
graph = {}
with open('kargerMinCut.txt') as f:
    for line in f:
        split_line = line.split()
        graph[int(split_line[0])] = set(split_line[1:])

print(graph)
print(calculate_min_cut(graph))
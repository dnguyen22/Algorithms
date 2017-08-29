# HW3: Min Cut Graph
# Todo: Remove repeats of rand_vertex when merging
import random


# Returns randomized calculation of min cut graph algorithm
def calculate_min_cut(graph):
    # Iterate until only two vertices remain
    while len(graph) > 2:
        # Pop random vertex
        rand_vertex = random.choice(list(graph))
        # Get edges of random vertex
        rand_edges = graph.pop(rand_vertex)
        # Randomly pick vertex to merge into from initial vertex edges
        vertex_to_merge = random.choice(rand_edges)

        # Merge random vertex into vertex_to_merge
        #
        # Remove rand_vertex from vertex_to_merge edges
        graph[vertex_to_merge].remove(rand_vertex)
        # Remove vertex_to_merge from rand_vertex edges
        rand_edges.remove(vertex_to_merge)

        for edge in rand_edges:
            # Update edge of each vertex from rand_vertex to vertex_to_merge
            graph[edge].remove(rand_vertex)
            graph[edge].append(vertex_to_merge)
            # Add rand_vertex edges to vertex_to_merge edges
            graph[vertex_to_merge].append(edge)

    # Get key vertices of graph
    vertices = graph.keys()
    # Count cuts between vertices
    count_cuts = 0
    for edge in graph[vertices[0]]:
        if edge == vertices[1]:
            count_cuts = count_cuts + 1

    return count_cuts


# Set up adjacency list as dictionary with keys as vertices, values as list of edges
graph = {}
with open('kargerMinCut.txt') as f:
    for line in f:
        split_line = line.split()
        # Converts list of string to list of int for value of each int vertex
        graph[int(split_line[0])] = list(map(int, split_line[1:]))

print(graph)
print(calculate_min_cut(graph))
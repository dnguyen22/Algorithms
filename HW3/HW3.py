# HW3: Min Cut Graph
import random


# Returns randomized calculation of min cut graph algorithm
def calculate_min_cut(graph):
    # removed_vertices = []
    # Iterate until only two vertices remain
    while len(graph) > 2:
        # Pop random vertex
        rand_vertex = random.choice(list(graph))
        # Get edges of random vertex
        rand_edges = graph.pop(rand_vertex)
        # Randomly pick vertex to merge into from initial vertex edges
        vertex_to_merge = random.choice(list(rand_edges))

        # Merge random vertex into vertex_to_merge
        #
        # Remove rand_vertex from vertex_to_merge edges
        graph[int(vertex_to_merge)].discard(str(rand_vertex))
        # Remove vertex_to_merge from rand_vertex edges
        rand_edges.discard(vertex_to_merge)

        for edge in rand_edges:
            # Update edge of each vertex from rand_vertex to vertex_to_merge
            graph[int(edge)].discard(str(rand_vertex))
            graph[int(edge)].add(vertex_to_merge)
            # Add rand_vertex edges to vertex_to_merge edges
            graph[int(vertex_to_merge)].add(edge)

    return 0


# Set up adjacency list as dictionary with keys as vertices, values as set of edges
graph = {}
with open('kargerMinCut.txt') as f:
    for line in f:
        split_line = line.split()
        graph[int(split_line[0])] = set(split_line[1:])

print(graph)
print(calculate_min_cut(graph))
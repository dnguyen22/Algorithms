# HW11: Floyd-Warshall Algorithm - All Pairs Shortest Path Algorithm
#   O(n^3) for both dense and sparse graphs (graphs can include negative edges).
#   Compared to O(n*mn) for Bellman-Ford algorithm run for n vertices
#   [recall O(m) = O(n) for sparse graphs O(m) = O(n^2) for dense graphs]
#   or O(n*mlog(n)) for Dijkstra's algorithm on n vertices. Dijkstra's algorithm is faster, but only works on graphs
#   with non-negative edges.
#   Johnson's algorithm runs in O(mnlog(n)) for general graphs (including with negative edges).
#   Bellman-Ford can account for negative edges.
import math


# Loops through file and adds edges as a dictionary to vertex tail dictionary for fast lookups
def extract_data(file):
    dictionary = dict()
    with open(file) as f:
        text = f.readlines()
        # Extract data from header
        header_split = text[0].split()
        num_vertices = int(header_split[0])
        num_edges = int(header_split[1])
        # Skip first line (header)
        for line in text[1:]:
            split = line.split()
            # Outer dictionary key = tail vertex. Inner dictionary key = head vertex. Value = edge cost
            if int(split[0]) not in dictionary:
                dictionary[int(split[0])] = {int(split[1]): int(split[2])}
            else:
                dictionary[int(split[0])].update({int(split[1]): int(split[2])})
    return dictionary, num_vertices, num_edges


# graph holds edge costs in graph, NUM_VERTICES is the total number of vertices in graph,
#   and NUM_EDGES is the total number of edges in graph
graph, NUM_VERTICES, NUM_EDGES = extract_data('g1.txt')
# Set up path length dictionary
path_lengths = dict()
# Initialize boolean for negative cycles
has_negative_cycles = False
# Initialize shortest path length
shortest_path = math.inf
# Initialize path_lengths dictionary for k = 0
for i in range(1, NUM_VERTICES + 1):
    path_lengths[i] = {}
    for j in range(1, NUM_VERTICES + 1):
        path_lengths[i][j] = {}
        if i == j:
            path_lengths[i][j][0] = 0
        elif j in graph[i]:
            path_lengths[i][j][0] = graph[i][j]
        else:
            path_lengths[i][j][0] = math.inf
# Flyod-Warshall Algorithm
for k in range(1, NUM_VERTICES + 1):
    for i in range(1, NUM_VERTICES + 1):
        for j in range(1, NUM_VERTICES + 1):
            path_lengths[i][j][k] = min(path_lengths[i][j][k-1], path_lengths[i][k][k-1] + path_lengths[k][j][k-1])

            if k == NUM_VERTICES:
                # Check if graph has negative cycles
                if i == j and path_lengths[i][j][k] < 0:
                    has_negative_cycles = True
                if path_lengths[i][j][k] < shortest_path:
                    # Update shortest path
                    shortest_path = path_lengths[i][j][k]

if has_negative_cycles:
    print('Graph has negative cycles')
else:
    print('Shortest path: ' + str(shortest_path))

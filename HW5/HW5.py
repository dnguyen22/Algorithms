# HW5: Dijkstra's Algorithm
import heapq

# Max path length
MAX_PATH_LENGTH = 1000000

# Returns graph from text file of weighted edges. Graph is in the form of an adjacency list dictionary with vertices as
#   keys and (end vertex, edge weight) tuples as values
def extract_data(file):
    adjacency_list = {}
    with open(file) as f:
        for line in f:
            split_line = line.split()
            # Set starting vertex as key with empty list as value
            adjacency_list[int(split_line[0])] = []
            # edges contains tuples of end vertices and edge weights
            edges = split_line[1:]
            for edge in edges:
                split_edge = edge.split(',')
                adjacency_list[int(split_line[0])].append((int(split_edge[0]), int(split_edge[1])))
    return adjacency_list

# Adjacency list graph
graph = extract_data('dijkstraData.txt')
# Heap data structure to hold edges
heap = []
# List to hold path lengths. Index i-1 holds path length from vertex 1 to vertex i
path_length = [MAX_PATH_LENGTH] * len(graph)

print(graph)


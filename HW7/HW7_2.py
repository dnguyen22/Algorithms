# HW7_1: Prim's Minimum Spanning Tree - Greedy Algorithms
import heapq


# Returns graph from text file of weighted edges. Undirected graph is in the form of an adjacency list dictionary
#   with vertices as keys and list of [edge weight, end vertex] as values
def extract_data(file):
    adjacency_list = {}
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            split_line = line.split()
            # Set up keys when first discovered in file
            if int(split_line[0]) not in adjacency_list:
                adjacency_list[int(split_line[0])] = []
            if int(split_line[1]) not in adjacency_list:
                adjacency_list[int(split_line[1])] = []

            # Set vertices as key with list of [edge weight, other vertex] as value
            adjacency_list[int(split_line[0])].append([int(split_line[2]), int(split_line[1])])
            adjacency_list[int(split_line[1])].append([int(split_line[2]), int(split_line[0])])

    return adjacency_list


# Adjacency list graph
graph = extract_data('edges.txt')
# Heap data structure to hold edges
heap = []
# Set source vertex
vert = 1
# Initialize set of unexplored vertices
unexplored = set(graph.keys())
# Initialize set of explored vertices
explored = set()
# Initialize min span tree
min_span_tree = []
# Total cost of tree
cost = 0

while len(unexplored) > 0:
    # Update explored and unexplored sets with new vertex
    explored.add(vert)
    unexplored.remove(vert)

    edges = graph[vert]
    # Add edges from current vertex to heap if vertex is unexplored
    for edge in edges:
        if edge[1] in unexplored:
            # Add edge to heap
            heapq.heappush(heap, edge)

    while True:
        # Pop off minimum edge length until pop unexplored vertex
        min_vertex = heapq.heappop(heap)
        if min_vertex[1] in unexplored or not heap:
            break

    # Add edge to minimum spanning tree
    min_span_tree.append([vert, min_vertex[1], min_vertex[0]])
    # Set next vertex to be added to explored set
    vert = min_vertex[1]

print(graph)
# Print answers
print(min_span_tree)

for edge in min_span_tree:
    cost = cost + edge[2]

print(cost)
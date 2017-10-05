# HW5: Dijkstra's Algorithm
import heapq

# Max path length
MAX_PATH_LENGTH = 1000000


# Returns graph from text file of weighted edges. Graph is in the form of an adjacency list dictionary with vertices as
#   keys and (edge weight, end vertex) tuples as values
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
                adjacency_list[int(split_line[0])].append((int(split_edge[1]), int(split_edge[0])))
    return adjacency_list


def dijkstra(vertex, priority_queue, paths, current):
    edges = graph[vertex]
    for edge in edges:
        heapq.heappush(priority_queue, edge)

    # Pop off minimum edge length
    min_vertex = heapq.heappop(priority_queue)
    # Update path length with total length up to min_vertex
    current = current + min_vertex[0]
    paths[min_vertex[1] - 1] = current

# Adjacency list graph
graph = extract_data('dijkstraData.txt')
# Heap data structure to hold edges
heap = []
# List to hold path lengths. Index i-1 holds path length from vertex 1 to vertex i
path_length = [MAX_PATH_LENGTH] * len(graph)
# Current path length from source vertex up to current point
current_length = 0

print(graph)
#dijkstra(1, heap, path_length, current_length)
# Set source vertex
vert = 1
# Initialize set of unexplored vertices
unexplored = set(graph.keys())
# Initialize set of explored vertices
explored = set()

# Update explored and unexplored sets with new vertex
explored.add(vert)
unexplored.remove(vert)

#edges = graph[vert]
#for edge in edges:
#    heapq.heappush(heap, edge)

# Pop off minimum edge length
#min_vertex = heapq.heappop(heap)
# Update path length with total length up to min_vertex
#current_length = current_length + min_vertex[0]
#path_length[min_vertex[1]-1] = current_length
# Set next vertex to be added to explored set
#vert = min_vertex[1]

print(explored)
print(unexplored)

# HW4: Strongly Connected Components
import sys

class Graph(object):
    """A directed graph with the following properties:

    Attributes:
        adjacency_list: A dictionary where the keys are the vertices and the values are the edge endpoint vertices
    """

    def __init__(self):
        self.adjacency_list = {}

    # Returns graph from text file of directed edges. Graph is in the form of a dictionary with vertex keys
    def extract_data(self, file, reverse=False):
        with open(file) as f:
            for line in f:
                split_line = line.split()
                # Save edges as int tail and head. If reversed, switch tail and head
                if not reverse:
                    tail = int(split_line[0])
                    head = int(split_line[1])
                else:
                    head = int(split_line[0])
                    tail = int(split_line[1])

                # Add new node to graph; create new key if first time node appears
                if tail in self.adjacency_list:
                    self.adjacency_list[tail].add(head)
                else:
                    self.adjacency_list[tail] = set([head])

    # Returns number of vertices with an edge leaving them. Does not include
    #   vertices with no edges or vertices with no leaving edges.
    def get_graph_size(self):
        return len(self.adjacency_list)

    # Runs depth first search on graph to compute the fill order on Kosaraju's Algorithm
    def fill_order(self, vertex, visited, stack):
        visited[vertex] = True
        for edge in self.adjacency_list[vertex]:
            if edge in visited and visited[edge] == False:
                self.fill_order(edge, visited, stack)
        stack = stack.append(vertex)

    # Runs depth first search in fill order to find strongly connected components via Kosaraju's Algorithm
    def dfs(self):
        pass

# Runs SCC algorithm on graph and returns sizes of SCCs
def compute_scc_size(graph):
    sizes = []
    return sizes


# Runs depth first search loop on entire graph (Kosaraju's Algorithm)
def dfs_loop(graph):
    global finishing_time
    global leader_node

    finishing_time = 0

    # Loop through keys in graph and run dfs

    return


# Depth first search from starting node
def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()

    # Mark node as explored
    visited.add(node)

    # For every edge in graph from node, run dfs on head node if it is unexplored
    for next in graph[node] - visited:
        dfs(graph, next, visited)

    return visited

sys.setrecursionlimit(300000)

# Generate graph from edges text file
graph = Graph()
graph.extract_data('SCC_test.txt', False)

# Generate reverse graph from edges text file
reversed_graph = Graph()
reversed_graph.extract_data('SCC_test.txt', True)

# Run SCC algorithm on graph, return sizes of SCC
#size_SCC = []
#size_SCC = compute_scc_size(graph)
# Sort size_SCC from smallest to largest
#size_SCC.sort()
# Print size of 5 largest SCCs
#print(size_SCC[-5:])
finishing_order = []
visited_vertex = dict.fromkeys(set(graph.adjacency_list.keys()), False)

for vert in graph.adjacency_list:
    if visited_vertex[vert] == False:
        graph.fill_order(vert, visited_vertex, finishing_order)

print("Size of graph: " + str(graph.get_graph_size()))
#print(graph.adjacency_list)
#print(reversed_graph.adjacency_list)
print(finishing_order)
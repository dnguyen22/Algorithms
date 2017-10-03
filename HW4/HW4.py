# HW4: Strongly Connected Components

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


# Global finishing time
finishing_time = 0
# Global leader node
leader_node = None
# Global leader dictionary that sets the leader as the value for each node

# Generate graph from edges text file
graph = extract_data('SCC_test.txt')
# Run SCC algorithm on graph, return sizes of SCC
size_SCC = []
size_SCC = compute_scc_size(graph)
# Sort size_SCC from smallest to largest
size_SCC.sort()
# Print size of 5 largest SCCs
print(size_SCC[-5:])
print(graph)
print(rev_graph)
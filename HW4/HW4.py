# HW4: Strongly Connected Components


# Returns graph from text file of directed edges. Graph is in the form of a list of tuples of the start and end vertex
#   of edges
def extract_data2(file):
    graph = []
    with open(file) as f:
        for line in f:
            split_line = line.split()
            # Save edges as int tuples (tail, head)
            edge = int(split_line[0]), int(split_line[1])
            graph.append(edge)
    return graph


# Returns graph from text file of directed edges. Graph is in the form of a dictionary with vertex keys
def extract_data(file):
    graph = {}
    with open(file) as f:
        for line in f:
            split_line = line.split()
            # Save edges as int tail and head
            tail = int(split_line[0])
            head = int(split_line[1])
            if tail in graph:
                graph[tail].append(head)
            else:
                graph[tail] = [head]
    return graph


# Runs SCC algorithm on graph and returns sizes of SCCs
def compute_scc_size(graph):
    sizes = []
    return sizes

# Runs depth first search loop on entire graph (Kosaraju's Algorithm)
def dfs_loop(graph):
    return

# Depth first search from starting node
def dfs(graph, node):
    global explored_nodes
    # Mark node as explored
    explored_nodes.add(node)

    # For every edge in graph from node, run dfs on head node if it is unexplored
    return


# Global variable set of explored nodes
explored_nodes = set()
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
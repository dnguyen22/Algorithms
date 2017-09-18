# HW4: Strongly Connected Components


# Returns graph from text file of directed edges. Graph is in the form of a list of tuples of the start and end vertex
#   of edges
def extract_data(file):
    graph = []
    with open(file) as f:
        for line in f:
            split_line = line.split()
            # Save edges as int tuples (tail, head)
            edge = int(split_line[0]), int(split_line[1])
            graph.append(edge)
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
    return

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
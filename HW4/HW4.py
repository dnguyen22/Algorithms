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

# Generate graph from edges text file
graph = extract_data('SCC_test.txt')
# Run SCC algorithm on graph, return sizes of SCC
size_SCC = []
# Sort size_SCC from smallest to largest
size_SCC.sort()
# Print size of 5 largest SCCs
print(size_SCC[-5:])
print(graph)
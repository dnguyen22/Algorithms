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

graph = extract_data('SCC_test.txt')
print(graph)
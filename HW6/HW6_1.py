# HW6_1: 2-Sum Algorithm

# Returns graph from text file of weighted edges. Graph is in the form of an adjacency list dictionary with vertices as
#   keys and list of [edge weight, end vertex] as values
def extract_data(file):
    adjacency_list = {}
    with open(file) as f:
        for line in f:
            split_line = line.split()
            # Set starting vertex as key with empty list as value
            adjacency_list[int(split_line[0])] = []
            # edges contains list of list of [end vertices and edge weights]
            edges = split_line[1:]
            for edge in edges:
                split_edge = edge.split(',')
                adjacency_list[int(split_line[0])].append([int(split_edge[1]), int(split_edge[0])])
    return adjacency_list
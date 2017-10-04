# HW5: Dijkstra's Algorithm


# Returns graph from text file of weighted edges. Graph is in the form of an adjacency list dictionary with vertices as
#   keys and (end vertex, edge weight) tuples as values
def extract_data(file):
    graph = {}
    with open(file) as f:
        for line in f:
            split_line = line.split()
            # Set starting vertex as key with empty list as value
            graph[int(split_line[0])] = []
            # edges contains tuples of end vertices and edge weights
            edges = split_line[1:]
            for edge in edges:
                split_edge = edge.split(',')
                graph[int(split_line[0])].append((int(split_edge[0]), int(split_edge[1])))

    print(graph)
            # Save edges as int tail and head
            #tail = int(split_line[0])
            #head = int(split_line[1])

            # Add new node to graph; create new key if first time node appears
            #if tail in graph:
                #graph[tail].add(head)
            #else:
                #graph[tail] = set([head])
    #return graph

extract_data('dijkstraData.txt')

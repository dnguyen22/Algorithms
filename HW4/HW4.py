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
    def dfs(self, vertex, visited, leaders, lead):
        visited[vertex] = True
        if lead in leaders:
            leaders[lead] = leaders[lead] + 1
        else:
            leaders[lead] = 1
        for edge in self.adjacency_list[vertex]:
            if edge in visited and visited[edge] == False:
                self.dfs(edge, visited, leaders, lead)

sys.setrecursionlimit(300000)

# Generate graph from edges text file
graph = Graph()
graph.extract_data('SCC_test.txt', False)

# Generate reverse graph from edges text file
reversed_graph = Graph()
reversed_graph.extract_data('SCC_test.txt', True)

# Stack to record finishing times of graph
finishing_order = []
# Dictionary to keep track of visited vertices
visited_vertex = dict.fromkeys(set(graph.adjacency_list.keys()), False)

# Loop through vertices to calculate finishing times
for vert in graph.adjacency_list:
    if visited_vertex[vert] == False:
        graph.fill_order(vert, visited_vertex, finishing_order)

# Dictionary to keep track of visisted vertices for reverse graph
visited_vertex_reverse_graph = dict.fromkeys(set(reversed_graph.adjacency_list.keys()), False)

leaders = {}
print(finishing_order)

while finishing_order:
    v = finishing_order.pop()
    if visited_vertex_reverse_graph[v] == False:
        lead = v
        reversed_graph.dfs(v, visited_vertex_reverse_graph, leaders, lead)

# Top 5 sizes of strongly connected components
print(list(leaders.values())[-5:])


# HW8: k Clustering - Kruskal's Minimum Spanning Tree


class UnionFind:
    def __init__(self):
        self.parents = dict()
        self.ranks = dict()
        self.count_clusters = 0

    # Returns parent of vertex
    def find(self, vertex):
        # If vertex is not root, update parent to root
        if self.parents[vertex] != vertex:
            self.parents[vertex] = self.find(self.parents[vertex])
        return self.parents[vertex]

    # Unions both vertices into one group
    def union(self, vertex1, vertex2):
        # Get roots
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            # Add smaller rank to bigger rank tree
            if self.ranks[root1] > self.ranks[root2]:
                self.parents[root2] = root1
            else:
                self.parents[root1] = root2

            # If ranks are equal, add root1 tree to root2 tree and increase rank of bigger tree
            if self.ranks[root1] == self.ranks[root2]:
                self.ranks[root2] = self.ranks[root2] + 1

            # Decrement number of clusters
            self.count_clusters = self.count_clusters - 1

    # Add vertex to data structure
    def add(self, vertex):
        if vertex not in self.parents:
            self.parents[vertex] = vertex
            self.ranks[vertex] = 0
            self.count_clusters = self.count_clusters + 1


# Loops through file and adds vertices to UnionFind
def extract_data(file):
    uf = UnionFind()
    edges = []
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            split = line.split()
            uf.add(int(split[0]))
            uf.add(int(split[1]))
            edges.append((int(split[0]), int(split[1]), int(split[2])))
    return uf, edges


union_find, graph = extract_data('clustering1.txt')
# Set k, number of clusters
K = 4
# Sort edges by distance from shortest to longest
sorted_graph = sorted(graph, key=lambda distance: distance[2])

while union_find.count_clusters > K:
    smallest_edge = sorted_graph.pop(0)
    # Union two vertices (method already accounts for if edge is within cluster)
    union_find.union(smallest_edge[0], smallest_edge[1])

print(union_find.parents)
print(union_find.count_clusters)

for key in union_find.parents:
    if union_find.find(key) != 112:
        print('Key: ', key)
        print('Root: ', union_find.find(key))
        print()


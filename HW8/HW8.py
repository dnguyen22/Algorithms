# HW8: k Clustering - Kruskal's Minimum Spanning Tree


class UnionFind:
    def __init__(self):
        self.parents = dict()
        self.ranks = dict()

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

    # Add vertex to data structure
    def add(self, vertex):
        self.parents[vertex] = vertex
        self.ranks[vertex] = 0


# Loops through file and adds vertices to UnionFind
def extract_data(file):
    uf = UnionFind()
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            split = line.split()
            uf.add(int(split[0]))
            uf.add(int(split[1]))
    return uf


unionfind = extract_data('clustering1.txt')
print(unionfind.parents)
print(unionfind.ranks)
# HW9_2: Weighted Independent Sets - Dynamic Programming Intro


# Loops through file and adds vertices to UnionFind
def extract_data(file):
    weights = []
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            weights.append(int(line))
    return weights


vertices = extract_data('mwis.txt')
# Holds total weight of set, including set of 0 vertices
set_weight = [0, vertices[0]]
# Dynamic programming approach to find solution in O(n) time
for i in range(2, len(vertices)+1):
    set_weight.append(max(set_weight[i-1], set_weight[i-2] + vertices[i-1]))

# Set of vertices used in final answer set
independent_set = set()
index = len(vertices)
while index > 1:
    if set_weight[index] >= set_weight[index-1] + vertices[index-1]:
        index = index - 1
    else:
        independent_set.add(index)
        index = index - 2
print(len(vertices))
print(len(set_weight))
print(vertices)
print(set_weight)
print(independent_set)
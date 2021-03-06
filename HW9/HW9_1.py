# HW9: Huffman Encoding - Greedy Algorithms
import heapq


# Node for Huffman Encoding tree
class HuffmanNode:
    def __init__(self, left = None, right = None, root = None):
        self.l = left
        self.r = right
        self.root = root


# Loops through file and adds vertices to UnionFind
def extract_data(file):
    alphabet = []
    index = 0
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            alphabet.append((int(line), index))
            index = index + 1
    return alphabet


# Extract letter weights from file
letters = extract_data('huffman.txt')
# Initialize heap
heap = []
# Add letter weights to heap
for letter in letters:
    heapq.heappush(heap, letter)

print(heap)
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    node = HuffmanNode(left[1], right[1])
    heapq.heappush(heap,(left[0] + right[0], node))

tree = heapq.heappop(heap)
print(tree)


# Depth first search to get min depth of tree
def get_min_depth(root):
    if isinstance(root, int):
        return 0
    return min(get_min_depth(root.l), get_min_depth(root.r)) +1


# Depth first search to get max depth of tree
def get_max_depth(root):
    if isinstance(root, int):
        return 0
    return max(get_max_depth(root.l), get_max_depth(root.r)) + 1


print(get_min_depth(tree[1]))
print(get_max_depth(tree[1]))
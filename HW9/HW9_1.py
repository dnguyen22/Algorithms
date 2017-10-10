# HW9: Huffman Encoding - Greedy Algorithms
import heapq

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
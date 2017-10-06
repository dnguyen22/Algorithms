# HW6_2: Median Maintenance Algorithm
import heapq

# Store medians of numbers up to index i
medians = []
# Heap to store all low values. Supports extract max
low_heap = []
# Heap to store all high values. Supports extract min
high_heap = []
# Text file with integers
file = 'Median.txt'
# Loop through file
with open(file) as f:
    for line in f:
        next_value = int(line)

        # Initial value when both heaps are empty
        if not low_heap and not high_heap:
            heapq.heappush(high_heap, next_value)
        else:
            # TODO: Add new value to high heap if greater than smallest value. Add to low heap if less than highest value
            # TODO: Balance heaps
            # TODO: If index is odd, median is odd value from high heap or low heap. If index is even, median is from low heap
            # TODO: Add median to medians list

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
# Index
index = 0
# Loop through file
with open(file) as f:
    for line in f:
        next_value = int(line)
        index = index + 1

        # Initial value when both heaps are empty
        if not low_heap and not high_heap:
            heapq.heappush(high_heap, next_value)
        else:
            # Add new value to high heap if greater than smallest value. Add to low heap if less than highest value
            if next_value > high_heap[0]:
                heapq.heappush(high_heap, next_value)
            else:
                heapq.heappush(low_heap, -next_value)

            # Balance heaps
            if len(high_heap) - len(low_heap) > 1:
                heapq.heappush(low_heap, -(heapq.heappop(high_heap)))
            elif len(low_heap) - len(high_heap) > 1:
                heapq.heappush(high_heap, -(heapq.heappop(low_heap)))

        # If index is odd, median is odd value from high heap or low heap.
        #   If index is even, median is from low heap.
        if index % 2 == 1:
            if len(low_heap) > len(high_heap):
                medians.append(-low_heap[0])
            else:
                medians.append(high_heap[0])
        else:
            medians.append(-low_heap[0])

print("Medians: ")
print(medians)
print('Sum of Medians: ' + str(sum(medians)))
print('Sum mod 10000: ' + str(sum(medians) % 10000))


# HW10: Knapsack Problem - Dynamic Programming


# Loops through file and adds items to dictionary for fast lookups
def extract_data(file):
    dictionary = dict()
    index = 0
    with open(file) as f:
        text = f.readlines()
        # Extract data from header
        split = text[0].split()
        max_weight = int(split[0])
        count_items = int(split[1])
        # Skip first line (header)
        for line in text[1:]:
            split = line.split()
            # dictionary values are tuples of item (value, weight)
            dictionary[index] = (int(split[0]), int(split[1]))
            # Increment item index
            index = index + 1
    return dictionary, max_weight, count_items


# Items
items, MAX_WEIGHT, NUM_ITEMS = extract_data('knapsack1.txt')
# Set up dictionary for subproblem solutions with key 'XY'
#   where X is the item index and Y is the weight capacity of the bag
bag = {}
for i in range(MAX_WEIGHT):
    bag['0 ' + str(i)] = 0

for i in range(1, NUM_ITEMS):
    print(i)
print(items)
print(bag)
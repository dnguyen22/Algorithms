# HW10: Knapsack Problem - Dynamic Programming


# Loops through file and adds items to dictionary for fast lookups
def extract_data(file):
    dictionary = dict()
    index = 1
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
#   where X is the item index and Y is the weight capacity of the bag. Value is value of items
bag = {}
# Initialize bag for item 0
for i in range(MAX_WEIGHT + 1):
    bag['0 ' + str(i)] = 0
# Loop through subproblems (all items and all weights)
for i in range(1, NUM_ITEMS + 1):
    # Access weight of item for later use
    item_weight = items[i][1]
    for j in range(0, MAX_WEIGHT + 1):
        # For the case of adding current item to bag, calculate value
        if item_weight > j:
            # If item weight is heavier than bag weight allowance, do not add item
            add_item_case = 0
        else:
            # If item weight fits into bag, add item to bag. Add to optimal case for left over weight capacity
            add_item_case = bag[str(i-1) + ' ' + str(j-item_weight)] + items[i][0]
        bag[str(i) + ' ' + str(j)] = max(bag[str(i-1) + ' ' + str(j)], add_item_case)

# Set of vertices used in final answer set
items_in_bag_set = set()
item_index = NUM_ITEMS
weight_index = MAX_WEIGHT
while item_index > 0:
    if bag[str(item_index) + ' ' + str(weight_index)] != bag[str(item_index-1) + ' ' + str(weight_index)]:
        # Current item is in optimal bag
        items_in_bag_set.add(item_index)
        weight_index = weight_index - items[item_index][1]
    # Move to next item
    item_index = item_index - 1

print('Optimal Value: ' + str(bag[str(NUM_ITEMS) + ' ' + str(MAX_WEIGHT)]))
print('Items in optimal bag: ')
print(items_in_bag_set)
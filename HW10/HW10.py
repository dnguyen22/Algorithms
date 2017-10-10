# HW10: Knapsack Problem - Dynamic Programming


# Loops through file and adds items to dictionary for fast lookups
def extract_data(file):
    dictionary = dict()
    index = 0
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            split = line.split()
            # dictionary values are tuples of item (value, weight)
            dictionary[index] = (int(split[0]), int(split[1]))
            # Increment item index
            index = index + 1
    return dictionary


# Items
items = extract_data('knapsack1.txt')
print(items)
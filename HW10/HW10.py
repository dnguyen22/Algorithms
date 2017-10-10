# HW10: Knapsack Problem - Dynamic Programming

# Loops through file and adds items
def extract_data(file):
    i = []
    with open(file) as f:
        # Skip first line (header)
        j = f.readlines()[1:]
        for line in j:
            split = line.split()
            i.append((int(split[0]), int[split[1]]))
    return i

# Items
items = extract_data('knapsack1.txt')
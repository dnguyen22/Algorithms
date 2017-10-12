# HW12: Traveling Salesman Problem - Nearest Neighbor Heuristic


# Loops through file and adds locations to dictionary
def extract_data(file):
    dictionary = dict()
    with open(file) as f:
        text = f.readlines()
        # Extract data from header
        num_cities = int(text[0])
        # Skip first line (header)
        for line in text[1:]:
            split = line.split()
            # dictionary values are tuples of item (x-coordinate, y-coordinate)
            dictionary[int(split[0])] = (float(split[1]), float(split[2]))
    return dictionary, num_cities


# Cities
cities, NUM_CITIES = extract_data('nn.txt')
print(cities)
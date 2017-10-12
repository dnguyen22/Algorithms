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


# Computes squared Euclidean distance between two cities
def distance_squared(city1, city2):
    return (city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2


# Cities
cities, NUM_CITIES = extract_data('nn.txt')
# List of cities visited
tour_path = []
# Set of cities unexplored
unexplored = set(cities.keys())
# Set of cities explored
explored = set()
print(unexplored)
print(explored)
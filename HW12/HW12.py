# HW12: Traveling Salesman Problem - Nearest Neighbor Heuristic
import math


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
# Current city - start tour at city 1
current_city = 1
unexplored.remove(current_city)
explored.add(current_city)
tour_path.append(current_city)
# Loop through cities until all cities are added to tour
while unexplored:
    # Find minimum distance
    min_distance = math.inf
    closest_city = math.inf
    # Loop through unexplored cities to find next closest city
    for city in unexplored:
        new_distance = distance_squared(cities[current_city], cities[city])

        if new_distance < min_distance:
            min_distance = new_distance
            # In case of tie in distance, save city with lowest index
            closest_city = city

    # Travel to closest city. Update unexplored and explored sets, and current city
    unexplored.remove(closest_city)
    explored.add(closest_city)
    tour_path.append(closest_city)
    current_city = closest_city

print(explored)
print(unexplored)
print(tour_path)


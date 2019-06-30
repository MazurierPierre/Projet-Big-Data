import random
import copy


# Program Parameters
NB_CITY = 100
MAX_DISTANCE = 10


# Generate a complete graph (in matrix form) with random weights
def generate_matrix(nb_city, max_weight):
    matrix = [[None for i in range(nb_city)] for j in range(nb_city)]

    for i in range(nb_city):
        for j in range(nb_city):
            if i == j:
                matrix[i][j] = 0
                break
            else:
                matrix[i][j] = matrix[j][i] = random.randint(1, max_weight)

    return matrix


# Calculates the travel time for a given path
def path_travel_time(path, matrix):
    distance = x = 0

    for i in range(0, NB_CITY):
        distance = distance + matrix[x][path[i]]
        x = path[i]

    return distance


# Swaps radomly 2 elements in a path
def ran_swap(path):
    r0, r1 = random.sample(range(0, NB_CITY - 1), 2)

    temp = path[r1]
    path[r1] = path[r0]
    path[r0] = temp

    return path


# Calculates the shortest path, going through all nodes and back, passing only once per node in a complete graph
def simulated_annealing(matrix):
    temp = 4
    cooling_rate = 0.001
    d = 0

    total_history = []
    selected = []
    path = []

    # Make a "random" list of cities and paths
    for i in range(1, NB_CITY):
        path.append(i)
    path.append(0)

    # Calculate distance for the first path
    distance = path_travel_time(path, matrix)
    total_history.append(distance)
    selected.append(distance)

    while temp > 1:

        # randomly swap 2 cities
        new_path = ran_swap(copy.copy(path))

        # Calculate the new distance
        new_distance = path_travel_time(new_path, matrix)
        total_history.append(new_distance)

        # Compare both distance and new distance
        # if math.exp(distance - new_distance) / temp >= random.uniform(0, 1):
        if new_distance < distance:
            distance = new_distance
            path = new_path

        # Iterate
        selected.append(distance)
        temp = temp * (1 - cooling_rate)
        d = d + 1

    print("Itierations. . . . : ", d)

    return path, distance, total_history, selected


# Generate matrix and calculate optimal path
g = generate_matrix(NB_CITY, MAX_DISTANCE)
optimal_path, distance, history, selected = simulated_annealing(g)
print("Optimal Path . . . : ", optimal_path)
print("Total Distance . . : ", distance)

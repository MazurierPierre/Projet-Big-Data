import random
import copy
import time
import math
from Algorithmes import matrix as mtx


# Swaps radomly 2 elements in a path
def ran_swap(path):
    r0, r1 = random.sample(range(0, len(path) - 1), 2)

    temp = path[r1]
    path[r1] = path[r0]
    path[r0] = temp

    return path


# Calculates the shortest path, going through all nodes and back, passing only once per node in a complete graph
def simulated_annealing(matrix, temp, cooling_rate):
    ts = time.clock()
    iterations = 0

    total_history = []
    selected = []
    path = []

    # Make a "random" list of cities and paths
    for i in range(1, len(matrix)):
        path.append(i)
    path.append(0)

    # Calculate distance for the first path
    distance = mtx.path_weight(path, matrix)
    total_history.append(distance)
    selected.append(distance)

    while temp > 1:

        # randomly swap 2 cities
        new_path = ran_swap(copy.copy(path))

        # Calculate the new distance
        new_distance = mtx.path_weight(new_path, matrix)
        total_history.append(new_distance)

        # Compare both distance and new distance
        if math.exp(distance - new_distance) / temp >= random.uniform(0, 1):
            distance = new_distance
            path = new_path

        # Iterate
        selected.append(distance)
        temp = temp * (1 - cooling_rate)
        iterations = iterations + 1

    # Returns :
    #   path            The optimal path
    #   distance        The sum of the weights of the path
    #   time - ts       The time the algorithme took to calculate the path
    #   total_history   History of all the total weights of each path tested
    #   selected        History of all of the total weights of the selected paths
    return path, distance, time.clock() - ts, iterations, total_history, selected

import random
import time
import copy
import math
from Algorithmes import matrix as mtx


def ran_swap_arrays(path):

    source, target = random.sample(range(len(path)), 2)
    src_index = random.randint(0, len(path[source]) - 2)
    trg_index = random.randint(0, len(path[target]) - 2)

    if len(path[source]) > 2:
        path[target].insert(trg_index, path[source][src_index])
        path[source].pop(src_index)
    else:
        temp = path[target][trg_index]
        path[target][trg_index] = path[source][0]
        path[source][src_index] = temp

    return path


def simulated_annealing(matrix, nb_trucks, temperature, cool_rate):
    nb_city = len(matrix)
    global_path = []
    weight_history = [[] for i in range(nb_trucks)]
    distance_history = []
    ts = time.clock()
    iterations = 0

    # Get "random" path
    for i in range(1, nb_city):
        global_path.append(i)

    # Chop array in k arrays
    path = [[] for i in range(nb_trucks)]
    index = 0
    for i in range(nb_trucks):
        for j in range(int(nb_city / nb_trucks)):
            path[i].append(global_path[index])
            index = index + 1
        path[i].append(0)

    # Calculating total distance for the first path
    distance = 0
    for i in range(nb_trucks):
        path_weight = mtx.path_weight(path[i], matrix)
        distance = distance + path_weight
        weight_history[i].append(path_weight)

    distance_history.append(distance)

    while temperature >= 1:

        # Random swap value in both arrays
        new_path = ran_swap_arrays(copy.copy(path))

        # New distance calculations
        new_distance = 0
        for i in range(nb_trucks):
            path_weight = mtx.path_weight(new_path[i], matrix)
            new_distance = new_distance + path_weight
            weight_history[i].append(path_weight)

        # Acceptance function
        if math.exp(distance - new_distance) / temperature >= random.uniform(0, 1):

            # Keep new paths
            path = new_path
            distance = new_distance

        distance_history.append(distance)
        temperature = temperature * (1 - cool_rate)
        iterations = iterations + 1

    return path, distance, time.clock() - ts, iterations, distance_history, weight_history

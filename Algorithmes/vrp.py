import random
import copy
import matplotlib.pyplot as plt


NB_CITY = 10
NB_TRUCK = 3
MAX_DISTANCE = 10


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


def path_travel_time(path, matrix):
    distance = x = 0

    for i in range(0, len(path)):
        distance = distance + matrix[x][path[i]]
        x = path[i]

    return distance


def ran_swap_arrays(path1, path2):
    r0, r1 = random.sample(range(0, len(path1) - 1), 2)

    temp = path1[r1]
    path1[r1] = path2[r0]
    path2[r0] = temp

    return path1, path2


def sa_vrp(matrix, nb_trucks):
    global_path = []
    weight_history = [[] for i in range(NB_TRUCK)]

    # Get "random" path
    for i in range(1, NB_CITY):
        global_path.append(i)
    global_path.append(0)

    # Chop array in k equal length arrays
    path = [[] for i in range(nb_trucks)]
    index = 0
    for i in range(nb_trucks):
        for j in range(int(NB_CITY / nb_trucks)):
            path[i].append(global_path[index])
            index = index + 1
        path[i].append(0)

    # Calculate total weights for all k arrays
    weight = []
    for i in range(nb_trucks):
        weight.append(path_travel_time(path[i], matrix))

    for k in range(0, 200):
        # Select biggest and smallest index
        big = small = weight[0]
        i_big = i_small = 0
        for i in range(1, len(weight)):
            if weight[i] > big:
                big = weight[i]
                i_big = i
            if weight[i] < small:
                small = weight[i]
                i_small = i

        # Random swap value in both arrays
        new_path = copy.copy(path)
        new_path[i_small], new_path[i_big] = ran_swap_arrays(new_path[i_small], new_path[i_big])

        for i in range(NB_TRUCK):
            weight_history[i].append(weight[i])

        # Acceptance function
        if abs(path_travel_time(path[i_big], matrix) - path_travel_time(path[i_small], matrix)) < abs(weight[i_big] - weight[i_small]):

            # Update weights
            weight.clear()
            for i in range(nb_trucks):
                weight.append(path_travel_time(path[i], matrix))

            # Keep new paths
            path = new_path
        else:
            print()

    return path, weight, weight_history


# Generate matrix
g = generate_matrix(NB_CITY, MAX_DISTANCE)
p, w, h = sa_vrp(g, NB_TRUCK)

for i in range(NB_TRUCK):
    plt.plot(h[i])

plt.show()
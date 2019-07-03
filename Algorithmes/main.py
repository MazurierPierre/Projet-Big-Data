import matplotlib.pyplot as plt
from Algorithmes import matrix as mtx
from Algorithmes import tsp
from Algorithmes import vrp


# Matrix generation constants
NB_CITY = 5
MAX_DISTANCE = 9

# Simulated annealing constants
TEMPERATURE = 4
COOL_RATE = 0.01

# VRP constants
NB_TRUCK = 2


def run_tsp():
    # Generate matrix
    g = mtx.generate(NB_CITY, MAX_DISTANCE)

    # Run TSP
    path, distance, sa_duration, total_history, selected = tsp.simulated_annealing(g, TEMPERATURE, COOL_RATE)

    mtx.print_console(g)

    print("Optimal path : ", path)
    print("Total weight : ", distance)
    print("Run time     : ", sa_duration)

    mtx.plot(g)
    # plt.plot(total_history)
    # plt.plot(selected)

    plt.show()


def run_vrp():
    # Generate matrix
    g = mtx.generate(NB_CITY, MAX_DISTANCE)

    # Run VRP
    path, distance, sa_duration, distance_history = vrp.simulated_annealing(g, NB_TRUCK, TEMPERATURE, COOL_RATE)

    print("Optimal paths :")
    for i in range(NB_TRUCK):
        print("    Truck ", i, ":", path[i])

    print("Total weight :", distance)
    print("Run time     : ", sa_duration)

    mtx.print_console(g)
    mtx.plot(g)
    plt.show()

run_vrp()
import matplotlib.pyplot as plt
from Algorithmes import matrix as mtx
from Algorithmes import tsp
from Algorithmes import vrp
from Algorithmes import generateXLXS as dataset


# Matrix generation constants
NB_CITY = 10
MAX_DISTANCE = 9

# Simulated annealing constants
TEMPERATURE = 4
COOL_RATE = 0.001

# VRP constants
NB_TRUCK = 3


def run_tsp(exec_number):
    # Generate matrix
    g = mtx.generate(NB_CITY, MAX_DISTANCE)

    # Run TSP
    path, distance, sa_duration, iterations, total_history, selected = tsp.simulated_annealing(g, TEMPERATURE, COOL_RATE)

    # Save data
    save_data(exec_number, g, sa_duration, iterations, distance)

    print("Optimal path : ", path)
    print("Total weight : ", distance)
    print("Run time     : ", sa_duration)

    # mtx.print_console(g)
    # mtx.plot(g)
    plt.plot(total_history)
    plt.plot(selected)

    plt.show()


def run_vrp(exec_number):
    # Generate matrix
    g = mtx.generate(NB_CITY, MAX_DISTANCE)

    # Run VRP
    path, distance, sa_duration, iterations, distance_history = vrp.simulated_annealing(g, NB_TRUCK, TEMPERATURE, COOL_RATE)

    # Save data
    save_data(exec_number, g, sa_duration, iterations, distance)

    # print("Optimal paths :")
    # for i in range(NB_TRUCK):
    #     print("    Truck ", i, ":", path[i])

    # print("Total weight :", distance)
    # print("Run time     : ", sa_duration)

    # mtx.print_console(g)
    # mtx.plot(g)
    # plt.show()


def save_data(exec_number, matrix, algorithm_duration, iterations, distance):
    list_cities = []
    for i in range(NB_CITY):
        list_cities.append([i, "-", 0, 1])

    list_roads = []
    for i in range(NB_CITY):
        for j in range(NB_CITY):
            if matrix[i][j] == 0:
                break
            else:
                list_roads.append([i, j, matrix[i][j]])

    list_trucks = []
    for i in range(NB_TRUCK):
        list_trucks.append([i, 0])

    list_cargo = []

    list_params = [
        ["NB_CITY", NB_CITY, "Number of cities in the graph."],
        ["NB_TRUCKS", NB_TRUCK, "Max number of trucks that can be deployed"],
        ["NB_OBJECT", 0, "Number of different objects that can be dispatched / needed by cities"],
        ["DENSITY", 1, "Number of connections between cities (0 = none, 1 = All cities are interconnected)."],
        ["OBJECT_SIZE", 0, "Maximum object size"],
        ["RATIO_TRUCK", 1, "Ratio of small trucks (Big trucks is 1- RATIO_TRUCK)."],
        ["DISTANCE", MAX_DISTANCE, "Max distance between cities"],
        ["TEMPERATURE", TEMPERATURE, "Used for simulated annealing algorithm"],
        ["COOL_RATE", COOL_RATE, "Used for simulated annealing algorithm"]
    ]

    list_machine = [
        ["ResolvedTime", algorithm_duration],
        ["NbIterations", iterations],
        ["TotalOptimumDistance", distance]
    ]

    list_objects = []

    dataset.generatedataset(exec_number, list_cities, list_roads, list_trucks, list_cargo, list_params, list_machine,
                            list_objects)


print("NB_CITY 10")
for i in range(0, 10):
    run_vrp(i)

NB_CITY = 100
print("NB_CITY 100")
for i in range(10, 20):
    run_vrp(i)

NB_CITY = 1000
print("NB_CITY 1000")
for i in range(20, 30):
    run_vrp(i)


NB_CITY = 100
print("MAX DISTANCE 9")
for i in range(30, 40):
    run_vrp(i)

MAX_DISTANCE = 99
print("MAX DISTANCE 99")
for i in range(40, 50):
    run_vrp(i)


MAX_DISTANCE = 9
print("NB_TRUCKS 3")
for i in range(50, 60):
    run_vrp(i)

NB_TRUCK = 11
print("NB_TRUCKS 11")
for i in range(60, 70):
    run_vrp(i)

NB_TRUCK = 33
print("NB_TRUCKS 33")
for i in range(70, 80):
    run_vrp(i)


NB_TRUCK = 3
COOL_RATE = 0.01
print("COOLDOWN 0.01")
for i in range(80, 90):
    run_vrp(i)

COOL_RATE = 0.001
print("COOLDOWN 0.001")
for i in range(90, 100):
    run_vrp(i)

COOL_RATE = 0.0001
print("COOLDOWN 0.0001")
for i in range(100, 110):
    run_vrp(i)

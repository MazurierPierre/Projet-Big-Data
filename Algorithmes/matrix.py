import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def generate(nb_city, max_weight):
    matrix = [[None for i in range(nb_city)] for j in range(nb_city)]

    for i in range(nb_city):
        for j in range(nb_city):
            if i == j:
                matrix[i][j] = 0
                break
            else:
                matrix[i][j] = matrix[j][i] = random.randint(1, max_weight)

    return matrix


# Self explanatory, print a graph (in matrix form) to the console
def print_console(matrix):
    size = len(matrix[0])
    for i in range(0, size):
        for j in range(0, size):
            print(" ", matrix[i][j], end='')
        print()


# Calculates the travel time for a given path
def path_weight(path, matrix):
    distance = x = 0

    for i in range(0, len(path)):
        distance = distance + matrix[x][path[i]]
        x = path[i]

    return distance


def plot(matrix):
    converted_graph = nx.from_numpy_matrix(np.matrix(matrix))
    pos = nx.circular_layout(converted_graph)

    nx.draw(converted_graph, pos, with_labels=True)
    labels = nx.get_edge_attributes(converted_graph, 'weight')
    nx.draw_networkx_edge_labels(converted_graph, pos, edge_labels=labels)

import numpy as np
from random import random


def flatten(list):
    return [item for sublist in list for item in sublist]


def generate_population(dimentions, population_size, domain=100, clone=False):
    population = []

    if clone:
        individual = np.array([(random()-0.5)*2*domain for _ in range(dimentions)])
        population = [individual for _ in range(population_size)]
        return np.array(population)

    for _ in range(population_size):
        population.append(np.array([(random()-0.5)*2*domain for _ in range(dimentions)]))

    return np.array(population)


def split_coordinates(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    if len(points[0]) == 3:
        z_coords = [point[2] for point in points]
        return x_coords, y_coords, z_coords
    return x_coords, y_coords


def result_message(individual, fitness, color=None):
    argument = ["{:.3f}".format(coordinate) for coordinate in flatten(individual.tolist())]
    value = "{:.3f}".format(fitness)
    if color:
        return f'({color}) Best fitness: {value} for individual: {argument}'
    else:
        return f'Best fitness: {value} for individual: {argument}'

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

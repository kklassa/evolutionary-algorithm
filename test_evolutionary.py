from numpy.core.numeric import cross
from evolutionary import *
import numpy as np


def test_generate_population_one_dimention():
    population = generate_population(1, 100, 20)
    assert population.shape == (20, 1)


def test_generate_population_n_dimentions():
    population = generate_population(2, 100, 31)
    assert population.shape == (31, 2)

    population = generate_population(10, 100, 112)
    assert population.shape == (112, 10)


def test_evaluate_fitness():
    population = np.array([
        np.array([2]),
        np.array([-5]),
        np.array([-17]),
        np.array([0]),
        np.array([121])
    ])
    q = lambda x: x**2
    fitness = evaluate_fitness(q, population)
    assert fitness == [4, 25, 289, 0, 14641]


def test_find_best():
    population = np.array([
        np.array([2]),
        np.array([-5]),
        np.array([-17]),
        np.array([0]),
        np.array([121])
    ])
    q = lambda x: x**2
    fitness = evaluate_fitness(q, population)
    best_individual, best_fitness = find_best(population, fitness)
    assert best_individual == np.array([0])
    assert best_fitness == 0


def test_reproduction():
    population = generate_population(1, 50, 20)
    q = lambda x: x**2
    fitness = evaluate_fitness(q, population)
    offspring = reproduction(population, fitness, 20)
    assert offspring.shape == population.shape

    offspring = reproduction(population, fitness, 8)
    assert offspring.shape[0] == 8
    assert offspring.shape[1] == 1


def test_crossover():
    population = generate_population(2, 30, 20)
    offspring = crossover(population, 0.3, 0.1)
    assert offspring.shape == population.shape

    population = generate_population(3, 15, 5)
    offspring = crossover(population, 0.3, 0.1)
    assert offspring.shape == population.shape


def test_mutation():
    population = generate_population(3, 24, 12)
    offspring = mutation(population, 0.4, 1)
    assert offspring.shape == population.shape


def test_succession():
    population = generate_population(2, 100, 6)
    q = lambda x, y: x**2 + y
    fitness = evaluate_fitness(q, population)
    offspring = reproduction(population, fitness, 6)
    offspring_fitness = evaluate_fitness(q, offspring)

    successors, successors_fitness = succession(population, fitness, offspring, offspring_fitness, 1)
    assert successors.shape == population.shape
    assert len(successors_fitness) == successors.shape[0]

    successors, successors_fitness = succession(population, fitness, offspring, offspring_fitness, 4)
    assert successors.shape == population.shape
    assert len(successors_fitness) == successors.shape[0]

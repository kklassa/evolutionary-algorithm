import numpy as np
from random import random
from math import sin, cos, e


# global parameters
MUTATION_CHANCE = 1
ELITE_SIZE = 1
ALPHA = 0.1
TOURNAMENT_GROUP_SIZE = 2


def proportional_reproduction(population, fitness, population_size):
    # currently doesnt work for negative values
    fitness_sum = sum(fitness)
    probability_distribution = np.array([fitness/fitness_sum for fitness in fitness])
    draw = np.random.choice(
        int(population.size / population.shape[1]),
        population_size,
        p=probability_distribution)
    return np.array([population[index] for index in draw])


def reproduction(population, fitness, population_size):
    offspring = []
    for _ in range(population_size):
        tournament_group = np.random.choice(int(population.size / population.shape[1]), TOURNAMENT_GROUP_SIZE) # indexes of two individuals
        tournament_group_fitness = np.array([fitness[i] for i in tournament_group])
        best_individual_index = tournament_group[tournament_group_fitness.argsort()][0]
        offspring.append(population[best_individual_index])
    return np.array(offspring)


def evaluate_fitness(q, population):
    return [q(*individual) for individual in population]


def find_best(population, fitness):
    return population[np.where(fitness == np.amin(fitness))], np.amin(fitness)


def crossover(population, crossover_chance, crossover_factor):
    offspring = []
    no_individuals = int(population.size/population.shape[1])
    for i in range(0, no_individuals if no_individuals % 2 == 0 else no_individuals - 1, 2):
        if random() <= crossover_chance:
            offspring.append(crossover_factor * population[i] + (1-crossover_factor) * population[i+1])
            offspring.append(crossover_factor * population[i+1] + (1-crossover_factor) * population[i])
        else:
            offspring.extend(population[i:i+2])

    if no_individuals % 2 != 0:
        offspring.append(population[-1])

    return np.array(offspring)


def mutation(population, mutation_strength, mutation_chance):
    for individual in population:
        if random() <= mutation_chance:
            individual += mutation_strength * random()

    return population


def succession(population, fitness, offspring, offspring_fitness, elite_size):

    successors_pool = offspring
    successors_fitness_pool = offspring_fitness

    for _ in range(elite_size):
        best_individual, best_fitness = find_best(population, fitness)
        successors_pool = np.append(successors_pool, best_individual, axis=0)
        successors_fitness_pool = np.append(successors_fitness_pool, best_fitness)
        best_index = np.argwhere(population == best_individual).flatten()[0]
        population = np.delete(population, best_index, axis=0)
        fitness.pop(best_index)

    successors = successors_pool[successors_fitness_pool.argsort()][:-elite_size]
    successors_fitness = successors_fitness_pool[successors_fitness_pool.argsort()][:-elite_size].tolist()

    return successors, successors_fitness


def generate_population(dimentions, domain, population_size):
    population = []
    for _ in range(population_size):
        population.append(np.array([(random()-0.5)*2*domain for _ in range(dimentions)]))
    return(np.array(population))


def evolve(q,
        population,
        population_size,
        crossover_chance,
        crossover_factor,
        mutation_strength,
        mutation_chance,
        elite_size,
        max_iter):
    t = 0
    fitness = evaluate_fitness(q, population)
    best_individual, best_fitness = find_best(population, fitness)
    while t < max_iter:
        offspring = reproduction(population, fitness, population_size)
        offspring = crossover(population, crossover_chance, crossover_factor)
        offspring = mutation(offspring, mutation_strength, mutation_chance)
        offspring_fitness = evaluate_fitness(q, offspring)
        t_best_individual, t_best_fitness = find_best(offspring, offspring_fitness)
        if t_best_fitness < best_fitness:
            best_fitness = t_best_fitness
            best_individual = t_best_individual
        population, fitness = succession(population, fitness, offspring, offspring_fitness, elite_size)
        t += 1
    return best_individual, best_fitness


def main():

    bird = lambda x, y: sin(x) * e ** (1-cos(y)) ** 2 + cos(y) * e ** (1-sin(x)) ** 2 + (x - y) ** 2
    rosenbrock = lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    # z = lambda x, y, z, t, u, v:
    r = lambda x, y: 4 + (x-2)**2 + 2*y**2
    q = lambda x: x**4 + 2*x**3 - x + 1
    population = generate_population(2, 100, 20)

    X, F = evolve(rosenbrock, population, 20, 0.4, 0.1, 0.3, 1, 1, 1000)
    print(f'Found best fitness {F} for individual {X}')


if __name__ == "__main__":
    main()

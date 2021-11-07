import timeit


def measure_time(
    dimentions,
    population_size,
    function_name,
    crossover_chance,
    mutation_strength,
    max_iter,
    repetitions
):
    SETUP_CODE = f'''
from evolutionary import evolutionary, generate_population
from simulation import bird, rosenbrock, shubert
population = generate_population({dimentions}, {population_size})
    '''
    TEST_CODE = f'''
evolutionary({function_name},
            population,
            {population_size},
            {crossover_chance},
            {mutation_strength},
            {max_iter})
    '''
    #time = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1)
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=repetitions, number=1)
    return times

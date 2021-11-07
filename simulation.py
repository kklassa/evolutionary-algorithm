from evolutionary import evolutionary, evolutionary_for_plots, generate_population, flatten
from plotter import Plot3D, Plot2D
from functions import bird, rosenbrock, shubert
from time_evolutionary import measure_time


def split_coordinates(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    z_coords = [point[2] for point in points]
    return x_coords, y_coords, z_coords



def execution_time_measurement():

    population_sizes = [10, 25, 50, 75, 100, 150, 200]
    times = []

    for size in population_sizes:
        time = measure_time(2, size, 'bird', 0.6, 0.2, 100, 10)
        average_time = sum(time)/len(time)
        times.append(average_time)

    time_plot = Plot2D()
    time_plot.plot_points(population_sizes, times, 'black', 'population size', 'execution time')
    time_plot.show()


def result_message(individual, fitness, color=None):
    argument = ["{:.3f}".format(coordinate) for coordinate in flatten(individual.tolist())]
    value = "{:.3f}".format(fitness)
    if color:
        return f'({color}) Best fitness: {value} for individual: {argument}'
    else:
        return f'Best fitness: {value} for individual: {argument}'


def main():

    fitness_function = bird
    my_plot = Plot3D()
    my_plot.create(fitness_function, 30)

    population = generate_population(2, 10, 30)
    points, best_individual, best_fitness= evolutionary_for_plots(fitness_function, population, 10, 0.3, 0.1, 100)
    x_coords, y_coords, z_coords = split_coordinates(points)
    color = 'red'
    my_plot.add_points(x_coords, y_coords, z_coords, color, 3)
    my_plot.add_text(result_message(best_individual, best_fitness, color))

    population = generate_population(2, 10, 30)
    points, best_individual, best_fitness= evolutionary_for_plots(fitness_function, population, 10, 0.3, 0.3, 100)
    x_coords, y_coords, z_coords = split_coordinates(points)
    color = 'black'
    my_plot.add_points(x_coords, y_coords, z_coords, color, 3)
    my_plot.add_text(result_message(best_individual, best_fitness, color))

    population = generate_population(2, 10, 30)
    points, best_individual, best_fitness= evolutionary_for_plots(fitness_function, population, 10, 0.3, 0.6, 100)
    x_coords, y_coords, z_coords = split_coordinates(points)
    color = 'green'
    my_plot.add_points(x_coords, y_coords, z_coords, color, 3)
    my_plot.add_text(result_message(best_individual, best_fitness, color))


    my_plot.show()




if __name__=="__main__":
    main()

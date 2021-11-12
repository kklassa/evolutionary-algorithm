from evolutionary import evolutionary, evolutionary_for_plots, generate_population, flatten, evolutionary_plot_all
from plotter import Plot3D, Plot2D
from functions import bird, rosenbrock, shubert
from time_evolutionary import measure_time


def split_coordinates(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    if len(points[0]) == 3:
        z_coords = [point[2] for point in points]
        return x_coords, y_coords, z_coords
    return x_coords, y_coords



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

    fitness_function = shubert

    population = generate_population(2, 20, 1000)
    visited= evolutionary_plot_all(fitness_function, population, 20, 0.3, 0.1, 500)
    x_coords, y_coords = split_coordinates(visited)
    my_plot = Plot2D()
    my_plot.plot_points(x_coords, y_coords, "red")

    my_plot.show()

    # time = measure_time(2, 200, 'bird', 0.6, 0.2, 2000, 3)
    # average_time = sum(time)/len(time)
    # print(average_time)



if __name__=="__main__":
    main()

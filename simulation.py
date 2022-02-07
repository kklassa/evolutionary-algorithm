from evolutionary import evolutionary, evolutionary_for_plots, evolutionary_plot_all
from time_evolutionary import measure_time
from utils.functions import bird, rosenbrock, shubert
from utils.utilities import generate_population, split_coordinates, result_message
from utils.plotter import Plot2D, Plot3D


def main():

    fitness_function = bird

    my_plot = Plot3D()
    my_plot.create(fitness_function, 10)

    population = generate_population(2, 10, 10)
    iteration_best, best_individual, best_fitness = evolutionary_for_plots(fitness_function, population, 10, 0.3, 0.25, 100)

    print(f'Found best individual: {best_individual}\nwith fitness: {best_fitness}')

    x_coords, y_coords, z_coords = split_coordinates(iteration_best)
    my_plot.add_points(x_coords, y_coords, z_coords, 'red', 2)

    my_plot.show()



if __name__=="__main__":
    main()

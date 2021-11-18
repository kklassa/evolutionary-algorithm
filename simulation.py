from evolutionary import evolutionary, evolutionary_for_plots, evolutionary_plot_all
from time_evolutionary import measure_time
from utils.functions import bird, rosenbrock, shubert
from utils.utilities import generate_population, split_coordinates, result_message
from utils.plotter import Plot2D, Plot3D


def main():

    fitness_function = shubert

    plot = Plot3D()
    plot.create(fitness_function, 4)

    population = generate_population(2, 30, 1000)
    visited= evolutionary_plot_all(fitness_function, population, 30, 0.3, 0.25, 500)
    x_coords, y_coords = split_coordinates(visited)
    my_plot = Plot2D()
    my_plot.plot_points(x_coords, y_coords, "red")

    my_plot.show()



if __name__=="__main__":
    main()

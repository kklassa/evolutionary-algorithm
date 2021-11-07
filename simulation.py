from evolutionary import evolutionary, evolutionary_for_plots, generate_population
from plotter import create_3D_plot, add_points, show_plot, Plot3D
from functions import bird, rosenbrock, shubert
from time_evolutionary import measure_time


def split_coordinates(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    z_coords = [point[2] for point in points]
    return x_coords, y_coords, z_coords


def main():

    my_plot = Plot3D()
    my_plot.create(bird, 10)

    population = generate_population(2, 50, 10)
    points = evolutionary_for_plots(bird, population, 50, 0.3, 0.25, 1000)
    x_coords, y_coords, z_coords = split_coordinates(points)
    my_plot.add_points(x_coords, y_coords, z_coords, 'red')

    population = generate_population(2, 30, 10)
    points = evolutionary_for_plots(bird, population, 30, 0.3, 0.25, 500)
    x_coords, y_coords, z_coords = split_coordinates(points)
    my_plot.add_points(x_coords, y_coords, z_coords, 'black')

    my_plot.show()




if __name__=="__main__":
    main()

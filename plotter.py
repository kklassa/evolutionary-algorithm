import numpy as np
from matplotlib import pyplot as plt
from math import sin, cos, e


def plot3d(x_data, y_data, z_function, contour=False, surface=False):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    if contour:
        x_data, y_data = np.meshgrid(x_data, y_data)
        z_data = z_function(x_data, y_data)
        ax.contour3D(x_data, y_data, z_data, 50, cmap='binary')
    elif surface:
        x_data, y_data = np.meshgrid(x_data, y_data)
        z_data = z_function(x_data, y_data)
        ax.plot_surface(x_data, y_data, z_data, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    else:
        z_data = z_function(x_data, y_data)
        ax.plot3D(x_data, y_data, z_data, 'gray')
    plt.show()


def plot2d(x_data, y_data):
    fig = plt.figure()
    plt.plot(x_data, y_data, 'ro')
    plt.show()


def main():
    _list = np.linspace(-6, 6, 30)
    y_list = np.linspace(-6, 6, 30)
    z = lambda x, y: 4 + (x-2)**2 + 2*y**2

    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    bird = lambda x, y: sin(x) * e ** (1-cos(y)) ** 2 + cos(y) * e ** (1-sin(x)) ** 2 + (x - y) ** 2

    # plot3d(x, y, bird, False, True)

    print(bird(4.7, 3.15))


if __name__ == "__main__":
    main()
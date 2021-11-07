import numpy as np
import matplotlib.pyplot as plt


class Plot3D():
    def __init__(self):
        self.plot = None
        self.text_height = 0.01


    def create(self, func, domain):
        plt.rcParams['figure.figsize'] = (6, 4)
        plt.rcParams['figure.dpi'] = 150
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        ax.set_xlabel("x axis")
        ax.set_ylabel("y axis")
        ax.set_zlabel("z axis")
        x = np.linspace(-domain, domain, 100)
        y = np.linspace(-domain, domain, 100)
        X,Y= np.meshgrid(x,y)
        Z= func(X,Y)
        ax.plot_surface(X,Y,Z,alpha=0.4, cmap='cool')
        ax.contour3D(X,Y,Z)
        self.plot = ax


    def add_points(self, xpoints, ypoints, zpoints, color, size):
        self.plot.plot(xpoints, ypoints, zpoints, 'o', markersize=size, color=color)


    def add_text(self, text):
        plt.figtext(0.5, self.text_height, text, ha="center")
        self.text_height += 0.035

    def show(self):
        plt.show()


class Plot2D():
    def __init__(self):
        self.plot = None


    def plot_points(self, xpoints, ypoints, color, xlabel=None, ylabel=None):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        ax.plot(xpoints, ypoints, 'o', color=color)
        self.plot = ax


    def show(self):
        plt.show()


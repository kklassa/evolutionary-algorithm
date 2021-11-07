import numpy as np
import matplotlib.pyplot as plt


class Plot3D():
    def __init__(self):
        self.plot = None

    def create(self, func, domain):
        plt.rcParams['figure.figsize'] = (6,4)
        plt.rcParams['figure.dpi']=150
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        ax.set_xlabel("(x-axis)")
        ax.set_ylabel("(y-axis)")
        ax.set_zlabel("(z-axis)")
        x = np.linspace(-domain, domain, 100)
        y = np.linspace(-domain, domain, 100)
        X,Y= np.meshgrid(x,y)
        Z= func(X,Y)
        ax.plot_surface(X,Y,Z,alpha=0.6, cmap='winter')
        ax.contour3D(X,Y,Z)
        self.plot = ax

    def add_points(self, xpoints, ypoints, zpoints, color):
        self.plot.plot(xpoints, ypoints, zpoints, 'o', markersize=1, color=color)

    def show(self):
        plt.show()


def main():
    pass

if __name__=="__main__":
    main()

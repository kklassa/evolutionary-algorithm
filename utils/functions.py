import numpy as np


def bird(x, y):
    return np.sin(x)*(np.exp(1-np.cos(y))**2)+np.cos(y)*(np.exp(1-np.sin(x))**2)+(x-y)**2


def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def shubert(x, y):
    xsum = 0
    ysum = 0
    for i in range(1, 6):
        xsum += i * np.cos((i+1)*x + i)
        ysum += i * np.cos((i+1)*y + i)
    return xsum * ysum

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functools import reduce

import math
import random
import numpy as np

START = -4
END = 4

SECOND_VARIABLE_START = -6
SECOND_VARIABLE_END = 6

def find_equally_spaced(start, end, n):
    return [start + (end - start) * i / (n - 1) for i in range(n)]

def find_chebyshev_nodes(start, end, n):
    return [(start + end) / 2 + ((end - start) / 2) * math.cos((math.pi * (2 * i + 1)) / (2 * (n - 1) + 2)) \
        for i in range(0, n)]

def generate_random_points(f, start, end, n):
    x = sorted([random.uniform(start, end) for i in range(n)])
    y = [f(i) for i in x]
    
    return (x, y)

def draw_function(f, a, b, step):

    x = list()
    y = list()

    i = a
    while i <= b:
        x.append(i)
        y.append(f(i))

        i += step

    x_ticks = list()
    i = a
    while i <= b:
        x_ticks.append(i)

        i += 1

    plt.plot(x, y)
    plt.grid(True)
    plt.xticks(x_ticks)

    plt.show()

def draw_functions(a, b, step, *functions, points=None):
    
    x_ticks = list()
    i = a
    while i <= b:
        x_ticks.append(i)

        i += 1

    plt.grid(True)
    plt.xticks(x_ticks)

    if points != None:
        points_x, points_y = points

        plt.scatter(points_x, points_y, s=10)

    for function, function_name in functions:
        x = list()
        y = list()

        i = a
        while i <= b:
            x.append(i)
            y.append(function(i))

            i += step

        plt.plot(x, y, label=function_name)

    plt.legend()

    plt.show()

def draw_two_variables_fuctions(grid, *functions):
    x_grid, y_grid = grid

    b = np.array(x_grid)
    d = np.array(y_grid)
    nu = np.zeros( (b.size, d.size) )

    for function, function_name in functions:
        counter_y = 0
        for deta in d:
            counter_x = 0
            for beta in b:
                nu[counter_x, counter_y] = function(beta, deta)

                counter_x += 1
            counter_y += 1

        X, Y = np.meshgrid(b, d)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')
        ax.set_zlim(-6, 6)
        ax.plot_surface(X, Y, nu)

    plt.show()

def count_step(i):
    return 8 / (4 ** i)
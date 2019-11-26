import random
import math

from function import *
from utils import *

NUMBER_OF_POINTS = 40

def combination(n, i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

def bernstein_polynom(n, i, t):
    return combination(n, i) * (t ** i) * ((1 - t) ** (n - i))

def find_bezier_curve(f, start, end, n):
    q1 = sorted([random.uniform(start, end) for i in range(n)])
    q2 = [f(q) for q in q1]

    bezier_y = [sum([bernstein_polynom(n, i, t) * q for i, q in enumerate(q2)])
        for t in [i / n for i in range(n)]]

    return (q1, bezier_y)

def draw_bezier_curve_with_function(bezier_curve_points, f, start, end, step):
    x_ticks = list()
    i = start
    while i <= end:
        x_ticks.append(i)

        i += 1

    plt.grid(True)
    plt.xticks(x_ticks)

    bezier_x, bezier_y = bezier_curve_points
    plt.plot(bezier_x, bezier_y, label="Bezier curve")

    x = list()
    y = list()

    i = start
    while i <= end:
        x.append(i)
        y.append(f(i))

        i += 0.01

    plt.plot(x, y, label="Original function")

    plt.legend()

    plt.show()

if __name__ == "__main__":
    bezier_curve_points = find_bezier_curve(f, START, END, NUMBER_OF_POINTS)

    draw_bezier_curve_with_function(bezier_curve_points, f, START, END, 0.01)
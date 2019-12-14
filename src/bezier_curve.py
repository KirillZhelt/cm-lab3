import math

from function import *
from utils import *

NUMBER_OF_POINTS = 40
NUMBER_OF_T = 100

def combination(n, i):
    return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

def bernstein_polynom(n, i, t):
    return combination(n, i) * (t ** i) * ((1 - t) ** (n - i))

def find_bezier_curve(random_points, number_of_t):

    q1, q2 = random_points

    n = len(q1)

    bezier_y = [sum([bernstein_polynom(n - 1, i, t) * q for i, q in enumerate(q2)])
        for t in [i / number_of_t for i in range(number_of_t)]]

    bezier_x = [sum([bernstein_polynom(n - 1, i, t) * q for i, q in enumerate(q1)])
        for t in [i / number_of_t for i in range(number_of_t)]]

    return (bezier_x, bezier_y)

def draw_bezier_curve_with_function(initial_points, bezier_curve_points, f, start, end, step):
    x_ticks = list()
    i = start
    while i <= end:
        x_ticks.append(i)

        i += 1

    plt.grid(True)
    plt.xticks(x_ticks)

    initial_x, initial_y = initial_points

    plt.scatter(initial_x, initial_y, s=10)

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
    random_points = generate_random_points(f, START, END, NUMBER_OF_POINTS)

    bezier_curve_points = find_bezier_curve(random_points, NUMBER_OF_T)

    draw_bezier_curve_with_function(random_points, bezier_curve_points, f, START, END, 0.01)

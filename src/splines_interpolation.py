from scipy import linalg

from function import *
from utils import *

def spline_builder(alpha, beta, gamma, delta, xi):

    def spline(x):
        return alpha + beta * (x - xi) + (gamma / 2) * (x - xi) ** 2 + (delta / 6) * (x - xi) ** 3 

    return spline

def spline_system_builder(splines, nodes):
    def system(x):
        for i in range(1, len(nodes)):
            if nodes[i - 1] <= x <= nodes[i]:
                return splines[i - 1](x)

        raise Exception("x is out of range")

    return system

def divided_differences(f, x0, x1, x2):
    return f(x2) / ((x2 - x1) * (x2 - x0)) + f(x1) / ((x1 - x2) * (x1 - x0)) + \
         f(x0) / ((x0 - x2) * (x0 - x1))

def spline_interpolation(f, nodes):
    n = len(nodes) - 1

    h = [nodes[i] - nodes[i - 1] for i in range(1, n + 1)]
    e = [h[i] / (h[i - 1] + h[i]) for i in range(1, n - 1)]
    c = [h[i - 1] / (h[i - 1] + h[i]) for i in range(2, n)]

    b = [6 * divided_differences(f, nodes[i - 1], nodes[i], nodes[i + 1]) for i in range(1, n)]

    m = [[2 if i == j else 0 for i in range(n - 1)] for j in range(n - 1)]

    for i in range(1, n - 1):
        m[i - 1][i] = e[i - 1]

    for i in range(2, n):
        m[i - 1][i - 2] = c[i - 2]

    gammas = list(linalg.solve(m, b, assume_a='sym'))

    gammas = [0] + gammas + [0]

    alphas = [f(nodes[i]) for i in range(1, n + 1)]

    betas = [(alphas[i - 1] - alphas[i - 2]) / h[i - 1] + ((2 * gammas[i] + gammas[i - 1]) / 6) * h[i - 1] \
        for i in range(1, n + 1)]

    deltas = [(gammas[i] - gammas[i - 1]) / h[i - 1] for i in range(1, n + 1)]

    splines = [spline_builder(alphas[i - 1], betas[i - 1], gammas[i], deltas[i - 1], nodes[i]) \
         for i in range(1, n + 1)]

    return spline_system_builder(splines, nodes)

if __name__ == "__main__":
    equally_spaced_nodes = find_equally_spaced(START, END, 6)

    splines = spline_interpolation(f, equally_spaced_nodes)

    draw_functions(START, END, 0.01, (splines, "Splines"), (f, "Function to interpolate"))
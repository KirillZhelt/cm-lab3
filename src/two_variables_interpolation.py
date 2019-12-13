from functools import reduce

from function import *
from utils import *
from splines_interpolation import spline_intepolation_coefs, spline_interpolation

def generate_grid(n, x_start, x_end, y_start, y_end):
    x = find_equally_spaced(x_start, x_end, n)
    y = find_equally_spaced(y_start, y_end, n)

    return (x, y)

def lagrange_basis(i, nodes, point):
    
    return reduce((lambda a, b: a * b), [(point - nodes[p]) / (nodes[i] - nodes[p]) \
        for p in range(len(nodes)) if p != i])

def interpolate_two_variables_function(g, grid):
    x_nodes, y_nodes = grid

    n = len(x_nodes)
    m = len(y_nodes)

    z = [[g(x_nodes[i], y_nodes[j]) for j in range(m)] for i in range(n)]

    def lagrange_polynom_function(x, y):
        result = 0

        for i in range(n):
            for j in range(m):
                tmp = z[i][j] * \
                    lagrange_basis(i, x_nodes, x) * lagrange_basis(j, y_nodes, y)

                result += tmp

        return result

    return lagrange_polynom_function

def two_variables_spline_builder(alpha, beta, gamma, delta, xi):
    def spline(x, y):
        return alpha(y) + beta(y) * (x - xi) + (gamma(y) / 2) * (x - xi) ** 2 + \
            (delta(y) / 6) * (x - xi) ** 3 

    return spline

def two_variables_spline_system_builder(splines, nodes):
    def system(x, y):
        for i in range(1, len(nodes)):
            if nodes[i - 1] <= x <= nodes[i]:
                return splines[i - 1](x, y)

        raise Exception("x is out of range")

    return system

def splines_two_variables_function_interpolation(g, grid):
    x_nodes, y_nodes = grid

    splines_for_y = []
    for y in y_nodes:
        splines_for_y.append(spline_intepolation_coefs(lambda x: g(x, y), x_nodes))

    n = len(x_nodes) - 1

    coefs_interpolated = [[], [], [], []]
    for i in range(4):
        # alphas, betas, gammas, deltas

        for j in range(n):
            # for each segment
            coefs = [splines_for_y[k][i][j] for k in range(len(splines_for_y))]

            def coef(y):
                return coefs[y_nodes.index(y)]

            coefs_interpolated[i].append(spline_interpolation(coef, y_nodes))            

    splines = [two_variables_spline_builder(coefs_interpolated[0][i], coefs_interpolated[1][i], \
        coefs_interpolated[2][i], coefs_interpolated[3][i], x_nodes[i + 1]) for i in range(n)]

    return two_variables_spline_system_builder(splines, x_nodes)

if __name__ == "__main__":
    grid = generate_grid(18, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)

    interpolation = interpolate_two_variables_function(g, grid)

    splines = splines_two_variables_function_interpolation(g, grid)

    grid_to_draw = generate_grid(20, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)
    draw_two_variables_fuctions(grid_to_draw, (splines, "Splines"), \
        (g, "Original function"), (interpolation, "Lagrange"))



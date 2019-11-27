from functools import reduce

from function import *
from utils import *

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

    def lagrange_polynom_function(x, y):
        result = 0

        for i in range(n):
            for j in range(m):
                tmp = g(x_nodes[i], y_nodes[j]) * \
                    lagrange_basis(i, x_nodes, x) * lagrange_basis(j, y_nodes, y)

                result += tmp

        return result

    return lagrange_polynom_function


if __name__ == "__main__":
    grid = generate_grid(12, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)

    interpolation = interpolate_two_variables_function(g, grid)

    grid_to_draw = generate_grid(20, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)
    draw_two_variables_fuctions(grid_to_draw, (interpolation, "Interpolation"), \
        (g, "Original function"))


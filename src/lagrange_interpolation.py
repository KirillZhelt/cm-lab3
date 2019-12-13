from function import *
from utils import *

def lagrange_interpolation(f, nodes):
    multiplier_parts = [f(node) / reduce(lambda x, y: x * y, \
        [node - nodes[j] for j in range(len(nodes)) if i != j]) \
            for i, node in enumerate(nodes)]

    def lagrange_polynom_function(x):
        result = 0
        
        for i, node in enumerate(nodes):
            sum_part = multiplier_parts[i]

            for j in range(len(nodes)):
                if i != j:
                    sum_part *= (x - nodes[j])

            result += sum_part

        return result

    return lagrange_polynom_function

if __name__ == "__main__":
    equally_spaced_nodes = find_equally_spaced(START, END, 18)
    chebyshev_nodes = find_chebyshev_nodes(START, END, 18)

    lagrange_polynom_from_equally_spaced_nodes = lagrange_interpolation(f, \
        equally_spaced_nodes)

    lagrange_polynom_from_chebyshev_nodes = lagrange_interpolation(f, \
        chebyshev_nodes)

    draw_functions(START, END, 0.01, (lagrange_polynom_from_equally_spaced_nodes, "Lagrange polynom (equally spaced nodes)"), \
        (f, "Function to interpolate"))

    draw_functions(START, END, 0.01, (lagrange_polynom_from_chebyshev_nodes, "Lagrange polynom (chebyshev nodes)"), \
        (f, "Function to interpolate"))


    




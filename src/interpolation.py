
from function import *

START = -4
END = 4

def lagrange_interpolation(f, nodes):
    def lagrange_polynom_function(x):
        result = 0
        
        for i, node in enumerate(nodes):
            sum_part = f(node)

            for j in range(len(nodes)):
                if i != j:
                    sum_part *= (x - nodes[j]) / (node - nodes[j])

            result += sum_part

        return result

    return lagrange_polynom_function

def find_equally_spaced(start, end, n):
    return [start + (end - start) * i / (n - 1) for i in range(n)]

def find_chebyshev_nodes():
    pass

if __name__ == "__main__":
    print(find_equally_spaced(START, END, 6))

    lagrange_polynom = lagrange_interpolation(f, find_equally_spaced(START, END, 6))

    draw_functions(START, END, 0.01, (lagrange_polynom, "Lagrange polynom"), \
        (f, "Function to interpolate"))


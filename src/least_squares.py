from scipy import linalg

from function import *
from utils import *

def least_squares(random_points, max_deg):
    random_x, random_y = random_points
    
    # max_deg = 2 -> n = 3

    n = max_deg + 1

    m = [ [sum([ x ** i * x ** j for x in random_x]) for j in range(n)] for i in range(n) ]

    b = [ sum([x ** i * random_y[k]  for k, x in enumerate(random_x)]) for i in range(n) ]

    alphas = list(linalg.solve(m, b, assume_a="sym"))

    def least_squares_function(x):
        return sum([ alpha * x ** i for i, alpha in enumerate(alphas) ])

    return least_squares_function


if __name__ == "__main__":
    random_points = generate_random_points(f, START, END, 100)

    least_squares_approximation = least_squares(random_points, 3)

    draw_functions(START, END, 0.01, (least_squares_approximation, "Least squares"), \
        (f, "Original function"), points=random_points)

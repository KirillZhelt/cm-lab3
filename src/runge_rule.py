from math import ceil

from function import *

from equally_spaced_integration import simpson, A, B, EXACT_VALUE
from gauss_integration import gauss, SEVEN_NODES, SEVEN_WEIGHTS

SIMPSON_P = 4

# TODO: какой показатель точности у гаусса на 7 узлах

def runge_rule(integrate, p, f, a, b, accuracy):
    N1 = 5
    N2 = 10

    h1 = (b - a) / N1

    q1 = integrate(f, a, b, h1)

    while True:
        h2 = (b - a) / N2
        q2 = integrate(f, a, b, h2)

        R = ((q2 - q1) * h2 ** p) / (h1 ** p - h2 ** p) 

        if abs(R) <= accuracy:
            return q2

        N = int(ceil((abs(R) / accuracy) ** (1 / p) * N2))

        N1 = N2
        h1 = h2
        q1 = q2

        N2 = N


if __name__ == "__main__":
    print(runge_rule(simpson, SIMPSON_P, f, A, B, 0.000000001) - EXACT_VALUE)

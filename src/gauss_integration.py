from function import *
from utils import *

A = -4
B = 4

TWO_NODES = [-0.577350, 0.577350]
TWO_WEIGHTS = [1, 1]

THREE_NODES = [-0.774597, 0.0, 0.774597]
THREE_WEIGHTS = [0.555556, 0.888889, 0.555556]

FOUR_NODES = [-0.861136 ,-0.339981, 0.339981, 0.861136]
FOUR_WEIGHTS = [0.347855, 0.652145, 0.652145, 0.347855]

FIVE_NODES = [-0.906180, -0.538469, 0.0, 0.538469, 0.906180]
FIVE_WEIGHTS = [0.236927, 0.478629, 0.568889, 0.478629, 0.236927]

SIX_NODES = [-0.932470, -0.661209, -0.238619, 0.238619, 0.661209, 0.932470]
SIX_WEIGHTS = [0.17324, 0.360762, 0.467914, 0.467914, 0.360762, 0.17324]

SEVEN_NODES = [0.41796, 0.38183, 0.279705, 0.129485, 0.38183, 0.279705, 0.129485]
SEVEN_WEIGHTS = [0, -0.405845, -0.7415312, -0.949108, 0.4058451, 0.741531, 0.9491079]

def gauss(f, a, b, nodes, weights):
    nodes = list(map(lambda x: (a + b) / 2 + (b - a) * x / 2, nodes))

    return (b - a) * sum(weights[i] * f(x) for i, x in enumerate(nodes)) / 2

def composite_gauss(f, a, b, nodes, weights, h):
    n = int((b - a) / h)

    return sum(gauss(f, a + (i - 1) * h, a + i * h, nodes, weights) for i in range(1, n + 1))

if __name__ == "__main__":
    i = 10

    print(composite_gauss(f, A, B, TWO_NODES, TWO_WEIGHTS, count_step(i)))

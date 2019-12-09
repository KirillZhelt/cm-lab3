from function import *
from utils import *

A = -4
B = 4

EXACT_VALUE = 4.967532679086564

TWO_NODES = [-0.5773502691896257, 0.5773502691896257]
TWO_WEIGHTS = [1, 1]

THREE_NODES = [0.0000000000000000, -0.7745966692414834, 0.7745966692414834]
THREE_WEIGHTS = [0.8888888888888888, 0.5555555555555556, 0.5555555555555556]

FOUR_NODES = [-0.3399810435848563, 0.3399810435848563, -0.8611363115940526, 0.8611363115940526]
FOUR_WEIGHTS = [0.6521451548625461, 0.6521451548625461, 0.3478548451374538, 0.3478548451374538]

FIVE_NODES = [0.0000000000000000, -0.5384693101056831, 0.5384693101056831, -0.9061798459386640, \
    0.9061798459386640]
FIVE_WEIGHTS = [0.5688888888888889, 0.4786286704993665, 0.4786286704993665, 0.2369268850561891, \
    0.2369268850561891]

SIX_NODES = [0.6612093864662645, -0.6612093864662645, -0.2386191860831969, 0.2386191860831969, \
    -0.9324695142031521, 0.9324695142031521]
SIX_WEIGHTS = [0.3607615730481386, 0.3607615730481386, 0.4679139345726910, 0.4679139345726910, \
    0.1713244923791704, 0.1713244923791704]

SEVEN_NODES = [0.0000000000000000, 0.4058451513773972, -0.4058451513773972, -0.7415311855993945, \
    0.7415311855993945, -0.9491079123427585, 0.9491079123427585]
SEVEN_WEIGHTS = [0.4179591836734694, 0.3818300505051189, 0.3818300505051189, 0.2797053914892766, 0.2797053914892766, \
    0.1294849661688697, 0.1294849661688697]

def gauss(f, a, b, nodes, weights):
    nodes = list(map(lambda x: (a + b) / 2 + (b - a) * x / 2, nodes))

    return (b - a) * sum(weights[i] * f(x) for i, x in enumerate(nodes)) / 2

def composite_gauss(f, a, b, nodes, weights, h):
    n = int((b - a) / h)

    return sum(gauss(f, a + (i - 1) * h, a + i * h, nodes, weights) for i in range(1, n + 1))

if __name__ == "__main__":
    i = 10

    print("Gauss2: " + str(\
        abs(composite_gauss(f, A, B, TWO_NODES, TWO_WEIGHTS, count_step(i)) - EXACT_VALUE)))
    print("Gauss3: " + str(\
        abs(composite_gauss(f, A, B, THREE_NODES, THREE_WEIGHTS, count_step(i)) - EXACT_VALUE)))
    print("Gauss4: " + str(\
        abs(composite_gauss(f, A, B, FOUR_NODES, FOUR_WEIGHTS, count_step(i)) - EXACT_VALUE)))
    print("Gauss5: " + str(\
        abs(composite_gauss(f, A, B, FIVE_NODES, FIVE_WEIGHTS, count_step(i)) - EXACT_VALUE)))
    print("Gauss6: " + str(\
        abs(composite_gauss(f, A, B, SIX_NODES, SIX_WEIGHTS, count_step(i)) - EXACT_VALUE)))
    print("Gauss7: " + str(\
        abs(composite_gauss(f, A, B, SEVEN_NODES, SEVEN_WEIGHTS, count_step(i)) - EXACT_VALUE)))    
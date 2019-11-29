import numpy as np

from function import *

A = -4
B = 4

def count_step(i):
    return 8 / (4 ** i)

def build_sequence(a, h, n):
    result = a

    for i in range(int(n)):
        yield result
        result += h

def left_rectangles(f, a, b, h):
    return h * sum([ f(x) for x in build_sequence(a, h, (b - a) / h) ])

def right_rectangles(f, a, b, h):
    return h * sum([ f(x) for x in build_sequence(a + h, h, (b - a) / h) ])

def middle_rectangles(f, a, b, h):
    return h * sum([ f(a + (k - 0.5) * h) for k in range(1, int((b - a) / h) + 1) ])

def trapezoid(f, a, b, h):
    return (h / 2) * (f(a) + 2 * sum([ f(a + k * h) for k in range(1, int((b - a) / h)) ]) + f(b))

if __name__ == "__main__":
    i = 10

    print(left_rectangles(f, A, B, count_step(i)))
    print(right_rectangles(f, A, B, count_step(i)))
    print(middle_rectangles(f, A, B, count_step(i)))
    print(trapezoid(f, A, B, count_step(i)))
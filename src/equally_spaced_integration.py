import numpy as np

from function import *

A = -4
B = 4

FIVE_POINTS = [7, 32, 12, 32, 7]

SEVEN_POINTS = [41, 216, 27, 272, 27, 216, 41]

NINE_POINTS = [989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989]

ELEVEN_POINTS = [16067, 106300, -48525, 272400, -260550, 427368, -260550, 272400, -48525, 106300, 16067]

THIRTEEN_POINTS = [1364651, 9903168, -7587864, 35725120, -51491295, 87516288, -87797136, 87516288, \
    -51491295, 35725120, -7587864, 9903168, 1364651]

FIFTEEN_POINTS = [90241897, 710986864, -770720657, 3501442784, -6625093363, 12630121616, -16802270373, \
    19534438464, -16802270373, 12630121616, -6625093363, 3501442784, -770720657, 710986864, 90241897]

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

def simpson(f, a, b, h):
    if int((b - a) / h) < 3:
        return None

    return (h / 3) * (sum([ f(a + (k - 1) * h) + 4 * f(a + k * h) + f(a + (k + 1) * h) \
        for k in range(1, int((b - a) / h), 2) ]))

def newton_cotes(f, a, b, h, coefs):
    if int((b - a) / h) < len(coefs):
        return None

    n = len(coefs) - 1
    
    return ((n * h) / sum(coefs)) * sum(sum([coefs[i] * f(a + (i + j) * h) ]) for i in range(0, n + 1) \
        for j in range(1, int((b - a) / h) + 1, n))

if __name__ == "__main__":
    i = 3

    print(left_rectangles(f, A, B, count_step(i)))
    print(right_rectangles(f, A, B, count_step(i)))
    print(middle_rectangles(f, A, B, count_step(i)))
    print(trapezoid(f, A, B, count_step(i)))
    print(simpson(f, A, B, count_step(i)))
    print(newton_cotes(f, A, B, count_step(i), FIVE_POINTS))
    print(newton_cotes(f, A, B, count_step(i), SEVEN_POINTS))
    print(newton_cotes(f, A, B, count_step(i), NINE_POINTS))
    print(newton_cotes(f, A, B, count_step(i), ELEVEN_POINTS))
    print(newton_cotes(f, A, B, count_step(i), THIRTEEN_POINTS))
    print(newton_cotes(f, A, B, count_step(i), FIFTEEN_POINTS))

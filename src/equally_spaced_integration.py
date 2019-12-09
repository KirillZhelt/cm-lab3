import numpy as np

from function import *
from utils import *

A = -4
B = 4

EXACT_VALUE = 4.967532679086564

FIVE_POINTS = [7, 32, 12, 32, 7]
FIVE_POINTS_COEF = 2 / 45

SEVEN_POINTS = [41, 216, 27, 272, 27, 216, 41]
SEVEN_POINTS_COEF = 1 / 140

NINE_POINTS = [989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989]
NINE_POINTS_COEF = 4 / 14175

ELEVEN_POINTS = [16067, 106300, -48525, 272400, -260550, 427368, -260550, 272400, -48525, 106300, 16067]
ELEVEN_POINTS_COEF = 5 / 299376

THIRTEEN_POINTS = [1364651, 9903168, -7587864, 35725120, -51491295, 87516288, -87797136, 87516288, \
    -51491295, 35725120, -7587864, 9903168, 1364651]
THIRTEEN_POINTS_COEF = 1 / 5255250

FIFTEEN_POINTS = [90241897, 710986864, -770720657, 3501442784, -6625093363, 12630121616, -16802270373, \
    19534438464, -16802270373, 12630121616, -6625093363, 3501442784, -770720657, 710986864, 90241897]
FIFTEEN_POINTS_COEF = 7 / 2501928000 

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

def simpson(f, a, b):
    return ((b - a) / 6) * (f(a) + 4 * f((a + b) / 2) + f(b))

def composite_simpson(f, a, b, h):
    n = int((b - a) / h) 

    return sum(simpson(f, a + (i - 1) * h, a + i * h) for i in range(1, n + 1))

def newton_cotes_basic(f, a, b, nodes_coefs, coef):
    h = (b - a) / (len(nodes_coefs) - 1)

    return (b - a) * (coef / (len(nodes_coefs) - 1)) * sum(nodes_coefs[i] * f(a + i * h) for i in range(0, len(nodes_coefs)))

def newton_cotes(f, a, b, h, nodes_coefs, coef):
    n = int((b - a) / h) 
    
    return sum(newton_cotes_basic(f, a + (i - 1) * h, a + i * h, nodes_coefs, coef) for i in range(1, n + 1))  
 
if __name__ == "__main__":
    i = 10

    print("Left retangles: " + str(abs(left_rectangles(f, A, B, count_step(i)) - EXACT_VALUE)))
    print("Right retangles: " + str(abs(right_rectangles(f, A, B, count_step(i)) - EXACT_VALUE)))
    print("Middle retangles: " + str(abs(middle_rectangles(f, A, B, count_step(i)) - EXACT_VALUE)))
    print("Trapezoid: " + str(abs(trapezoid(f, A, B, count_step(i)) - EXACT_VALUE)))
    print("Simpson: " + str(abs(composite_simpson(f, A, B, count_step(i)) - EXACT_VALUE)))
    print("Newton-Cotes3: " + str(abs(newton_cotes(f, A, B, count_step(i), [1, 4, 1], 1 / 3) - EXACT_VALUE)))
    print("Newton-Cotes5: " + str(abs(newton_cotes(f, A, B, count_step(i), FIVE_POINTS, FIVE_POINTS_COEF) - EXACT_VALUE)))
    print("Newton-Cotes7: " + str(abs(newton_cotes(f, A, B, count_step(i), SEVEN_POINTS, SEVEN_POINTS_COEF) - EXACT_VALUE)))
    print("Newton-Cotes9: " + str(abs(newton_cotes(f, A, B, count_step(i), NINE_POINTS, NINE_POINTS_COEF) - EXACT_VALUE)))
    print("Newton-Cotes11: " + str(abs(newton_cotes(f, A, B, count_step(i), ELEVEN_POINTS, ELEVEN_POINTS_COEF) - EXACT_VALUE)))
    print("Newton-Cotes13: " + str(abs(newton_cotes(f, A, B, count_step(i), THIRTEEN_POINTS, THIRTEEN_POINTS_COEF) - EXACT_VALUE)))
    print("Newton-Cotes15: " + str(abs(newton_cotes(f, A, B, count_step(i), FIFTEEN_POINTS, FIFTEEN_POINTS_COEF) - EXACT_VALUE)))

import math
import random

START = -4
END = 4

def find_equally_spaced(start, end, n):
    return [start + (end - start) * i / (n - 1) for i in range(n)]

def find_chebyshev_nodes(start, end, n):
    return [(start + end) / 2 + ((end - start) / 2) * math.cos((math.pi * (2 * i + 1)) / (2 * (n - 1) + 2)) \
        for i in range(0, n)]

def generate_random_points(f, start, end, n):
    x = sorted([random.uniform(start, end) for i in range(n)])
    y = [f(i) for i in x]
    
    return (x, y)
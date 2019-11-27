import math

def f(x):
    return ((x ** 9  + math.pi) * math.cos(math.log(x ** 2 + 1))) / math.exp(x ** 2) - x / 2019

def derivative_f(x):
    return x * math.exp(-x ** 2) * (math.cos(math.log(x ** 2 + 1)) * (9 * x ** 7 - 2 * (x ** 9 + math.pi)) - 2 * (x ** 9 + math.pi) * math.sin(math.log(x ** 2 + 1)) * (x ** 2 + 1) ** -1) - 1 / 2019

def g(x, y):
    return ((x ** 9 + math.pi) * math.cos(math.log(y ** 4 + 1))) / ((y ** 2 + math.exp(1)) * math.exp(x ** 2))



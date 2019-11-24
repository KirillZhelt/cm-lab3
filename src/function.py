import matplotlib.pyplot as plt
import math

def f(x):
    return ((x ** 9  + math.pi) * math.cos(math.log(x ** 2 + 1))) / math.exp(x ** 2) - x / 2019

def derivative_f(x):
    return x * math.exp(-x ** 2) * (math.cos(math.log(x ** 2 + 1)) * (9 * x ** 7 - 2 * (x ** 9 + math.pi)) - 2 * (x ** 9 + math.pi) * math.sin(math.log(x ** 2 + 1)) * (x ** 2 + 1) ** -1) - 1 / 2019

def draw_function(f, a, b, step):

    x = list()
    y = list()

    i = a
    while i <= b:
        x.append(i)
        y.append(f(i))

        i += step

    x_ticks = list()
    i = a
    while i <= b:
        x_ticks.append(i)

        i += 1

    plt.plot(x, y)
    plt.grid(True)
    plt.xticks(x_ticks)

    plt.show()

def draw_functions(a, b, step, *functions):
    
    x_ticks = list()
    i = a
    while i <= b:
        x_ticks.append(i)

        i += 1

    plt.grid(True)
    plt.xticks(x_ticks)

    for function, function_name in functions:
        x = list()
        y = list()

        i = a
        while i <= b:
            x.append(i)
            y.append(function(i))

            i += step

        plt.plot(x, y, label=function_name)

    plt.legend()

    plt.show()

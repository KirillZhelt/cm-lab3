import math

from function import *

SECTIONS = ((-3.5, -1.6), (-1.4, -0.84), (1.5, 2.27))

BISECTION_SECTION_LENGTH = 1e-4
DISCRETE_NEWTON_H = 1e-5
DISCRETE_NEWTON_EPS = 1e-13
NEWTON_EPS = 1e-15


def sign(x):
    return (x >= 0) - (x < 0)

def bisection(sections, f, section_length):
    result_sections = [list(section) for section in sections]
    section_counts = [0] * len(result_sections)

    for i, section in enumerate(result_sections):
        while section[1] - section[0] > section_length:
            mid = (section[1] + section[0]) / 2
            if sign(f(mid)) != sign(f(section[0])):
                section[1] = mid
            else:
                section[0] = mid

            section_counts[i] += 1

    return (result_sections, section_counts)

def discrete_newton(sections, f, h, eps):
    roots = list()
    root_counts = [0] * len(sections)

    for i, section in enumerate(sections):
        prev_x = section[1]

        while True:
            root_counts[i] += 1

            x = prev_x - (h * f(prev_x)) / (f(prev_x + h) - f(prev_x))

            if math.fabs(x - prev_x) < eps:
                break

            prev_x = x

        roots.append(x)

    return (roots, root_counts)

def newton_improve_roots(prev_roots, f ,derivative_f, eps):
    # метод ньютона, улучщающий найденные корни
    roots = list()
    root_counts = [0] * len(prev_roots)

    for i, prev_root in enumerate(prev_roots):
        while True:
            root_counts[i] += 1

            x = prev_root - f(prev_root) / derivative_f(prev_root)

            if math.fabs(x - prev_root) < eps:
                break

            prev_root = x

        roots.append(x)

    return (roots, root_counts)

def newton(sections, f, derivative_f, eps):
    # метод ньютона, находящий корни из отрезков, сжатых бисекцией
    roots = list()
    root_counts = [0] * len(sections)

    for i, section in enumerate(sections):
        prev_x = section[1]

        while True:
            root_counts[i] += 1

            x = prev_x - f(prev_x) / derivative_f(prev_x)

            if math.fabs(x - prev_x) < eps:
                break

            prev_x = x

        roots.append(x)

    return (roots, root_counts)

if __name__ == "__main__":
    result_sections, section_counts = bisection(SECTIONS, f, BISECTION_SECTION_LENGTH)

    discrete_newton_roots, discrete_newton_root_counts = discrete_newton(result_sections, f, \
        DISCRETE_NEWTON_H, DISCRETE_NEWTON_EPS)

    newton_roots, newton_root_counts = newton(result_sections, f, derivative_f, NEWTON_EPS)
    newton_improve_roots, newton_improve_root_counts = newton_improve_roots(discrete_newton_roots, f, \
        derivative_f, NEWTON_EPS)

    with open("report.txt", "a") as report_file:
        report_file.write("\n")
        report_file.write("BISECTION (TASK 3):\n")
        report_file.write("Segments of separation: ")
        report_file.write(str(result_sections))
        report_file.write("\n")
        report_file.write("Number of steps for each segment: ")
        report_file.write(str(section_counts))
        report_file.write("\n")
        report_file.write("BISECTION_SECTION_LENGTH = " + str(BISECTION_SECTION_LENGTH))
        report_file.write("\n")
        report_file.write("\n")
        
        report_file.write("\n")
        report_file.write("DISCRETE NEWTON (TASK 4):\n")
        report_file.write("Roots: ")
        report_file.write(str(discrete_newton_roots))
        report_file.write("\n")
        report_file.write("Number of steps for each root: ")
        report_file.write(str(discrete_newton_root_counts))
        report_file.write("\n")
        report_file.write("EPS = " + str(DISCRETE_NEWTON_EPS) + ", H = " + str(DISCRETE_NEWTON_H))
        report_file.write("\n")
        report_file.write("\n")

        report_file.write("\n")
        report_file.write("IMPROVE ROOTS USING NEWTON (TASK 5):\n")
        report_file.write("Roots: ")
        report_file.write(str(newton_improve_roots))
        report_file.write("\n")
        report_file.write("Number of steps for each root: ")
        report_file.write(str(newton_improve_root_counts))
        report_file.write("\n")
        report_file.write("EPS = " + str(NEWTON_EPS))
        report_file.write("\n")
        report_file.write("\n")

        report_file.write("\n")
        report_file.write("NEWTON TO SEGMENTS OF SEPARATION (TASK 5):\n")
        report_file.write("Roots: ")
        report_file.write(str(newton_roots))
        report_file.write("\n")
        report_file.write("Number of steps for each root: ")
        report_file.write(str(newton_root_counts))
        report_file.write("\n")
        report_file.write("EPS = " + str(NEWTON_EPS))
        report_file.write("\n")




import datetime
import time

from scipy import linalg

from function import *
from utils import *

from solve_equation import *
from lagrange_interpolation import *
from splines_interpolation import *
from bezier_curve import *
from least_squares import *
from two_variables_interpolation import *
from equally_spaced_integration import *
from gauss_integration import *

if __name__ == "__main__":
    b = [1, 1]

    a = [[1, 2], [3, 4]]

    linalg.solve(a, b)

    draw_function(f, -26, 20, 0.01)

    result_sections, section_counts = bisection(SECTIONS, f, BISECTION_SECTION_LENGTH)

    discrete_newton_roots, discrete_newton_root_counts = discrete_newton(result_sections, f, \
        DISCRETE_NEWTON_H, DISCRETE_NEWTON_EPS)

    newton_roots, newton_root_counts = newton(result_sections, f, derivative_f, NEWTON_EPS)
    newton_improve_roots, newton_improve_root_counts = newton_improve_roots(discrete_newton_roots, f, \
        derivative_f, NEWTON_EPS)

    with open("report.txt", "w") as report_file:
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

        report_file.write("\n")
        report_file.write("LAGRANGE INTERPOLATION ON EQUALLY SPACED NODES (TASK 6):\n")

        for i in 6, 12, 18:
            report_file.write("Number of nodes: " + str(i) + "\n")

            start_time = time.perf_counter()

            equally_spaced_nodes = find_equally_spaced(START, END, i)
            lagrange_polynom_from_equally_spaced_nodes = lagrange_interpolation(f, \
                equally_spaced_nodes)
                
            end_time = time.perf_counter()

            delta = end_time - start_time

            report_file.write("Elapsed time: " + str(delta) + "\n")

            draw_functions(START, END, 0.01, (lagrange_polynom_from_equally_spaced_nodes, \
                "Lagrange polynom (equally spaced nodes) " + str(i)), \
                (f, "Function to interpolate"))

        report_file.write("\n")
        report_file.write("LAGRANGE INTERPOLATION ON CHEBYSHEV NODES (TASK 7):\n")

        for i in 6, 12, 18:
            report_file.write("Number of nodes: " + str(i) + "\n")

            start_time = time.perf_counter()

            chebyshev_nodes = find_chebyshev_nodes(START, END, i)
            lagrange_polynom_from_chebyshev_nodes = lagrange_interpolation(f, \
                chebyshev_nodes)

            end_time = time.perf_counter()

            delta = end_time - start_time

            report_file.write("Elapsed time: " + str(delta) + "\n")

            draw_functions(START, END, 0.01, (lagrange_polynom_from_chebyshev_nodes, \
                "Lagrange polynom (chebyshev nodes) " + str(i)), \
                (f, "Function to interpolate"))

        report_file.write("\n")
        report_file.write("SPLINES INTERPOLATION (TASK 8):\n")

        spline_interpolation(f, find_equally_spaced(START, END, 8))

        for i in 6, 12, 18:
            report_file.write("Number of nodes: " + str(i) + "\n")

            start_time = time.perf_counter()

            equally_spaced_nodes = find_equally_spaced(START, END, i)
            splines = spline_interpolation(f, equally_spaced_nodes)

            end_time = time.perf_counter()

            delta = end_time - start_time
            report_file.write("Elapsed time: " + str(delta) + "\n")

            draw_functions(START, END, 0.01, (splines, "Splines " + str(i)), (f, "Function to interpolate"))

        report_file.write("\n")
        report_file.write("BEZIER CURVE (TASK 9):\n")

        random_points = generate_random_points(f, START, END, NUMBER_OF_POINTS)

        start_time = time.perf_counter()
        bezier_curve_points = find_bezier_curve(random_points, NUMBER_OF_T)
        end_time = time.perf_counter()

        delta = end_time - start_time
        report_file.write("Elapsed time: " + str(delta) + "\n")

        draw_bezier_curve_with_function(random_points, bezier_curve_points, f, START, END, 0.01)

        report_file.write("\n")
        report_file.write("LEAST SQUARES (TASK 10):\n")

        random_points = generate_random_points(f, START, END, 100)
        for i in 1, 2, 3, 4, 6:
            start_time = time.perf_counter()
            least_squares_approximation = least_squares(random_points, i)
            end_time = time.perf_counter()

            delta = end_time - start_time
            report_file.write("Elapsed time: " + str(delta) + "\n")

            draw_functions(START, END, 0.01, (least_squares_approximation, "Least squares " + str(i)), \
                (f, "Original function"), points=random_points)

        report_file.write("\n")
        report_file.write("TWO VARIABLES FUNCTION LAGRANGE INTERPOLATION (TASK 11):\n")

        grid_to_draw = generate_grid(30, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)
        for i in 6, 12, 18:
            grid = generate_grid(i, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)

            start_time = time.perf_counter() 
            interpolation = interpolate_two_variables_function(g, grid)
            end_time = time.perf_counter()

            delta = end_time - start_time
            report_file.write("Elapsed time: " + str(delta) + "\n")

            draw_two_variables_fuctions(grid_to_draw, (interpolation, "Lagrange " + str(i)), \
                (g, "Original function"))

        report_file.write("\n")
        report_file.write("TWO VARIABLES FUNCTION SPLINES INTERPOLATION (TASK 12):\n")

        grid_to_draw = generate_grid(30, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)
        for i in 6, 12, 18:
            grid = generate_grid(i, START, END, SECOND_VARIABLE_START, SECOND_VARIABLE_END)

            start_time = time.perf_counter() 
            interpolation = splines_two_variables_function_interpolation(g, grid)
            end_time = time.perf_counter()

            delta = end_time - start_time
            report_file.write("Elapsed time: " + str(delta) + "\n")

            draw_two_variables_fuctions(grid_to_draw, (interpolation, "Splines " + str(i)), \
                (g, "Original function"))

        report_file.write("\n")
        report_file.write("EQUALLY SPACED INTEGRATION (TASK 13):\n")

        def profile_integration(name, integration_function, report_file, *args):
            start_time = time.perf_counter()
            result = abs(integration_function(*args) - EXACT_VALUE)
            end_time = time.perf_counter()

            delta = end_time - start_time
            report_file.write("{0} ({1}); elapsed time={2}; result difference={3}\n"\
                .format(name, i, delta, result))

        for i in range(0, 11):
            profile_integration("Left rectangles", left_rectangles, report_file, f, A, B, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Right rectangles", right_rectangles, report_file, f, A, B, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Middle rectangles", middle_rectangles, report_file, f, A, B, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Trapezoid", trapezoid, report_file, f, A, B, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Simpson", composite_simpson, report_file, f, A, B, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Newton-Cotes5", newton_cotes, report_file, f, A, B, count_step(i), FIVE_POINTS, FIVE_POINTS_COEF)

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Newton-Cotes7", newton_cotes, report_file, f, A, B, count_step(i), SEVEN_POINTS, SEVEN_POINTS_COEF)

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Newton-Cotes9", newton_cotes, report_file, f, A, B, count_step(i), NINE_POINTS, NINE_POINTS_COEF)

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Newton-Cotes11", newton_cotes, report_file, f, A, B, count_step(i), ELEVEN_POINTS, ELEVEN_POINTS_COEF)

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Newton-Cotes13", newton_cotes, report_file, f, A, B, count_step(i), THIRTEEN_POINTS, THIRTEEN_POINTS_COEF)

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Newton-Cotes15", newton_cotes, report_file, f, A, B, count_step(i), FIFTEEN_POINTS, FIFTEEN_POINTS_COEF)
           
        report_file.write("\n")
        report_file.write("GAUSS INTEGRATION (TASK 15):\n")

        for i in range(0, 11):
            profile_integration("Gauss2", composite_gauss, report_file, f, A, B, TWO_NODES, TWO_WEIGHTS, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Gauss3", composite_gauss, report_file, f, A, B, THREE_NODES, THREE_WEIGHTS, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Gauss4", composite_gauss, report_file, f, A, B, FOUR_NODES, FOUR_WEIGHTS, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Gauss5", composite_gauss, report_file, f, A, B, FIVE_NODES, FIVE_WEIGHTS, count_step(i))

        report_file.write("\n")
        for i in range(0, 11):
            profile_integration("Gauss6", composite_gauss, report_file, f, A, B, SIX_NODES, SIX_WEIGHTS, count_step(i))
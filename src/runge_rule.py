from math import ceil

from function import *

from equally_spaced_integration import newton_cotes, A, B, EXACT_VALUE, FIFTEEN_POINTS, FIFTEEN_POINTS_COEF
from gauss_integration import composite_gauss, SEVEN_NODES, SEVEN_WEIGHTS

COTES_15_P = 16
GAUSS_7_P = 14

def runge_rule_newton_cotes(p, accuracy):
    N1 = 1
    N2 = 2

    h1 = (B - A) / N1

    q1 = newton_cotes(f, A, B, h1, FIFTEEN_POINTS, FIFTEEN_POINTS_COEF)

    count = 0

    while True:
        count += 1

        h2 = (B - A) / N2
        q2 = newton_cotes(f, A, B, h2, FIFTEEN_POINTS, FIFTEEN_POINTS_COEF)

        R = ((q2 - q1) * h2 ** p) / (h1 ** p - h2 ** p) 

        if abs(R) <= accuracy:
            return q2, count

        N = int(ceil((abs(R) / accuracy) ** (1 / p) * N2))

        N1 = N2
        h1 = h2
        q1 = q2

        N2 = N

def runge_rule_gauss(p, accuracy):
    N1 = 1
    N2 = 2

    h1 = (B - A) / N1

    q1 = composite_gauss(f, A, B, SEVEN_NODES, SEVEN_WEIGHTS, h1)

    count = 0

    while True:
        count += 1

        h2 = (B - A) / N2
        q2 = composite_gauss(f, A, B, SEVEN_NODES, SEVEN_WEIGHTS, h2)

        R = ((q2 - q1) * h2 ** p) / (h1 ** p - h2 ** p) 

        if abs(R) <= accuracy:
            return q2, count

        N = int(ceil((abs(R) / accuracy) ** (1 / p) * N2))

        N1 = N2
        h1 = h2
        q1 = q2

        N2 = N

if __name__ == "__main__":

    with open('report.txt', 'a') as report_file:
        report_file.write("\n")
        report_file.write("Runge rule (TASK 15):\n")

        _, count = runge_rule_newton_cotes(COTES_15_P, 10e-15)
        report_file.write("Newton-Cotes15: {0} steps\n".format(count))

        _, count = runge_rule_gauss(GAUSS_7_P, 10e-15)
        report_file.write("Gauss7: {0} steps\n".format(count))

import math
import random

def horner(polynomial, value):
    result = polynomial[0]
    for i in range(1, len(polynomial)):
        result = result * value + polynomial[i]
    return result

def sign(x):
    if x <= 0:
        return -1
    else:
        return 1

def muller_method(coefficients, epsilon=1e-8, kmax=1000, nr=100):
    A = max([abs(i) for i in coefficients])
    R = (abs(coefficients[0]) + A) / abs(coefficients[0])
    roots = set()

    for _ in range(nr):
        x0 = random.uniform(-R, R)
        x1 = random.uniform(-R, R)
        x2 = random.uniform(-R, R)

        for k in range(kmax):
            h0 = x1 - x0
            h1 = x2 - x1
            delta0 = (horner(coefficients, x1) - horner(coefficients, x0)) / h0
            delta1 = (horner(coefficients, x2) - horner(coefficients, x1)) / h1
            a = (delta1 - delta0) / (h1 + h0)
            b = a * h1 + delta1
            c = horner(coefficients, x2)

            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                break

            if abs(b + sign(b) * math.sqrt(discriminant)) < epsilon:
                break

            delta_x = 2 * c / (b + sign(b) * math.sqrt(discriminant))
            x3 = x2 - delta_x

            if abs(delta_x) < epsilon or k >= kmax or abs(delta_x) > 1e8:
                if abs(delta_x) < epsilon:
                    roots.add(x2)
                break

            x0, x1, x2 = x1, x2, x3

    return roots

def save_roots_to_file(roots, filename):
    with open(filename, 'w') as file:
        for root in roots:
            file.write(str(root) + '\n')


coefficients_p1 = [1.0, -6.0, 11.0, -6.0]
coefficients_p2 = [42.0, -55.0, -42.0, 49.0, -6.0]
coefficients_p3 = [8.0, -38.0, 49.0, -22.0, 3.0]
coefficients_p4 = [1.0, -6.0, 13.0, -12.0, 4.0]

roots = muller_method(coefficients_p1)
if roots is not None:
    save_roots_to_file(roots, 'roots.txt')

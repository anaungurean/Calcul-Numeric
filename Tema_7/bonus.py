import random

def f(x):
    return x**3 - 6*x**2 + 11*x - 6
    # return 42*x**4 - 55*x**3 - 42*x**2 + 49*x - 6
    # return 8*x**4 - 38*x**3 + 49*x**2 - 22*x + 3
    # return x**4 - 6*x**3 + 13*x**2 - 12*x + 4

def f_prime(x):
    return 3*x**2 - 12*x + 11
    # return 168*x**3 - 165*x**2 - 84*x + 49
    # return 32*x**3 - 114*x**2 + 98*x - 22
    # return 4*x**3 - 18*x**2 + 26*x - 12

coefficients_p1 = [1.0, -6.0, 11.0, -6.0]
coefficients_p2 = [42.0, -55.0, -42.0, 49.0, -6.0]
coefficients_p3 = [8.0, -38.0, 49.0, -22.0, 3.0]
coefficients_p4 = [1.0, -6.0, 13.0, -12.0, 4.0]

def newton_fourth_order(coefficients, f, f_prime, epsilon=1e-8, kmax=1000):
    roots = set()

    for _ in range(100):
        A = max([abs(i) for i in coefficients])
        R = (abs(coefficients[0]) + A) / abs(coefficients[0])
        x0 = random.uniform(-R, R)
        x = x0
        for _ in range(kmax):
            if f_prime(x) == 0:
                break

            y = x - (f(x) / f_prime(x))
            z = x - ((f(x)**2 + f(y)**2) / f_prime(x) * (f(x) - f(y)))

            if abs(y - z) < epsilon:
                roots.add(y)
                break

            x = y

    return roots

def save_roots_to_file(roots, filename):
    with open(filename, 'w') as file:
        for root in roots:
            file.write(str(root) + '\n')


roots = newton_fourth_order(coefficients_p1, f, f_prime)
if roots:
    save_roots_to_file(roots, 'roots_bonus.txt')

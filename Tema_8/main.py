import numpy as np
from prettytable import PrettyTable


def calculate_gradient_analytical(F, x, y):
    # Calcularea gradientului functiei F in punctul (x, y) folosind formula analitica
    if F == F1:
        partial_x = 2 * x - 2
        partial_y = 2 * y - 4
    elif F == F2:
        partial_x = 6 * x - 12
        partial_y = 4 * y + 16
    elif F == F3:
        partial_x = 2 * x - 4 * y
        partial_y = -4 * x + 10 * y - 4
    elif F == F4:
        partial_x = 2 * x * y - 2 * y ** 2 + 3 * y
        partial_y = x ** 2 - 4 * x * y + 10 * y - 4
    else:
        raise ValueError("Functia data nu este recunoscuta.")

    return np.array([partial_x, partial_y])


def calculate_gradient_approximate(F, x, y, h=1e-5):
    # Calcularea gradientului functiei F in punctul (x, y) folosind o aproximare numerica
    partial_x = (3 * F(x, y) - 4 * F(x - h, y) + F(x - 2 * h, y)) / (2 * h)
    partial_y = (3 * F(x, y) - 4 * F(x, y - h) + F(x, y - 2 * h)) / (2 * h)
    return np.array([partial_x, partial_y])


def constant_learning_rate(eta):
    # Metoda de alegere a ratei de invatare constante
    return eta


def backtracking_line_search(F, x, y, grad, beta=0.8):
    # Metoda de ajustare a ratei de invatare cu backtracking line search
    eta = 1.0
    p = 1
    while F(x - eta * grad[0], y - eta * grad[1]) > F(x, y) - (eta / 2) * np.linalg.norm(grad) ** 2 and p < 8:
        eta *= beta
        p += 1
    return eta


def gradient_descent(F, initial_x, initial_y, gradient_method='analytical', eta_method='constant', eta = 0.001,
                     epsilon=1e-5, k_max=30000):
    x, y = initial_x, initial_y
    k = 0
    while True:
        if gradient_method == 'analytical':
            grad = calculate_gradient_analytical(F, x, y)
        elif gradient_method == 'approximate':
            grad = calculate_gradient_approximate(F, x, y)
        else:
            raise ValueError("Metoda de calcul a gradientului nu este recunoscuta.")

        if eta_method == 'constant':
            learning_rate = constant_learning_rate(eta)
        elif eta_method == 'backtracking':
            learning_rate = backtracking_line_search(F, x, y, grad)
        else:
            raise ValueError("Metoda de alegere a ratei de invatare nu este recunoscuta.")

        x -= learning_rate * grad[0]
        y -= learning_rate * grad[1]
        k += 1
        if np.linalg.norm(learning_rate * grad) < epsilon or k >= k_max or np.linalg.norm(learning_rate * grad) > 1e10:
            break
    return (x, y), k


# Functia F1: F(x, y) = x^2 + y^2 - 2x - 4y - 1
def F1(x, y):
    return x ** 2 + y ** 2 - 2 * x - 4 * y - 1


# Functia F2: F(x, y) = 3x^2 - 12x + 2y^2 + 16y - 10
def F2(x, y):
    return 3 * x ** 2 - 12 * x + 2 * y ** 2 + 16 * y - 10


# Functia F3: F(x, y) = x^2 - 4xy + 5y^2 - 4y + 3
def F3(x, y):
    return x ** 2 - 4 * x * y + 5 * y ** 2 - 4 * y + 3


# Functia F4: F(x, y) = x^2y - 2xy^2 + 3xy + 4
def F4(x, y):
    return x**2 * y - 2*x*y**2 + 3*x*y + 4


def main():
    # Rularea algoritmului cu valorile initiale alese pentru fiecare functie
    eta_methods = ['constant', 'backtracking']
    eta = 0.01
    gradient_methods = ['analytical', 'approximate']
    epsilon = 1e-5


    # Initializare tabel
    table = PrettyTable()
    table.field_names = ["Functie", "Metoda gradient", "Metoda eta", "Eta", "Solutie (x)", "Solutie (y)", "Nr. iteratii",
                         "Convergenta"]


    # Calcul si adaugare rezultate in tabel
    for F in [F1, F2, F3, F4]:
        for gradient_method in gradient_methods:
            for eta_method in eta_methods:
                    sol, num_iterations = gradient_descent(F, -2, 1, gradient_method=gradient_method, eta_method=eta_method, eta = eta, epsilon=epsilon)
                    if num_iterations < 30000:
                        convergence = "Da"
                    else:
                        convergence = "Nu"
                    table.add_row(
                        [F.__name__, gradient_method, eta_method, eta, sol[0], sol[1], num_iterations, convergence])


    print(table)

if __name__ == "__main__":
    main()


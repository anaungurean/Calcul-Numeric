import numpy as np

def descompunere_LU(epsilon, n, A):
    for p in range(n):
        for i in range(p, n):
            A[i][p] = (A[i][p] - sum(A[i][k] * A[k][p] for k in range(p)))

        for i in range(p+1, n):
            if np.abs(A[i][i]) < epsilon:
                raise ValueError("Error: Nu se poate efectua descompunerea LU")
            A[p][i] = (A[p][i] - sum(A[p][k] * A[k][i] for k in range(p))) / A[p][p]


def determinant_A(n, A):
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det

def substitutie_directa(A, b):
    n = len(b)
    x = np.zeros(n)

    for i in range(n):
        sum_val = 0
        for j in range(i):
            sum_val += A[i][j] * x[j]
        x[i] = (b[i] - sum_val) / A[i][i]

    return x

def substitutie_inversa(A, b):
    n = len(b)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_val = 0
        for j in range(i + 1, n):
            sum_val += A[i][j] * x[j]
        x[i] = (b[i] - sum_val)

    return x

def calcul_norma(A_init, x_LU, b_init):
    n = len(b_init)
    norma = 0.0

    for i in range(n):
        suma = sum(A_init[i][j] * x_LU[j] for j in range(n))
        norma += (suma - b_init[i]) ** 2

    norma = norma ** 0.5
    return norma

def utilizare_biblioteca(A_init, b_init):
    x_LU = np.linalg.solve(A_init, b_init)
    A_lib = np.linalg.inv(A_init)
    x_lib = np.dot(A_lib, b_init)
    norma1 = np.linalg.norm(x_LU - x_lib, ord=2)
    norma2 = np.linalg.norm(x_LU - np.dot(A_lib, b_init), ord=2)

    print("Solutia sistemului Ax = b:")
    print("x_LU:", x_LU)
    print("x_lib:", x_lib)
    print()

    print("Inversa matricei A:")
    print("A_lib:")
    print(A_lib)
    print()

    print("Normele:")
    print("||x_LU - x_lib||2:", norma1)
    print("||x_LU - A_inv_lib b||2:", norma2)



if __name__ == '__main__':
    n = int(input("Introduceti dimensiunea n a datelor: "))
    t = float(input("Introduceti valoarea t (5,...,10) pentru calculul variabilei epsilon: "))
    while t < 5 or t > 10:
        print("Valoarea t trebuie sa fie intre 5 si 10...")
        t = float(input("Introduceti alta valoare pentru t: "))

    epsilon = 10 ** (-t)

    A_init = np.zeros((n, n))
    b_init = np.zeros(n)

    if n < 10:
        for i in range(n):
            for j in range(n):
                A_init[i][j] = float(input(f"Introduceti valoarea elementului A[{i}][{j}]: "))
        for i in range(n):
            b_init[i] = float(input(f"Introduceti valoarea elementului b[{i}]: "))
    else:
        for i in range(n):
            for j in range(n):
                A_init[i][j] = np.random.uniform(-100, 100)
        b_init = np.random.uniform(-100, 100, n)

    A = A_init.copy()
    try:
        descompunere_LU(epsilon, n, A)
        print("Matricea A:")
        print(A)
        print()

        print("Matricea L:")
        for i in range(n):
            print("[", end=" ")
            for j in range(n):
                if i < j:
                    print(0, end=" ")
                else:
                    print(A[i][j], end=" ")
            print("]")
        print()

        print("Matricea U:")
        for i in range(n):
            print("[", end=" ")
            for j in range(n):
                if i == j:
                    print(1, end=" ")
                elif i < j:
                    print(A[i][j], end=" ")
                else:
                    print(0, end=" ")
            print("]")
        print()

        det = determinant_A(n, A)
        print(f"Determinantul matricei A este: {det}")

        y = substitutie_directa(A, b_init)
        x_LU = substitutie_inversa(A, y)

        print("Solutia aproximativa x_LU:")
        print(x_LU)

        norma = calcul_norma(A_init, x_LU, b_init)
        toleranta = 10 ** (-9)
        print(f"Norma: {norma}")
        if norma < toleranta:
            print("Soluția este în limita toleranței.")
        else:
            print("Soluția NU este în limita toleranței.")

        utilizare_biblioteca(A_init, b_init)

    except ValueError as e:
        print(e)



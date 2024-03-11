import numpy as np

def descompunere_LU(epsilon, n, A):
    L = np.zeros(n * (n + 1) // 2)
    U = np.zeros(n * (n + 1) // 2)

    for i in range(n):
        for j in range(i+1):
            s = 0.0
            for k in range(j):
                s += L[i * (i + 1) // 2 + k] * U[j * (j + 1) // 2 + k]
            L[i * (i + 1) // 2 + j] = A[i][j] - s

        for j in range(i, n):
            s = 0.0
            for k in range(i):
                s += L[i * (i + 1) // 2 + k] * U[j * (j + 1) // 2 + k]
            if np.abs(L[i * (i + 1) // 2 + i]) < epsilon:
                raise ValueError("Error: Nu se poate efectua descompunerea LU")
            U[j * (j + 1) // 2 + i] = (A[i][j] - s) / L[i * (i + 1) // 2 + i]

    return L, U

def substitutie_directa(L, n, b):
    y = np.zeros(n)
    for i in range(n):
        s = 0.0
        for j in range(i):
            s += L[i * (i + 1) // 2 + j] * y[j]
        y[i] = (b[i] - s) / L[i * (i + 1) // 2 + i]
    return y

def substitutie_inversa(U, n, y):
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        s = 0.0
        for j in range(i + 1, n):
            s += U[i * (i + 1) // 2 + j] * x[j]
        x[i] = (y[i] - s)
    return x

if __name__ == '__main__':
    n = int(input("Introduceti dimensiunea n a datelor: "))
    t = float(input("Introduceti valoarea t (5,...,10) pentru calculul variabilei epsilon: "))
    while t < 5 or t > 10:
        print("Valoarea t trebuie sa fie intre 5 si 10...")
        t = float(input("Introduceti alta valoare pentru t: "))

    epsilon = 10 ** (-t)

    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(n):
        for j in range(n):
            A[i][j] = float(input(f"Introduceti valoarea elementului A[{i}][{j}]: "))

    for i in range(n):
        b[i] = float(input(f"Introduceti valoarea elementului b[{i}]: "))

    try:
        L, U = descompunere_LU(epsilon, n, A)
        print("L:", L)
        print("U:", U)

        y = substitutie_directa(L, n, b)
        x = substitutie_inversa(U, n, y)

        print("Solutia sistemului Ax = b:")
        print("x =", x)

    except ValueError as e:
        print(e)
import numpy as np

def descompunere_LU(epsilon, n, A):
    for i in range(n):
        for j in range(i):
            if np.abs(A[j][j]) < epsilon:
                raise ValueError("Error: Nu se poate efectua descompunerea LU")
            A[i][j] = (A[i][j] - sum(A[i][k] * A[k][j] for k in range(j))) / A[j][j]

        for j in range(i, n):
            A[i][j] = (A[i][j] - sum(A[i][k] * A[k][j] for k in range(i)))

    return A


def determinant_A(n, A):
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det


if __name__ == '__main__':
    n = int(input("Introduceti dimensiunea n a datelor: "))
    t = float(input("Introduceti valoarea t (5,...,10) pentru calculul variabilei epsilon: "))
    while t < 5 or t > 10:
        print("Valoarea t trebuie sa fie intre 5 si 10...")
        t = float(input("Introduceti alta valoare pentru t: "))

    epsilon = 10 ** (-t)

    # Atest = np.array([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]])
    # btest = np.array([4, 10, 0])
    # try:
    #     L, U = descompunere_LU(epsilon, 3, Atest)
    #     print(L)
    #     print(U)
    #     print(np.dot(L, U))
    # except ValueError as e:
    #     print(e)

    A_init = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A_init[i][j] = float(input(f"Introduceti valoarea elementului A[{i}][{j}]: "))

    A = A_init.copy()

    b = np.zeros(n)
    for i in range(n):
        b[i] = float(input(f"Introduceti valoarea elementului b[{i}]: "))

    try:
        res = descompunere_LU(epsilon, n, A)
        print("Matricea A:")
        print(res)
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
    except ValueError as e:
        print(e)



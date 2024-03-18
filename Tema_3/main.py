import copy
import streamlit as st
import numpy as np

def determine_vector_b(A, s):
    n = len(A)
    b = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            b[i] += s[j] * A[i][j]
    return b

def qr_decomposition(A,b, epsilon=1e-10):
    n = len(A)
    Q = np.eye(n)
    for r in range(n - 1): # constructie matricea Pr, constanta beta, vectorul u
        sigma = sum(A[i][r] ** 2 for i in range(r, n))
        if sigma <= epsilon:
            break # matricea A singulara
        k = np.sqrt(sigma)
        if A[r][r] < 0:
            k = -k
        beta = sigma - k * A[r][r]
        u = [0] * n
        u[r] = A[r][r] - k
        for i in range(r + 1, n):
            u[i] = A[i][r]
        # A = Pr * A
        for j in range(r, n):
            tau = sum(A[i][j] * u[i] for i in range(r, n)) / beta
            for i in range(r, n):
                A[i][j] -= tau * u[i]

        # b = Pr * b
        tau = sum(b[i] * u[i] for i in range(r, n)) / beta
        for i in range(r, n):
            b[i] -= tau * u[i]

        # Q = Q * Pr
        for j in range(n):
            tau = sum(Q[i][j] * u[i] for i in range(r, n)) / beta
            for i in range(r, n):
                Q[i][j] -= tau * u[i]

    R = np.array(A)
    Q = Q.T
    return Q, R, b

def solve_linear_system_with_library(A_init, b_init):
    Q, R = np.linalg.qr(A_init)
    x_QR = np.linalg.solve(R, np.dot(Q.T, b_init))
    return x_QR


def solve_linear_system(b, R):
    n = len(b)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_term = 0
        for j in range(i + 1, n):
            sum_term += R[i, j] * x[j]
        x[i] = (b[i] - sum_term) / R[i, i]

    return x


def determin_errors(A_init, x_householder, x_QR, b_init,s):
    norma1 = np.linalg.norm(np.dot(A_init, x_householder) - b_init, ord=2)
    norma2 = np.linalg.norm(np.dot(A_init,x_QR) - b_init, ord=2)
    norma3 = np.linalg.norm(x_householder - s, ord=2) / np.linalg.norm(s, ord=2)
    norma4 = np.linalg.norm(x_QR - s, ord=2) / np.linalg.norm(s, ord=2)
    if norma1 < 10 ** (-6):
        print("Norma1:", norma1, " < 10^(-6)")
    if norma2 < 10 ** (-6):
        print("Norma2:", norma2, " < 10^(-6)")
    if norma3 < 10 ** (-6):
        print("Norma3  :", norma3, " < 10^(-6)")
    if norma4 < 10 ** (-6):
        print("Norma4:", norma4, " < 10^(-6)")

def solve_upper_triangular(R, b):
    n = len(b)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        sum_term = 0
        for j in range(i + 1, n):
            sum_term += R[i, j] * x[j]
        x[i] = (b[i] - sum_term) / R[i, i]

    return x

def determine_inv_A(A_init,Q,R):
    n = len(A_init)
    inv_A = np.zeros((n, n))

    for j in range(n):
        ej = np.zeros(n)
        ej[j] = 1.0
        b = np.dot(Q.T, ej)  # sau ej * Q.T pentru a lua linia j

        x_star = solve_upper_triangular(R, b)
        # print("Coloana", j, "din inversa matricei A:")
        # print(x_star)
        inv_A[:, j] = x_star

    return inv_A

def determine_inv_A_with_library(A_init):
    return np.linalg.inv(A_init)

def check_if_singular(A):
    det_A = np.linalg.det(A)
    if det_A == 0:
        return True  # Matricea este singulară
    else:
        return False  # Matricea nu este singulară


if __name__ == '__main__':

    if (input("Do you want to use the default values? (y/n): ") == "y"):
        A = [[0, 0, 4], [1, 2, 3], [0, 1, 2]]
        s = [3, 2, 1]
        epsilon = 0.1
    else:
        n = int(input("Introduceti dimensiunea n a datelor: "))
        A = np.zeros((n, n))
        s = np.zeros(n)
        for i in range(n):
            for j in range(n):
                A[i][j] = np.random.uniform(0, 10)
        s[i] = np.random.uniform(0, 10)

    if check_if_singular(A):
        print("Matricea A este singulara")
        exit(1)


    A_init = copy.deepcopy(A)
    b = determine_vector_b(A, s)
    b_init = copy.deepcopy(b)

    print("Vectorul b:", b)
    print("-------------------")
    Q, R,b = qr_decomposition(A,b)
    print("Descompunerea QR:")
    print("Q =", Q)
    print("R =", R)
    print("-------------------")

    x_householder = solve_linear_system(b, R)
    print("Solutia sistemului Ax = b:")
    print("x_householder:", x_householder)
    print("-------------------")

    x_QR = solve_linear_system_with_library(A_init, b_init)
    print("Solutia sistemului Ax = b cu biblioteca numpy:")
    print("x_QR:", x_QR)
    print("-------------------")
    print("Diferenta solutiilor:")
    print("||x_householder - x_QR||2:", np.linalg.norm(x_householder - x_QR, ord=2))
    print("-------------------")
    determin_errors(A_init, x_householder, x_QR, b_init,s)

    print("-------------------")
    inv_A = determine_inv_A(A_init,Q,R)
    print("Inversa matricei A:")
    print(inv_A)
    print("-------------------")
    inv_A_library = determine_inv_A_with_library(A_init)
    print("Inversa matricei A cu biblioteca numpy:")
    print(inv_A_library)
    print("-------------------")
    print("Diferenta inverselor:")
    print("||inv_A - inv_A_library||2:", np.linalg.norm(inv_A - inv_A_library, ord=2))
    print("-------------------")

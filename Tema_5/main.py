import numpy as np
import copy
def determine_p_q(A):
    n = A.shape[0]
    p, q = 0, 0
    max = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(A[i][j]) > max:
                max = abs(A[i][j])
                p, q = i, j
    return p, q

def check_is_diagonal(A, eps):
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            if i != j and abs(A[i][j]) > eps:
                return False
    return True

def jacobi_method(A, eps, max_iter):
    k = 0
    U = np.eye(A.shape[0])
    n = A.shape[0]
    p, q = determine_p_q(A)

    while k <= max_iter and not check_is_diagonal(A, eps):
        alpha = (A[p, p] - A[q, q]) / (2 * A[p, q])
        t = -alpha + np.sign(alpha) * np.sqrt(1 + alpha ** 2)
        c = 1 / np.sqrt(1 + t ** 2)
        s = t / np.sqrt(1 + t ** 2)
        for j in range(n):
            if j != p and j != q:
                A[p][j], A[j][p] = c * A[p][j] + s * A[q][j], c * A[j][p] + s * A[j][q]
                A[q][j], A[j][q] = -s * A[j][p] + c * A[q][j], -s * A[j][p] + c * A[q][j]
        A[p][p] = A[p][p] + t * A[p][q]
        A[q][q] = A[q][q] - t * A[p][q]
        A[p][q] = A[q][p] = 0

        old_U_p = [U[i][p] for i in range(n)]
        for i in range(n):
            U[i][p] = c * U[i][p] + s * U[i][q]
        for i in range(n):
            U[i][q] = c * U[i][q] - s * old_U_p[i]

        p, q = determine_p_q(A)
        k += 1

    return A.diagonal(), U


def calculate_norm(A_init, U, valori_proprii):
    AU = np.dot(A_init, U)
    UV = np.dot(U, valori_proprii)
    difference = AU - UV
    norm = np.linalg.norm(difference)
    return norm

def cholesky_iteration(A, epsilon=1e-10, max_iterations=1000):
    L = np.linalg.cholesky(A)
    k = 0

    while k < max_iterations:
        A_next = np.dot(L.T, L)

        if np.linalg.norm(A_next - A) < epsilon:
            break
        A = A_next
        k += 1
        L = np.linalg.cholesky(A)
    return A_next

def svd_pseudoinverse(A):
    U, S, V = np.linalg.svd(A)
    S_pseudo = np.zeros((A.shape[1], A.shape[0]))
    S_pseudo[:len(S), :len(S)] = np.diag(1 / S)
    A_pseudo = np.dot(V.T, np.dot(S_pseudo, U.T))
    return A_pseudo

def pseudo_inverse_least_squares(A):
    A_J = np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)
    return A_J
def calculate_L1_norm(A_I, A_J):
    diff = A_I - A_J
    norm_L1 = np.linalg.norm(diff, ord=1)
    return norm_L1

def calculate_svd_properties(A):
    U, S, V = np.linalg.svd(A)
    print("Valorile singulare ale matricei A:")
    print(S)

    rank = np.count_nonzero(S)
    print("Rangul matricei A:", rank)

    condition_number = np.max(S) / np.min(S)
    print("Numărul de condiționare al matricei A:", condition_number)

    A_pseudo = svd_pseudoinverse(A)
    print("Pseudoinversa matricei A:")
    print(A_pseudo)

    A_J = pseudo_inverse_least_squares(A)
    norm_L1 = calculate_L1_norm(A_pseudo, A_J)
    print("Matricea pseudo-inversă în sensul celor mai mici pătrate (A^J):")
    print(A_J)
    print("Norma L1 între A^I și A^J:", norm_L1)


def main():
    A = np.array([[1, 1, 2], [1, 1, 2], [2, 2, 2]], dtype=float)
    # A = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]], dtype=float)
    # A = np.array([[1,2,3,4], [2,3,4,5], [3,4,5,6], [4,5,6,7]], dtype=float )
    # A = np.array([[1,0,1,0], [0,1,0,1], [1,0,1,0], [0,1,0,1]], dtype=float)

    A_init = copy.deepcopy(A)
    eps = 1e-15
    max_iter = 10000
    valori_proprii, U = jacobi_method(A, eps, max_iter)
    print("-------------Exercise1---------------------")
    print("Valori proprii:", valori_proprii)
    print("Matricea U:", U)
    norm = calculate_norm(A_init,  U, valori_proprii)
    print("Norm:", norm)

    print("\n\n")
    print("-------------Exercise2---------------------")
    A = np.array([[4, 12, -16],
                  [12, 37, -43],
                  [-16, -43, 98]])
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    print("Valorile proprii ale matricei A:")
    print(eigenvalues)
    result = cholesky_iteration(A)
    print("Ultima matrice calculată:")
    print(result)
    print("\n\n")

    print("-------------Exercise3---------------------")
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [14, 11, 12]])

    calculate_svd_properties(A)

if __name__ == "__main__":
    main()

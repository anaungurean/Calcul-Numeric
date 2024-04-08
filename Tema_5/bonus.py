import numpy as np
import copy

def get_element_at_pos_ij(vector_matrix, i, j):
    if i >= j:
        index = i * (i + 1) // 2 + j
    else:
        index = j * (j + 1) // 2 + i
    return vector_matrix[index]

def get_index_at_pos_ij(i, j):
    if i >= j:
        index = i * (i + 1) // 2 + j
    else:
        index = j * (j + 1) // 2 + i
    return index

def pos_to_indices(pos):
    i = 0
    while pos >= i:
        pos -= i
        i += 1
    return i - 1, pos

def get_pos_for_max(vector_matrix, size_matrix):
    maxi = abs(vector_matrix[1])
    pos_maxi_i = 1
    pos_maxi_j = 0
    for i in range(3, len(vector_matrix)):
        if abs(vector_matrix[i]) > maxi:
            pos_i, pos_j = pos_to_indices(i)
            if pos_i != pos_j:
                maxi = abs(vector_matrix[i])
                pos_maxi_i = pos_i
                pos_maxi_j = pos_j
    return pos_maxi_i, pos_maxi_j

def get_t_c_s(vector_matrix, p, q, size_matrix, eps=1e-9):
    a_pq = get_element_at_pos_ij(vector_matrix, p, q)
    if abs(a_pq) < eps:
        return None, None, None
    a_pp = get_element_at_pos_ij(vector_matrix, p, p)
    a_qq = get_element_at_pos_ij(vector_matrix, q, q)

    alpha = (a_pp - a_qq) / (2 * a_pq)
    root_part_2 = (alpha**2 + 1) ** 0.5
    root_t_1 = (- alpha) + root_part_2
    root_t_2 = (- alpha) - root_part_2

    if abs(root_t_1) > abs(root_t_2):
        t = root_t_2
    else:
        t = root_t_1

    numitor = (1 + t**2) ** 0.5
    c = 1 / numitor
    s = t / numitor
    return t, c, s

def is_not_diagonal(vector_matrix, size_matrix, eps=1e-9):
    for i in range(size_matrix):
        for j in range(i):
            if abs(get_element_at_pos_ij(vector_matrix, i, j)) > eps:
                return True
    return False

def update(vector_matrix, p, q, t, c, s, size_matrix):
    for j in range(size_matrix):
        if j != p and j != q:
            a_pj = get_element_at_pos_ij(vector_matrix, p, j)
            index_a_pj = get_index_at_pos_ij(p, j)
            a_qj = get_element_at_pos_ij(vector_matrix, q, j)
            index_a_qj = get_index_at_pos_ij(q, j)

            vector_matrix[index_a_pj] = c * a_pj + s * a_qj
            vector_matrix[index_a_qj] = - s * a_pj + c * a_qj

    a_pq = get_element_at_pos_ij(vector_matrix, p, q)
    index_a_pp = get_index_at_pos_ij(p, p)
    vector_matrix[index_a_pp] += t * a_pq
    index_a_qq = get_index_at_pos_ij(q, q)
    vector_matrix[index_a_qq] -= t * a_pq

    index_a_pq = get_index_at_pos_ij(p, q)
    vector_matrix[index_a_pq] = 0

def jacobi(matrix, eps=1e-9, max_iter=1000):
    vector_matrix = []
    size_matrix = len(matrix)
    for i in range(size_matrix):
        for j in range(i + 1):
            vector_matrix.append(matrix[i][j])

    p, q = get_pos_for_max(vector_matrix, size_matrix)
    t, c, s = get_t_c_s(vector_matrix, p, q, size_matrix, eps)
    k = 0
    while is_not_diagonal(vector_matrix, size_matrix, eps) and k <= max_iter:
        update(vector_matrix, p, q, t, c, s, size_matrix)
        p, q = get_pos_for_max(vector_matrix, size_matrix)
        t, c, s = get_t_c_s(vector_matrix, p, q, size_matrix, eps)
        k += 1

    eigenvalues = [get_element_at_pos_ij(vector_matrix, i, i) for i in range(size_matrix)]
    return eigenvalues

# Example usage
A = np.array([[1, 1, 2], [1, 1, 2], [2, 2, 2]], dtype=float)
eigenvalues = jacobi(A)
print("Eigenvalues:", eigenvalues)

import numpy as np

def read_data(file_name_a, file_name_b):
    with open(file_name_a, 'r') as file:
        dimension_a = int(file.readline().strip())
        sparse_matrix_a = {}

        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                value, row, col = map(float, parts)
                row = int(row)
                col = int(col)
                sparse_matrix_a.setdefault(row, {})[col] = sparse_matrix_a.get((row, col), 0) + value

    with open(file_name_b, 'r') as file:
        dimension_b = int(file.readline())
        vector_b = np.zeros((dimension_b))
        for i in range(dimension_b):
            value = float(file.readline())
            vector_b[i] = value

    return dimension_a, sparse_matrix_a, dimension_b, vector_b

def sparse_matrix_representation(matrix_a):
    valori = []
    ind_col = []
    inceput_linii = [0]

    for row_idx, row in matrix_a.items():
        num_elements = 0
        for col_idx, value in row.items():
            valori.append(value)
            ind_col.append(col_idx)
            num_elements += 1
        inceput_linii.append(inceput_linii[-1] + num_elements)

    return valori, ind_col, inceput_linii

def check_diagonal_not_null(A, dimension_a, epsilon=10 ** (-9)):
    for i in range(dimension_a):
        if i not in A or i not in A[i] or abs(A[i][i]) <= epsilon:
            print(f"Elementul de pe diagonala principala de pe linia {i} este nul sau foarte mic")
            return 0
    return 1

def gauss_seidel(matrix_a, vector_b, dimension_a, epsilon=10 ** (-9), kmax=10000):
    xGS = np.zeros(dimension_a)

    for k in range(kmax):
        old_xGS = xGS.copy()

        for i in range(dimension_a):
            lower_sum = 0
            for j, value in matrix_a.get(i, {}).items():
                if j < i:
                    lower_sum += value * xGS[j]

            upper_sum = 0
            for j, value in matrix_a.get(i, {}).items():
                if j > i:
                    upper_sum += value * old_xGS[j]

            xGS[i] = (vector_b[i] - lower_sum - upper_sum) / matrix_a.get(i, {}).get(i, 1)
            # print("Iteratia", k)
            # print(xGS)
            print(calculate_norm(matrix_a, vector_b, xGS))
        delta_x = np.linalg.norm(xGS - old_xGS)

        if delta_x < epsilon or delta_x > 10**8:
            break

    if delta_x < epsilon:
        print(f"Metoda Gauss-Seidel a convergat dupa {k} iteratii")
        return xGS
    else:
        return 0

def gauss_seidel_list(valori, ind_col, inceput_linii, vector_b, dimension_a, epsilon=1e-9, kmax=10000):
    xGS = np.zeros(dimension_a)

    for k in range(kmax):
        old_xGS = xGS.copy()

        for i in range(dimension_a):
            lower_sum = 0
            upper_sum = 0
            diagonal = 0

            start = inceput_linii[i]
            end = inceput_linii[i + 1]
            for idx in range(start, end):
                j = ind_col[idx]
                value = valori[idx]
                if j < i:
                    lower_sum += value * xGS[j]
                elif j > i:
                    upper_sum += value * xGS[j]

            for idx in range(start, end):
                j = ind_col[idx]
                value = valori[idx]
                if j == i:
                    diagonal += value

            xGS[i] = (vector_b[i] - lower_sum - upper_sum) / diagonal

        delta_x = np.linalg.norm(xGS - old_xGS)

        if delta_x < epsilon or delta_x > 1e8:
            break

    if delta_x < epsilon:
        print(f"Metoda Gauss-Seidel a convergat după {k} iteratii")
        return xGS
    else:
        return 0

def calculate_error(matrix_a, vector_b, solution):
    error_vector = np.zeros_like(vector_b)

    for i, row in matrix_a.items():
        for j, value in row.items():
            error_vector[i] += value * solution[j]

    error_norm = np.linalg.norm(error_vector - vector_b)
    return error_norm

def calculate_norm(matrix_a, vector_b, solution):
    Ax = np.zeros_like(vector_b)

    for i, row in matrix_a.items():
        for j, value in row.items():
            Ax[i] += value * solution[j]

    norm_inf = np.max(np.abs(Ax - vector_b))
    return norm_inf

def calculate_error_list(valori, ind_col, inceput_linii, vector_b, solution):
    error_vector = np.zeros_like(vector_b)

    for i in range(len(inceput_linii) - 1):
        start = inceput_linii[i]
        end = inceput_linii[i + 1]
        for idx in range(start, end):
            j = ind_col[idx]
            value = valori[idx]
            error_vector[i] += value * solution[j]

    error_norm = np.linalg.norm(error_vector - vector_b)
    return error_norm

def calculate_norm_list(valori, ind_col, inceput_linii, vector_b, solution):
    Ax = np.zeros_like(vector_b)

    for i in range(len(inceput_linii) - 1):
        start = inceput_linii[i]
        end = inceput_linii[i + 1]
        for idx in range(start, end):
            j = ind_col[idx]
            value = valori[idx]
            Ax[i] += value * solution[j]

    norm_inf = np.max(np.abs(Ax - vector_b))
    return norm_inf

def sparse_representation_dict(matrix):
    sparse_matrix = {}
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value != 0:
                sparse_matrix.setdefault(row_idx, {})[col_idx] = value
    return sparse_matrix

if __name__ == '__main__':
    if (input("Do you want to use the default values? (y/n): ") == "y"):
        matrix = [[102.5, 0.0, 2.5, 0.0, 0.0], [3.5, 104.88, 1.05, 0.0, 0.33], [0.0, 0.0, 100.0, 0.0, 0.0], [0.0, 1.3, 0.0, 101.3, 0.0], [0.73, 0.0, 0.0, 1.5, 102.23]]
        vector = [6.0, 7.0, 8.0, 9.0, 1.0]
        sparse_matrix = sparse_representation_dict(matrix)
        solution = gauss_seidel(sparse_matrix, vector, len(matrix))
        if np.all(solution == 0):
            print("Divergență...")
        else:
            print("Solutia sistemului este:", solution)
            error = calculate_error(sparse_matrix, vector, solution)
            print("Eroarea:", error)
            norm_inf = calculate_norm(sparse_matrix, vector, solution)
            print("Norma infinita:", norm_inf)
    else:
        dimension_a, matrix_a, dimension_b, vector_b = read_data('a_5.txt', 'b_5.txt')
        # print("Matricea A:", matrix_a)
        # valori, ind_col, inceput_linii = sparse_matrix_representation(matrix_a)
        # print("Valori:", valori)
        # print("Indici coloane:", ind_col)
        # print("Inceput linii:", inceput_linii)
        if check_diagonal_not_null(matrix_a, dimension_a) == 1:
            print("Matricea A are diagonala nenula")
        else:
            print("Matricea A nu are diagonala nenula")
            exit(0)

        solution = gauss_seidel(matrix_a, vector_b, dimension_a)
        if np.all(solution == 0):
            print("Divergență...")
        else:
            print("Solutia sistemului este:", solution)
            error = calculate_error(matrix_a, vector_b, solution)
            print("Eroarea:", error)
            norm_inf = calculate_norm(matrix_a, vector_b, solution)
            print("Norma infinita:", norm_inf)

        # valori, ind_col, inceput_linii = sparse_matrix_representation(matrix_a)
        # solution = gauss_seidel_list(valori, ind_col, inceput_linii, vector_b, dimension_a)
        # if np.all(solution == 0):
        #     print("Divergență...")
        # else:
        #     print("Soluția sistemului este:", solution)
        #     error = calculate_error_list(valori, ind_col, inceput_linii, vector_b, solution)
        #     print("Eroarea:", error)
        #     norm_inf = calculate_norm_list(valori, ind_col, inceput_linii, vector_b, solution)
        #     print("Norma infinită:", norm_inf)


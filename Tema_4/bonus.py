import numpy as np

def read_sparse_matrix(file_name):

    with open(file_name, 'r') as file:
        dimension = int(file.readline().strip())
        sparse_matrix = {}

        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                value, row, col = map(float, parts)
                row = int(row)
                col = int(col)
                sparse_matrix.setdefault(row, {})[col] = sparse_matrix.get((row, col), 0) + value

    return sparse_matrix, dimension

def sum_sparse_matrix(matrix_a, matrix_b):
    result_matrix = {}
    for row, cols in matrix_a.items():
        for col, value in cols.items():
            result_matrix.setdefault(row, {})[col] = value

    for row, cols in matrix_b.items():
        for col, value in cols.items():
            result_matrix[row][col] = result_matrix.get(row, {}).get(col, 0) + value

    return result_matrix

def compare_matrices(matrix_a, matrix_b, epsilon=1e-9):
    for row, cols in matrix_a.items():
        for col, value in cols.items():
            if abs(value - matrix_b.get(row, {}).get(col, 0)) > epsilon:
                return False
    return True

if __name__ == '__main__':
    matrix_a, dimension_a = read_sparse_matrix('a.txt')
    matrix_b, dimension_b = read_sparse_matrix('b.txt')

    if dimension_a != dimension_b:
        print("Dimensiunile matricelor nu corespund...")
        exit(0)

    sum_matrix = sum_sparse_matrix(matrix_a, matrix_b)

    marix_aplusb, dimension_aplusb = read_sparse_matrix('aplusb.txt')

    if compare_matrices(sum_matrix, marix_aplusb):
        print(" a + b = aplusb.txt")
    else:
        print(" a + b != aplusb.txt")

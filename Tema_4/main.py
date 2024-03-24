import numpy as np

def read_data(file_name_a, file_name_b):
    with open(file_name_a, 'r') as file:
        dimension_a = int(file.readline())
        matrix_a = np.zeros((dimension_a, dimension_a))
        for line in file:
            value, row, col = map(float, line.split(','))
            row = int(row)
            col = int(col)
            matrix_a[row][col] = value

    with open(file_name_b, 'r') as file:
        dimension_b = int(file.readline())
        vector_b = np.zeros((dimension_b))
        for i in range(dimension_b):
            value = float(file.readline())
            vector_b[i] = value

    return dimension_a, matrix_a, dimension_b, vector_b

def store_matrix_in_list(A):
    matrix_list = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            if A[i][j] != 0:
                row.append((A[i][j], j))
        matrix_list.append(row)
    return matrix_list

def store_matrix_in_dictionary(A):
    matrix_dictionary = {}
    for i in range(len(A)):
        for j in range (len(A)):
            if (A[i][j]) !=0:
                matrix_dictionary[(i,j)] = A[i][j]

    return matrix_dictionary

def check_diagonal_not_null(A):
    for i in range(len(A)):
        if A[i][i] == 0:
            return 0
    return 1


if __name__ == '__main__':
    dimension_a, matrix_a, dimension_b, vector_b = read_data('a_5.txt', 'b_5.txt')
    if (check_diagonal_not_null(matrix_a) == 1):
        print("Matricea A are diagonala nenula")
    else:
        print("Matricea A nu are diagonala nenula")

    matrix_list = store_matrix_in_list(matrix_a)
    matrix_dictionary = store_matrix_in_dictionary(matrix_a)









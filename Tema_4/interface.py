import streamlit as st
import numpy as np
from main import check_diagonal_not_null, gauss_seidel, calculate_error, calculate_norm

import numpy as np
from io import BytesIO

def read_data(file_a, file_b):
    with BytesIO(file_a.read()) as file:
        dimension_a = int(file.readline().strip())
        sparse_matrix_a = {}

        for line in file:
            parts = line.strip().split(b',')
            if len(parts) == 3:
                value, row, col = map(float, parts)
                row = int(row)
                col = int(col)
                sparse_matrix_a.setdefault(row, {})[col] = sparse_matrix_a.get((row, col), 0) + value

    with BytesIO(file_b.read()) as file:
        dimension_b = int(file.readline())
        vector_b = np.zeros((dimension_b))
        for i in range(dimension_b):
            value = float(file.readline())
            vector_b[i] = value

    return dimension_a, sparse_matrix_a, dimension_b, vector_b

def main():
    st.title("Sparse Matrix Solver")


    file_a = st.file_uploader("Upload matrix file:")
    file_b = st.file_uploader("Upload vector file:")

    if file_a and file_b:
            dimension_a, matrix_a, dimension_b, vector_b = read_data(file_a, file_b)
            if check_diagonal_not_null(matrix_a, dimension_a) == 1:
                st.write("Matrix A has non-null diagonal.")
            else:
                st.write("Matrix A doesn't have non-null diagonal.")
                st.stop()

            solution = gauss_seidel(matrix_a, vector_b, dimension_a)
            if np.all(solution == 0):
                st.write("Divergence...")
            else:
                st.write("Solution:", solution)
                error = calculate_error(matrix_a, vector_b, solution)
                st.write("Error:", error)
                norm_inf = calculate_norm(matrix_a, vector_b, solution)
                st.write("Infinity norm:", norm_inf)

if __name__ == "__main__":
    main()

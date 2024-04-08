import streamlit as st
import numpy as np
import copy

from main import jacobi_method, calculate_norm, svd_pseudoinverse, pseudo_inverse_least_squares, calculate_L1_norm, calculate_svd_properties, cholesky_iteration

def main():
    st.title('Numerical Linear Algebra Exercises')

    exercise = st.sidebar.selectbox(
        "Choose an exercise",
        ("Exercise 1", "Exercise 2", "Exercise 3")
    )

    if exercise == "Exercise 1":
        st.subheader("Exercise 1")
        A_input = st.text_area("Enter matrix A separated by spaces (rows separated by new lines)")
        if A_input:
            A = np.array([[float(num) for num in line.split()] for line in A_input.split('\n')])
            eps = 1e-15
            max_iter = 10000
            valori_proprii, U = jacobi_method(A, eps, max_iter)
            st.write("Eigenvalues:", valori_proprii)
            st.write("Eigenvectors (U):", U)
            norm = calculate_norm(copy.deepcopy(A), U, valori_proprii)
            st.write("Norm:", norm)

    elif exercise == "Exercise 2":
        st.subheader("Exercise 2")
        A = np.array([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
        eigenvalues, _ = np.linalg.eigh(A)
        st.write("Eigenvalues of matrix A:", eigenvalues)
        result = cholesky_iteration(A)
        st.write("Last calculated matrix:", result)

    elif exercise == "Exercise 3":
        st.subheader("Exercise 3")
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [15, 11, 12]])
        U, S, _ = np.linalg.svd(A)
        rank = np.count_nonzero(S)
        condition_number = np.max(S) / np.min(S)
        A_pseudo = svd_pseudoinverse(A)
        A_J = pseudo_inverse_least_squares(A)
        norm_L1 = calculate_L1_norm(A, A_J)
        st.write("Singular values of matrix A:", S)
        st.write("Rank of matrix A:", rank)
        st.write("Condition number of matrix A:", condition_number)
        st.write("Pseudoinverse of matrix A:", A_pseudo)
        st.write("Least squares pseudo-inverse (A^J):", A_J)
        st.write("L1 Norm between A and A^J:", norm_L1)

if __name__ == "__main__":
    main()

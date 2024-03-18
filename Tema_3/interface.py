import copy
import numpy as np
import streamlit as st
from main import determine_vector_b, qr_decomposition, solve_linear_system, determine_inv_A

def main():

    st.title("QR Decomposition and Linear System Solver")

    n = st.number_input("Enter the dimension n of the matrix A", min_value=1, step=1)
    A = np.zeros((n, n))
    st.subheader("Enter the matrix A:")
    for i in range(n):
        cols = st.columns(n)
        for j in range(n):
            A[i][j] = cols[j].number_input(f"A[{i}][{j}]", value=0.0)

    st.subheader("Enter the vector s:")
    cols = st.columns(n)
    s = np.zeros(n)
    for i in range(n):
        s[i] = cols[i].number_input(f"s[{i}]", value=0.0)

    A_init = copy.deepcopy(A)
    b = determine_vector_b(A, s)
    if st.button("Show vector b"):
        st.subheader("Vector b:")
        st.write(b)

    Q, R, b = qr_decomposition(A, b)
    if st.button("Show Matrix Q"):
        st.subheader("Matrix Q:")
        st.write(Q)

    if st.button("Show Matrix R"):
        st.subheader("Matrix R:")
        st.write(R)

    try:
        if st.button("Show Solution of Ax = b"):
            x = solve_linear_system(b, R)
            st.subheader("Solution of the system Ax = b:")
            st.write(x)

        A_inv = determine_inv_A(A_init,Q,R)
        if st.button("Show Inverse of matrix A"):
            st.subheader("Inverse of matrix A:")
            st.write(A_inv)
    except np.linalg.LinAlgError:
        st.error("Matrix A is singular and cannot be inverted.")

if __name__ == "__main__":
    main()

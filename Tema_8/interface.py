import streamlit as st
from main import gradient_descent, F1, F2, F3, F4

# Define the Streamlit app
def main():
    st.title("Optimizarea Funcțiilor cu Gradient Descent")

    # Define the functions
    function_names = ["F1", "F2", "F3", "F4"]
    selected_function = st.selectbox("Alegeți o funcție", function_names)

    functions = {
        "F1": F1,
        "F2": F2,
        "F3": F3,
        "F4": F4
    }

    selected_func = functions[selected_function]

    # Define the gradient methods and eta methods
    gradient_methods = ['analytical', 'approximate']
    eta_methods = ['constant', 'backtracking']
    selected_gradient_method = st.radio("Alegeți metoda de gradient", gradient_methods)
    selected_eta_method = st.radio("Alegeți metoda de eta", eta_methods)

    eta = 0.01
    epsilon = 1e-5

    if st.button("Rulează Gradient Descent"):
        st.write(f"Ați ales funcția: {selected_function}")
        st.write(f"Metoda de gradient: {selected_gradient_method}")
        st.write(f"Metoda de eta: {selected_eta_method}")

        sol, num_iterations = gradient_descent(selected_func, -2, 1, gradient_method=selected_gradient_method, eta_method=selected_eta_method, eta=eta, epsilon=epsilon)
        if num_iterations < 30000:
            convergence = "Da"
        else:
            convergence = "Nu"
        st.write(f"Solutie (x): {sol[0]}, Solutie (y): {sol[1]}, Nr. iteratii: {num_iterations}, Convergenta: {convergence}")

# Run the Streamlit app
if __name__ == "__main__":
    main()

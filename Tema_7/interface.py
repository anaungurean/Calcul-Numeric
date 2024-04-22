import streamlit as st
from main import muller_method, save_roots_to_file

# Define the Streamlit app
def main():
    st.title("Metoda Muller pentru găsirea rădăcinilor")

    num_coefficients = st.number_input("Numărul de coeficienți", min_value=1, step=1, value=1)

    coefficients = []
    for i in range(num_coefficients):
        coefficient = st.number_input(f"Coefficient {i+1}", step=0.1)
        coefficients.append(coefficient)

    if st.button("Găsește rădăcinile"):
        roots = muller_method(coefficients)

        if roots:
            st.write("Rădăcinile polinomului sunt:")
            for root in roots:
                st.write(root)
            save_roots_to_file(roots, 'roots.txt')
        else:
            st.write("Nu s-au găsit rădăcini pentru polinomul introdus.")

# Run the Streamlit app
if __name__ == "__main__":
    main()

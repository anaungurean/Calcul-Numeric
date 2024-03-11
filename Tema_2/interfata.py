import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button, Text, messagebox
from Tema_2.main import descompunere_LU, determinant_A

class Interfata(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("500x550")

        self.label_dimensiune = Label(self, text="Introduceti dimensiunea n a datelor:")
        self.label_dimensiune.pack(pady=10)

        self.entry_dimensiune = Entry(self)
        self.entry_dimensiune.pack(pady=10)

        self.label_t = Label(self, text="Introduceti valoarea t (5,...,10) pentru calculul variabilei epsilon:")
        self.label_t.pack(pady=10)

        self.entry_t = Entry(self)
        self.entry_t.pack(pady=10)

        self.label_matrice = Label(self, text="Introduceti matricea A (linie cu linie):")
        self.label_matrice.pack(pady=10)

        self.text_matrice = Text(self, height=10, width=30)
        self.text_matrice.pack(pady=10)

        self.buton_det = Button(self, text="Afiseaza determinantul", command=self.afiseaza_det)
        self.buton_det.pack(pady=10)

        self.buton_afiseaza_L = Button(self, text="Afiseaza matricea L", command=self.afiseaza_matrice_L)
        self.buton_afiseaza_L.pack(pady=10)

        self.buton_afiseaza_U = Button(self, text="Afiseaza matricea U", command=self.afiseaza_matrice_U)
        self.buton_afiseaza_U.pack(pady=10)

    def afiseaza_matrice(self, matrice, titlu):
        messagebox.showinfo(titlu, str(matrice))

    def citeste_matrice(self, n):
        A_init = np.zeros((n, n))
        matrice_text = self.text_matrice.get("1.0", "end-1c").split("\n")

        for i in range(n):
            row_values = list(map(float, matrice_text[i].split()))
            A_init[i] = row_values

        return A_init

    def afiseaza_det(self):
        n = int(self.entry_dimensiune.get())
        t = float(self.entry_t.get())

        epsilon = 10 ** (-t)

        A_init = self.citeste_matrice(n)
        A = A_init.copy()

        try:
            descompunere_LU(epsilon, n, A)
            det = determinant_A(n, A)
            messagebox.showinfo("Determinant", f"Determinantul matricei A este: {det}")
        except Exception as e:
            messagebox.showerror("Eroare", f"Calculul determinantului a esuat: {e}")

    def afiseaza_matrice_L(self):
        n = int(self.entry_dimensiune.get())
        t = float(self.entry_t.get())

        epsilon = 10 ** (-t)

        A_init = self.citeste_matrice(n)
        A = A_init.copy()

        try:
            descompunere_LU(epsilon, n, A)
            self.afiseaza_matrice(np.tril(A), "Matricea L")
        except ValueError as e:
            messagebox.showerror("Eroare", str(e))

    def afiseaza_matrice_U(self):
        n = int(self.entry_dimensiune.get())
        t = float(self.entry_t.get())

        epsilon = 10 ** (-t)

        A_init = self.citeste_matrice(n)
        A = A_init.copy()

        try:
            descompunere_LU(epsilon, n, A)

            matrice_U = np.triu(A)
            np.fill_diagonal(matrice_U, 1)

            self.afiseaza_matrice(matrice_U, "Matricea U")
        except ValueError as e:
            messagebox.showerror("Eroare", str(e))


if __name__ == '__main__':
    app = Interfata()
    app.mainloop()

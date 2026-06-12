import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(51)
    plt.bar(["a) P(Filtro | Aceite)", "b) P(Aceite | Filtro)"],
            [prob_a, prob_b], color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.80 — Cambio de aceite y filtro")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "aceite_filtro")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.80
La probabilidad de que al llenar el tanque de gasolina
también se necesite cambiar el aceite es 0.25, de que
se necesite cambiar el filtro de aceite es 0.40, y de
que se necesite cambiar ambos es 0.14.

a) Si se cambia el aceite, ¿cuál es la probabilidad de
   que también se necesite cambiar el filtro?
b) Si se cambia el filtro, ¿cuál es la probabilidad de
   que también se necesite cambiar el aceite?
=========================================================
"""
    print(enunciado)

    P_A = 0.25
    P_F = 0.40
    P_A_int_F = 0.14

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(Filtro | Aceite) = P(F ∩ A) / P(A).")
    prob_a = P_A_int_F / P_A
    print(f"-> P(F | A) = {P_A_int_F} / {P_A} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(Aceite | Filtro) = P(A ∩ F) / P(F).")
    prob_b = P_A_int_F / P_F
    print(f"-> P(A | F) = {P_A_int_F} / {P_F} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

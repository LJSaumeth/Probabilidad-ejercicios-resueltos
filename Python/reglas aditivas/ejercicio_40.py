import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(40)
    colores = ["#2ecc71", "#e74c3c", "#f39c12", "#3498db", "#9b59b6"]
    plt.bar(etiquetas, valores, color=colores)
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.69 — Llenado de cajas")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.3f}" if v >= 0.01 else f"{v:.4f}", ha="center")
    guardar_figura(out, "llenado_cajas")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.69
En áreas industriales se usan máquinas para llenar cajas.
Dichas máquinas pueden cumplir especificaciones (A), llenar
por debajo del nivel (B) o rebasar el límite (C).
Sea P(B) = 0.001 y P(A) = 0.990.

a) Determine P(C).
b) ¿Cuál es la probabilidad de que la máquina no llene
   de manera suficiente?
c) ¿Cuál es la probabilidad de que la máquina llene de más
   o de menos?
=========================================================
"""
    print(enunciado)

    P_A = 0.990
    P_B = 0.001

    print("--- SOLUCIÓN a) ---")
    print("Explicación: A, B y C son mutuamente excluyentes y exhaustivos (partición del espacio muestral).")
    print("Por lo tanto: P(A) + P(B) + P(C) = 1")
    P_C = 1 - P_A - P_B
    print(f"-> P(C) = 1 − P(A) − P(B) = 1 − {P_A} − {P_B} = {P_C}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'No llene de manera suficiente' significa llenar por debajo = evento B.")
    print(f"-> P(insuficiente) = P(B) = {P_B}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: 'Llene de más o de menos' = B ∪ C. Como son mutuamente excluyentes:")
    P_B_o_C = P_B + P_C
    print(f"-> P(B ∪ C) = P(B) + P(C) = {P_B} + {P_C} = {P_B_o_C}")

    crear_graficas(
        ["P(A) Correcto", "P(B) Insuficiente", "P(C) Exceso", "P(B ∪ C) Defectuoso", "P(Perfecto)"],
        [P_A, P_B, P_C, P_B_o_C, P_A]
    )


if __name__ == "__main__":
    main()

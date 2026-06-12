import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(92)
    plt.bar(["P(Insatisfecho | Vendedor A)"], [prob], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.125 — Software estadístico")
    plt.text(0, prob / 2, f"{prob:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "software_satisfaccion")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.125
Encuesta de software estadístico: 10% no quedó satisfecho.
La mitad de los insatisfechos compraron al vendedor A.
20% de los encuestados compraron al vendedor A. Dado que
el proveedor fue A, ¿cuál es la probabilidad de que un
usuario específico haya quedado insatisfecho?
=========================================================
"""
    print(enunciado)

    P_I = 0.10                  # P(insatisfecho)
    P_A_dado_I = 0.50           # P(vendedor A | insatisfecho)
    P_A = 0.20                  # P(vendedor A)

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Se pide P(Insatisfecho | Vendedor A).")
    print()

    print("Usamos la forma alternativa de Bayes:")
    print("              P(A|I) × P(I)")
    print("  P(I|A) = ───────────────────")
    print("                  P(A)")
    print()

    num = P_A_dado_I * P_I
    prob = num / P_A
    print(f"            {P_A_dado_I} × {P_I}     {num:.4f}")
    print(f"  P(I|A) = ───────────── = ─────── = {prob:.4f}")
    print(f"               {P_A}         {P_A}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

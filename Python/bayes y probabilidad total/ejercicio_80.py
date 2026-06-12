import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(80)
    plt.bar(["a) 3 del mismo color", "b) Cada color representado"],
            [prob_a, prob_b], color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.113 — Bolas con reemplazo")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "bolas_reemplazo")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.113
De una caja con 6 bolas negras y 4 verdes se extraen 3
bolas sucesivamente CON reemplazo. ¿Probabilidad de que:

a) las 3 sean del mismo color?
b) cada color esté representado?
=========================================================
"""
    print(enunciado)

    P_N = 6/10
    P_V = 4/10

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'Mismo color' = 3 negras O 3 verdes (independientes c/reemplazo).")
    p_3N = P_N ** 3
    p_3V = P_V ** 3
    prob_a = p_3N + p_3V
    print(f"  P(3 negras) = ({P_N})³ = {p_3N:.4f}")
    print(f"  P(3 verdes) = ({P_V})³ = {p_3V:.4f}")
    print(f"  P(mismo color) = {p_3N:.4f} + {p_3V:.4f} = {prob_a:.4f}")
    print()

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Cada color representado' significa que hay al menos 1 negra y al menos 1 verde en las 3 extracciones.")
    print("Esto excluye los casos '3 negras' y '3 verdes'.")
    prob_b = 1 - prob_a
    print(f"  P(cada color) = 1 − P(mismo color) = 1 − {prob_a:.4f} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

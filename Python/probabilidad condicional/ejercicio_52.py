import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b, prob_c):
    out = carpeta_graficas(52)
    plt.bar(["a) Ambos ven", "b) Esposa|Esposo ve", "c) Al menos uno ve"],
            [prob_a, prob_b, prob_c], color=["#e74c3c", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.81 — Pareja viendo TV")
    for i, v in enumerate([prob_a, prob_b, prob_c]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "pareja_tv")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.81
La probabilidad de que un hombre casado vea cierto programa
de televisión es 0.4 y la probabilidad de que lo vea una
mujer casada es 0.5. La probabilidad de que un hombre vea
el programa, dado que su esposa lo ve, es 0.7.

Calcule la probabilidad de que:

a) una pareja casada vea el programa;
b) una esposa vea el programa dado que su esposo lo ve;
c) al menos uno de los miembros de la pareja vea el
   programa.
=========================================================
"""
    print(enunciado)

    P_H = 0.4
    P_M = 0.5
    P_H_dado_M = 0.7

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'Ambos vean' = P(H ∩ M). Usamos: P(H|M) = P(H∩M) / P(M)")
    print("Despejando: P(H ∩ M) = P(H|M) × P(M)")
    P_H_int_M = P_H_dado_M * P_M
    print(f"-> P(H ∩ M) = {P_H_dado_M} × {P_M} = {P_H_int_M}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(M|H) = P(M∩H) / P(H).")
    P_M_dado_H = P_H_int_M / P_H
    print(f"-> P(M | H) = {P_H_int_M} / {P_H} = {P_M_dado_H:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: P(H ∪ M) = P(H) + P(M) − P(H ∩ M).")
    P_union = P_H + P_M - P_H_int_M
    print(f"-> P(H ∪ M) = {P_H} + {P_M} − {P_H_int_M} = {P_union}")

    crear_graficas(P_H_int_M, P_M_dado_H, P_union)


if __name__ == "__main__":
    main()

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b, prob_c):
    out = carpeta_graficas(53)
    plt.bar(["a) Al menos 1 vota", "b) Esposa|Esposo vota", "c) Esposo|Esposa no vota"],
            [prob_a, prob_b, prob_c], color=["#2ecc71", "#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.82 — Pareja votando")
    for i, v in enumerate([prob_a, prob_b, prob_c]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "pareja_votando")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.82
Para parejas casadas en cierto suburbio:
P(esposo vote) = 0.21, P(esposa vote) = 0.28,
P(ambos voten) = 0.15.

a) ¿Probabilidad de que al menos uno vote?
b) ¿Probabilidad de que una esposa vote, dado que su
   esposo vota?
c) ¿Probabilidad de que un esposo vote, dado que su
   esposa no vota?
=========================================================
"""
    print(enunciado)

    P_H = 0.21
    P_M = 0.28
    P_H_int_M = 0.15

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(H ∪ M) = P(H) + P(M) − P(H ∩ M).")
    prob_a = P_H + P_M - P_H_int_M
    print(f"-> P(H ∪ M) = {P_H} + {P_M} − {P_H_int_M} = {prob_a}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(M | H) = P(M ∩ H) / P(H).")
    prob_b = P_H_int_M / P_H
    print(f"-> P(M | H) = {P_H_int_M} / {P_H} = {prob_b:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: P(H | M') = P(H ∩ M') / P(M').")
    print("P(H ∩ M') = P(H) − P(H ∩ M).")
    P_H_solo = P_H - P_H_int_M
    P_no_M = 1 - P_M
    prob_c = P_H_solo / P_no_M
    print(f"-> P(H ∩ M') = {P_H} − {P_H_int_M} = {P_H_solo}")
    print(f"-> P(M') = 1 − {P_M} = {P_no_M}")
    print(f"-> P(H | M') = {P_H_solo} / {P_no_M} = {prob_c:.4f}")

    crear_graficas(prob_a, prob_b, prob_c)


if __name__ == "__main__":
    main()

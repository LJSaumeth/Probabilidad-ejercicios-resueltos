import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b, prob_c):
    out = carpeta_graficas(54)
    plt.bar(["a) P(Canadá|Casa rod.)", "b) P(Casa rod.|Canadá)", "c) P(no Can. o no CR)"],
            [prob_a, prob_b, prob_c], color=["#e74c3c", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.83 — Cavernas Luray")
    for i, v in enumerate([prob_a, prob_b, prob_c]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "cavernas_luray")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.83
La probabilidad de que un vehículo en las Cavernas Luray
tenga matrícula de Canadá es 0.12, de que sea casa rodante
es 0.28 y de que sea casa rodante con matrícula de Canadá
es 0.09.

a) P(una casa rodante tenga matrícula de Canadá)
b) P(un vehículo con matrícula de Canadá sea casa rodante)
c) P(un vehículo no tenga matrícula de Canadá o no sea
   casa rodante)
=========================================================
"""
    print(enunciado)

    P_C = 0.12
    P_R = 0.28
    P_C_int_R = 0.09

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(Canadá | Casa rodante) = P(C ∩ R) / P(R).")
    prob_a = P_C_int_R / P_R
    print(f"-> P(C | R) = {P_C_int_R} / {P_R} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(Casa rodante | Canadá) = P(R ∩ C) / P(C).")
    prob_b = P_C_int_R / P_C
    print(f"-> P(R | C) = {P_C_int_R} / {P_C} = {prob_b:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: P(C' ∪ R') = P((C ∩ R)') por De Morgan = 1 − P(C ∩ R).")
    prob_c = 1 - P_C_int_R
    print(f"-> P(C' ∪ R') = 1 − P(C ∩ R) = 1 − {P_C_int_R} = {prob_c}")

    crear_graficas(prob_a, prob_b, prob_c)


if __name__ == "__main__":
    main()

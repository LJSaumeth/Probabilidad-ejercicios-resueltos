import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(77)
    plt.bar(["a) Exactamente 2 sobrevivan", "b) Los 3 sobrevivan"],
            [prob_a, prob_b], color=["#e74c3c", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.110 — Operación de corazón")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "operacion_corazon")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.110
La probabilidad de que un paciente se recupere de una
delicada operación de corazón es 0.8. ¿Cuál es la
probabilidad de que:

a) exactamente 2 de los siguientes 3 pacientes sobrevivan?
b) los siguientes 3 pacientes sobrevivan?
=========================================================
"""
    print(enunciado)

    p = 0.8
    n = 3

    print("--- SOLUCIÓN (Distribución binomial) ---")
    print("P(X=k) = C(n,k) × p^k × (1−p)^(n−k)")
    print()

    print("--- a) Exactamente 2 de 3 ---")
    k = 2
    comb = math.comb(n, k)
    prob_a = comb * (p ** k) * ((1 - p) ** (n - k))
    print(f"  C(3, 2) = {comb}")
    print(f"  P(X=2) = {comb} × ({p})² × ({1-p})¹ = {comb} × {p**2} × {1-p} = {prob_a:.4f}")
    print()

    print("--- b) Los 3 sobrevivan ---")
    prob_b = p ** 3
    print(f"  P(X=3) = ({p})³ = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

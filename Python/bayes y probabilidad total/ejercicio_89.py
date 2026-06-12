import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(89)
    plt.bar(["a) 3 defectuosos", "b) 3 de 4 defectuosos"],
            [prob_a, prob_b], color=["#e74c3c", "#f39c12"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.122 — Control de calidad")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.002, f"{v:.4f}", ha="center")
    guardar_figura(out, "control_calidad")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.122
Un proceso está fuera de control y 20% de los artículos
tiene defecto.

a) Si 3 artículos salen en serie, ¿probabilidad de que los
   3 estén defectuosos?
b) Si salen 4 artículos, ¿probabilidad de que 3 estén
   defectuosos?
=========================================================
"""
    print(enunciado)

    p = 0.20
    q = 1 - p

    print("--- SOLUCIÓN (Distribución binomial) ---")
    print()

    print("--- a) Los 3 defectuosos ---")
    prob_a = p ** 3
    print(f"  P(3 defect.) = ({p})³ = {prob_a:.4f}")
    print()

    print("--- b) Exactamente 3 de 4 defectuosos ---")
    k = 3
    n = 4
    comb = math.comb(n, k)
    prob_b = comb * (p ** k) * (q ** (n - k))
    print(f"  C(4, 3) = {comb}")
    print(f"  P(X=3) = {comb} × ({p})³ × ({q})¹ = {comb} × {p**3} × {q} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_3, prob_0):
    out = carpeta_graficas(71)
    plt.bar(["a) Exactamente 3 alérgicos", "b) Ninguno alérgico"],
            [prob_3, prob_0], color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.104 — Alergia a hierbas")
    for i, v in enumerate([prob_3, prob_0]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "alergia_hierbas")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.104
Un alergólogo afirma que 50% de sus pacientes son alérgicos
a algún tipo de hierba. ¿Cuál es la probabilidad de que:

a) exactamente 3 de sus 4 pacientes siguientes sean
   alérgicos?
b) ninguno de sus 4 pacientes siguientes sea alérgico?
=========================================================
"""
    print(enunciado)

    p = 0.5
    n = 4

    print("--- SOLUCIÓN (Distribución binomial) ---")
    print("Explicación: Cada paciente es un ensayo independiente con P(alérgico)=0.5.")
    print("Usamos la fórmula binomial: P(X=k) = C(n,k) × p^k × (1−p)^(n−k)")
    print()

    print("--- a) Exactamente 3 de 4 ---")
    k = 3
    comb = math.comb(n, k)
    prob_a = comb * (p ** k) * ((1 - p) ** (n - k))
    print(f"  C(4, 3) = {comb}")
    print(f"  P(X=3) = {comb} × ({p})³ × ({1-p})¹ = {comb} × {p**3} × {1-p} = {prob_a:.4f}")
    print()

    print("--- b) Ninguno de 4 ---")
    k = 0
    comb = math.comb(n, k)
    prob_b = comb * (p ** k) * ((1 - p) ** (n - k))
    print(f"  C(4, 0) = {comb}")
    print(f"  P(X=0) = {comb} × ({p})⁰ × ({1-p})⁴ = 1 × 1 × {(1-p)**4} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

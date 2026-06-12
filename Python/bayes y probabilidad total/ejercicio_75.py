import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(75)
    plt.bar(["a) 4 cometan error", "b) Jones+Clark sí, Roberts+Williams no"],
            [prob_a, prob_b], color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.108 — Errores en declaración de impuestos")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.0005, f"{v:.6f}", ha="center")
    guardar_figura(out, "errores_impuestos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.108
La probabilidad de que una persona cometa un error en su
declaración de impuestos es 0.1. Calcule la probabilidad:

a) cada una de cuatro personas no relacionadas cometa un
   error;
b) el Sr. Jones y la Sra. Clark cometan un error, y el
   Sr. Roberts y la Sra. Williams no cometan errores.
=========================================================
"""
    print(enunciado)

    p = 0.1
    q = 1 - p

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Eventos independientes. Los 4 cometan error = p⁴.")
    prob_a = p ** 4
    print(f"  P(los 4 error) = ({p})⁴ = {prob_a:.4f}")
    print()

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Dos personas específicas (Jones, Clark) error Y dos (Roberts, Williams) no error.")
    prob_b = (p ** 2) * (q ** 2)
    print(f"  P(Jones error) × P(Clark error) × P(Roberts bien) × P(Williams bien)")
    print(f"  = {p} × {p} × {q} × {q} = {p}² × {q}² = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

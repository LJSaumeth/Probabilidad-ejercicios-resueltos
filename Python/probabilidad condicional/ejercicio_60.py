import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(60)
    plt.bar(["a) Ninguno disponible", "b) Al menos uno disponible"],
            [prob_a, prob_b], color=["#e74c3c", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.89 — Carros de bomberos")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.002, f"{v:.4f}", ha="center")
    guardar_figura(out, "carros_bomberos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.89
Una ciudad tiene dos carros de bomberos que operan de
forma independiente. La probabilidad de que un carro
específico esté disponible cuando se le necesite es 0.96.

a) ¿Cuál es la probabilidad de que ninguno esté disponible?
b) ¿Cuál es la probabilidad de que un carro de bomberos
   esté disponible cuando se le necesite?
=========================================================
"""
    print(enunciado)

    P_disponible = 0.96
    P_no_disponible = 1 - P_disponible

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Como son independientes, P(ninguno disponible) = P(no disponible)².")
    prob_a = P_no_disponible ** 2
    print(f"-> P(no disponible cada uno) = 1 − {P_disponible} = {P_no_disponible}")
    print(f"-> P(ninguno) = {P_no_disponible}² = {prob_a}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Al menos uno disponible' = complemento de 'ninguno disponible'.")
    print("P(al menos uno) = 1 − P(ninguno).")
    prob_b = 1 - prob_a
    print(f"-> P(al menos uno) = 1 − {prob_a} = {prob_b}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

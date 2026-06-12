import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(24)
    plt.bar(etiquetas, valores, color=["#3498db", "#2ecc71", "#e74c3c", "#f39c12"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.53 — Ubicación de industria")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.2f}", ha="center")
    guardar_figura(out, "ubicacion_industria")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.53
La probabilidad de que una industria estadounidense se
ubique en Shanghai es 0.7, en Beijing es 0.4 y en
Shanghai o Beijing (o ambas) es 0.8.

¿Cuál es la probabilidad de que la industria se ubique:

a) en ambas ciudades?
b) en ninguna de esas ciudades?
=========================================================
"""
    print(enunciado)

    P_S = 0.7
    P_B = 0.4
    P_S_union_B = 0.8

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Usamos la regla aditiva de probabilidad:")
    print("P(S ∪ B) = P(S) + P(B) − P(S ∩ B)")
    print("Despejando: P(S ∩ B) = P(S) + P(B) − P(S ∪ B)")
    P_interseccion = P_S + P_B - P_S_union_B
    print(f"-> P(S ∩ B) = {P_S} + {P_B} − {P_S_union_B} = {P_interseccion}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'En ninguna ciudad' es el complemento de la unión:")
    print("P(ninguna) = 1 − P(S ∪ B)")
    P_ninguna = 1 - P_S_union_B
    print(f"-> P(ninguna) = 1 − {P_S_union_B} = {P_ninguna}")

    crear_graficas(
        ["P(S)", "P(B)", "P(S ∪ B)", "P(S ∩ B)"],
        [P_S, P_B, P_S_union_B, P_interseccion]
    )


if __name__ == "__main__":
    main()

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(35)
    plt.bar(etiquetas, valores, color=["#3498db", "#2ecc71", "#e74c3c", "#f39c12"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.64 — Vida del componente electrónico")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.2f}", ha="center")
    guardar_figura(out, "vida_componente")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.64
Existe interés por la vida de un componente electrónico.
Se sabe que la probabilidad de que funcione más de 6000
horas es 0.42. Además, la probabilidad de que no dure más
de 4000 horas es 0.04.

a) ¿Cuál es la probabilidad de que la vida del componente
   sea menor o igual a 6000 horas?
b) ¿Cuál es la probabilidad de que la vida del componente
   sea mayor que 4000 horas?
=========================================================
"""
    print(enunciado)

    P_mas_6000 = 0.42
    P_menor_igual_4000 = 0.04

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'Menor o igual a 6000' es el complemento de 'más de 6000'.")
    P_menor_igual_6000 = 1 - P_mas_6000
    print(f"-> P(≤ 6000) = 1 − P(> 6000) = 1 − {P_mas_6000} = {P_menor_igual_6000}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Mayor que 4000' es el complemento de 'no mayor que 4000' (≤ 4000).")
    P_mayor_4000 = 1 - P_menor_igual_4000
    print(f"-> P(> 4000) = 1 − P(≤ 4000) = 1 − {P_menor_igual_4000} = {P_mayor_4000}")

    crear_graficas(
        ["P(> 6000)", "P(≤ 6000)", "P(≤ 4000)", "P(> 4000)"],
        [P_mas_6000, P_menor_igual_6000, P_menor_igual_4000, P_mayor_4000]
    )


if __name__ == "__main__":
    main()

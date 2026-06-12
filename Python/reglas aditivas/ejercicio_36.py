import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(36)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db", "#f39c12", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.65 — Falla y deformación del componente")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.2f}", ha="center")
    guardar_figura(out, "falla_deformacion")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.65
Considere la situación del ejercicio 2.64. Sea A el evento
de que el componente falle en una prueba específica y B
el evento de que se deforme pero no falle. A ocurre con
probabilidad 0.20 y B ocurre con probabilidad 0.35.

a) ¿Cuál es la probabilidad de que el componente no falle
   en la prueba?
b) ¿Cuál es la probabilidad de que el componente funcione
   perfectamente bien (ni se deforme ni falle)?
c) ¿Cuál es la probabilidad de que el componente falle o
   se deforme en la prueba?
=========================================================
"""
    print(enunciado)

    P_A = 0.20
    P_B = 0.35

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'No falle' es el complemento de A.")
    P_no_A = 1 - P_A
    print(f"-> P(no falla) = 1 − P(A) = 1 − {P_A} = {P_no_A}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: A y B son mutuamente excluyentes (no puede fallar y solo deformarse a la vez).")
    print("'Funcione perfectamente' = no falle Y no se deforme = complemento de (A ∪ B).")
    P_union = P_A + P_B
    P_perfecto = 1 - P_union
    print(f"-> P(A ∪ B) = P(A) + P(B) = {P_A} + {P_B} = {P_union}")
    print(f"-> P(perfecto) = 1 − P(A ∪ B) = 1 − {P_union} = {P_perfecto}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Ya calculamos P(A ∪ B) en el inciso anterior.")
    print(f"-> P(falle o se deforme) = P(A ∪ B) = {P_union}")

    crear_graficas(
        ["P(A) Falla", "P(B) Deforma", "P(No falla)", "P(Perfecto)"],
        [P_A, P_B, P_no_A, P_perfecto]
    )


if __name__ == "__main__":
    main()

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores, total_manos):
    out = carpeta_graficas(30)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.59 — Mano de póquer (5 cartas)")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.0001, f"{v:.6f}", ha="center")
    guardar_figura(out, "mano_poquer")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.59
En una mano de póquer que consta de 5 cartas, encuentre
la probabilidad de tener:

a) 3 ases;
b) 4 cartas de corazones y 1 de tréboles.
=========================================================
"""
    print(enunciado)

    total_cartas = 52
    total_manos = math.comb(total_cartas, 5)
    print(f"-> Total de manos posibles de 5 cartas: C(52, 5) = {total_manos:,}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Para tener exactamente 3 ases, elegimos 3 de los 4 ases y 2 cartas de las 48 restantes (no ases).")
    formas_ases = math.comb(4, 3)
    formas_resto = math.comb(48, 2)
    formas_a = formas_ases * formas_resto
    prob_a = formas_a / total_manos
    print(f"-> Formas de elegir 3 ases de 4:       C(4, 3) = {formas_ases}")
    print(f"-> Formas de elegir 2 cartas de 48:     C(48, 2) = {formas_resto}")
    print(f"-> Casos favorables: {formas_ases} × {formas_resto} = {formas_a:,}")
    print(f"-> P(3 ases) = {formas_a:,} / {total_manos:,} = {prob_a:.6f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para tener 4 corazones y 1 trébol, elegimos 4 de los 13 corazones y 1 de los 13 tréboles.")
    formas_corazones = math.comb(13, 4)
    formas_trebol = math.comb(13, 1)
    formas_b = formas_corazones * formas_trebol
    prob_b = formas_b / total_manos
    print(f"-> Formas de elegir 4 corazones de 13:   C(13, 4) = {formas_corazones}")
    print(f"-> Formas de elegir 1 trébol de 13:      C(13, 1) = {formas_trebol}")
    print(f"-> Casos favorables: {formas_corazones} × {formas_trebol} = {formas_b:,}")
    print(f"-> P(4 corazones y 1 trébol) = {formas_b:,} / {total_manos:,} = {prob_b:.6f}")

    crear_graficas(
        ["a) 3 ases", "b) 4 corazones, 1 trébol"],
        [prob_a, prob_b],
        total_manos
    )


if __name__ == "__main__":
    main()

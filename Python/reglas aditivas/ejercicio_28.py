import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(28)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.57 — Letra del alfabeto")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.005, f"{v:.4f}", ha="center")
    guardar_figura(out, "letra_alfabeto")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.57
Si se elige al azar una letra del alfabeto inglés,
encuentre la probabilidad de que la letra:

a) sea una vocal excepto y;
b) esté listada en algún lugar antes de la letra j;
c) esté listada en algún lugar después de la letra g.
=========================================================
"""
    print(enunciado)

    total = 26

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Las vocales del alfabeto inglés son a, e, i, o, u (5 letras). Se excluye 'y'.")
    vocales = 5
    p_vocal = vocales / total
    print(f"-> Vocales (sin y): a, e, i, o, u → {vocales} letras")
    print(f"-> P = {vocales} / {total} = {p_vocal:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Las letras antes de 'j' son: a, b, c, d, e, f, g, h, i.")
    antes_j = 9
    p_antes_j = antes_j / total
    print(f"-> Letras antes de j: a, b, c, d, e, f, g, h, i → {antes_j} letras")
    print(f"-> P = {antes_j} / {total} = {p_antes_j:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Las letras después de 'g' son desde la h hasta la z.")
    despues_g = total - 7
    p_despues_g = despues_g / total
    print(f"-> Letras después de g: h, i, j, ..., z → {despues_g} letras")
    print(f"-> P = {despues_g} / {total} = {p_despues_g:.4f}")

    crear_graficas(
        ["a) Vocal (sin y)", "b) Antes de j", "c) Después de g"],
        [p_vocal, p_antes_j, p_despues_g]
    )


if __name__ == "__main__":
    main()

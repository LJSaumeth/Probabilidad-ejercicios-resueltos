import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(31)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.60 — Selección de 3 libros")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "seleccion_libros")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.60
Si se toman 3 libros al azar, de un librero que contiene
5 novelas, 3 libros de poemas y 1 diccionario, ¿cuál es
la probabilidad de que:

a) se seleccione el diccionario?
b) se seleccionen 2 novelas y 1 libro de poemas?
=========================================================
"""
    print(enunciado)

    total_libros = 5 + 3 + 1
    total_formas = math.comb(total_libros, 3)
    print(f"-> Total de libros: {total_libros}")
    print(f"-> Total de formas de elegir 3 libros: C({total_libros}, 3) = {total_formas}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Para que se seleccione el diccionario, elegimos el diccionario (1 forma) y 2 libros de los 8 restantes.")
    formas_a = math.comb(1, 1) * math.comb(8, 2)
    prob_a = formas_a / total_formas
    print(f"-> Formas de elegir el diccionario:         C(1, 1) = 1")
    print(f"-> Formas de elegir 2 libros de los 8 restantes: C(8, 2) = {math.comb(8, 2)}")
    print(f"-> Casos favorables: 1 × {math.comb(8, 2)} = {formas_a}")
    print(f"-> P(diccionario) = {formas_a} / {total_formas} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Elegimos 2 novelas de 5, 1 poema de 3 y 0 diccionarios.")
    formas_b = math.comb(5, 2) * math.comb(3, 1)
    prob_b = formas_b / total_formas
    print(f"-> Formas de elegir 2 novelas de 5:  C(5, 2) = {math.comb(5, 2)}")
    print(f"-> Formas de elegir 1 poema de 3:    C(3, 1) = {math.comb(3, 1)}")
    print(f"-> Casos favorables: {math.comb(5, 2)} × {math.comb(3, 1)} = {formas_b}")
    print(f"-> P(2 novelas y 1 poema) = {formas_b} / {total_formas} = {prob_b:.4f}")

    crear_graficas(
        ["a) Diccionario", "b) 2 novelas, 1 poema"],
        [prob_a, prob_b]
    )


if __name__ == "__main__":
    main()

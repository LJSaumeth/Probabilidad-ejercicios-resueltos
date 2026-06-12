import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(selecciones):
    out = carpeta_graficas(79)
    plt.bar(["Selecciones de 9 manzanas (3 de cada color)"], [selecciones], color="#2ecc71")
    plt.ylabel("Número de formas")
    plt.title("Ejercicio 2.112 — Selección de manzanas")
    plt.text(0, selecciones / 2, f"{selecciones:,}", ha="center", fontsize=14)
    guardar_figura(out, "seleccion_manzanas")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.112
Si se tienen 4 manzanas rojas, 5 verdes y 6 amarillas,
¿cuántas selecciones de 9 manzanas se pueden hacer si se
deben seleccionar 3 de cada color?
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN (Combinatoria) ---")
    print("Se eligen 3 rojas de 4, 3 verdes de 5 y 3 amarillas de 6.")
    print()

    c1 = math.comb(4, 3)
    c2 = math.comb(5, 3)
    c3 = math.comb(6, 3)

    print(f"  C(4, 3) = {c1}")
    print(f"  C(5, 3) = {c2}")
    print(f"  C(6, 3) = {c3}")
    print()

    total = c1 * c2 * c3
    print(f"  Total = {c1} × {c2} × {c3} = {total:,} selecciones")

    crear_graficas(total)


if __name__ == "__main__":
    main()

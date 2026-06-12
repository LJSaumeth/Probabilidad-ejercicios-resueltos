import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(combinaciones, combinaciones_por_aceite):
    out = carpeta_graficas(83)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.bar(["Total combinaciones"], [combinaciones], color="#3498db")
    ax1.text(0, combinaciones / 2, str(combinaciones), ha="center", fontsize=14)
    ax1.set_title("a) Total de combinaciones")
    ax2.bar(["Por tipo de aceite"], [combinaciones_por_aceite], color="#e74c3c")
    ax2.text(0, combinaciones_por_aceite / 2, str(combinaciones_por_aceite), ha="center", fontsize=14)
    ax2.set_title("b) Combinaciones por aceite")
    plt.suptitle("Ejercicio 2.116 — Papas fritas")
    guardar_figura(out, "papas_fritas")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.116
Un fabricante estudia efectos de temperatura (3 niveles),
tiempo de cocción (4 niveles) y tipo de aceite (3 tipos)
al elaborar papas fritas.

a) ¿Número total de combinaciones a estudiar?
b) ¿Cuántas combinaciones para cada tipo de aceite?
c) ¿Por qué las permutaciones no intervienen aquí?
=========================================================
"""
    print(enunciado)

    temp = 3
    tiempo = 4
    aceite = 3

    print("--- SOLUCIÓN a) ---")
    print("Principio fundamental de conteo: multiplicamos las opciones.")
    comb = temp * tiempo * aceite
    print(f"  Total = {temp} × {tiempo} × {aceite} = {comb} combinaciones")
    print()

    print("--- SOLUCIÓN b) ---")
    print("Fijando el tipo de aceite, variamos temperatura y tiempo.")
    comb_por_aceite = temp * tiempo
    print(f"  Por aceite = {temp} × {tiempo} = {comb_por_aceite} combinaciones")
    print()

    print("--- SOLUCIÓN c) ---")
    print("Las permutaciones no aplican porque no estamos ordenando elementos.")
    print("Simplemente elegimos UN nivel de cada factor. Cada combinación es una")
    print("selección única de (temperatura, tiempo, aceite), no un reordenamiento.")

    crear_graficas(comb, comb_por_aceite)


if __name__ == "__main__":
    main()

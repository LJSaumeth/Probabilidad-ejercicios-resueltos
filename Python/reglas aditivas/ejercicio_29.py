import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import itertools
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(distribucion):
    out = carpeta_graficas(29)
    sumas = sorted(distribucion.keys())
    frecuencias = [distribucion[s] for s in sumas]
    etiquetas = [str(s) for s in sumas]
    colores = ["#e74c3c" if s == 8 else "#f39c12" if s <= 5 else "#3498db" for s in sumas]
    plt.bar(etiquetas, frecuencias, color=colores)
    plt.ylabel("Número de resultados")
    plt.xlabel("Suma de los dados")
    plt.title("Ejercicio 2.58 — Distribución de sumas (2 dados)")
    guardar_figura(out, "suma_dados")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.58
Se lanza un par de dados. Calcule la probabilidad de
obtener:

a) un total de 8;
b) máximo un total de 5.
=========================================================
"""
    print(enunciado)

    dados = list(range(1, 7))
    espacio = list(itertools.product(dados, repeat=2))
    total = len(espacio)

    distribucion = {}
    for d1, d2 in espacio:
        s = d1 + d2
        distribucion[s] = distribucion.get(s, 0) + 1

    print("--- SOLUCIÓN a) ---")
    print("Explicación: De los 36 resultados equiprobables, contamos aquellos que suman 8.")
    suma_8 = distribucion[8]
    p_8 = suma_8 / total
    resultados_8 = [(d1, d2) for d1, d2 in espacio if d1 + d2 == 8]
    print(f"-> Resultados que suman 8: {resultados_8}")
    print(f"-> Casos favorables: {suma_8}")
    print(f"-> P(suma 8) = {suma_8} / {total} = {p_8:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Máximo un total de 5' significa suma ≤ 5 (es decir, suma 2, 3, 4 o 5).")
    suma_max_5 = sum(distribucion[s] for s in [2, 3, 4, 5])
    p_max_5 = suma_max_5 / total
    for s in [2, 3, 4, 5]:
        resultados = [(d1, d2) for d1, d2 in espacio if d1 + d2 == s]
        print(f"-> Suma {s}: {resultados} ({distribucion[s]} casos)")
    print(f"-> Total casos favorables: {suma_max_5}")
    print(f"-> P(suma ≤ 5) = {suma_max_5} / {total} = {p_max_5:.4f}")

    crear_graficas(distribucion)


if __name__ == "__main__":
    main()

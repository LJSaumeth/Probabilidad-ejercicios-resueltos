import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(post1, post2):
    out = carpeta_graficas(88)
    plt.bar(["P(Ingeniero 1 | error)", "P(Ingeniero 2 | error)"],
            [post1, post2], color=["#3498db", "#e74c3c"])
    plt.ylabel("Probabilidad a posteriori")
    plt.title("Ejercicio 2.121 — Ingenieros de ventas")
    for i, v in enumerate([post1, post2]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "ingenieros_ventas")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.121
Una empresa emplea dos ingenieros de ventas. El ingeniero
1 estima costos en 70% de las cotizaciones, el ingeniero
2 en 30%. La tasa de error del ingeniero 1 es 0.02 y la
del ingeniero 2 es 0.04. Al revisar una cotización se
encuentra un error grave. ¿Qué ingeniero supone usted que
hizo los cálculos? Explique.
=========================================================
"""
    print(enunciado)

    P_I1 = 0.70
    P_I2 = 0.30
    P_E_dado_I1 = 0.02
    P_E_dado_I2 = 0.04

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print()

    print("Paso 1: P(Error) por probabilidad total.")
    P_E = P_I1 * P_E_dado_I1 + P_I2 * P_E_dado_I2
    c1 = P_I1 * P_E_dado_I1
    c2 = P_I2 * P_E_dado_I2
    print(f"  Ingeniero 1: {P_I1} × {P_E_dado_I1} = {c1:.4f}")
    print(f"  Ingeniero 2: {P_I2} × {P_E_dado_I2} = {c2:.4f}")
    print(f"  → P(Error) = {P_E:.4f}")
    print()

    print("Paso 2: Bayes para cada ingeniero.")
    post1 = c1 / P_E
    post2 = c2 / P_E
    print(f"  P(Ingeniero 1 | Error) = {c1:.4f} / {P_E:.4f} = {post1:.4f}")
    print(f"  P(Ingeniero 2 | Error) = {c2:.4f} / {P_E:.4f} = {post2:.4f}")
    print()

    print("Conclusión: Aunque el ingeniero 2 tiene el DOBLE de tasa de error (4% vs")
    print(f"2%), el ingeniero 1 hace muchos más trabajos (70% vs 30%). La probabilidad")
    print(f"a posteriori de que el error sea del ingeniero 1 es {post1:.4f} ({post1*100:.1f}%).")
    print(f"Lo más probable es que el error sea del ingeniero 1.")

    crear_graficas(post1, post2)


if __name__ == "__main__":
    main()

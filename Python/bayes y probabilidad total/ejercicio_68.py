import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(P_latex_dado_rodillo):
    out = carpeta_graficas(68)
    plt.bar(["P(Látex | Compra rodillo)"], [P_latex_dado_rodillo], color="#9b59b6")
    plt.ylabel("Probabilidad a posteriori")
    plt.title("Ejercicio 2.101 — Tienda de pintura")
    plt.text(0, P_latex_dado_rodillo / 2, f"{P_latex_dado_rodillo:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "tienda_pintura")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.101
Una cadena de tiendas produce pintura de látex y
semiesmaltada. P(comprar látex) = 0.75. De los que compran
látex, 60% también compra rodillos. De los que compran
semiesmaltada, solo 30% compra rodillos. Un comprador
seleccionado al azar adquiere un rodillo y una lata de
pintura. ¿Cuál es la probabilidad de que sea látex?
=========================================================
"""
    print(enunciado)

    P_L = 0.75                  # P(látex)
    P_S = 1 - P_L               # P(semiesmaltada)
    P_R_dado_L = 0.60           # P(rodillo | látex)
    P_R_dado_S = 0.30           # P(rodillo | semiesmaltada)

    print("--- PRELIMINAR ---")
    print(f"  P(Semiesmaltada) = 1 − {P_L} = {P_S}")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Queremos: P(Látex | Rodillo)")
    print()

    print("Paso 1: P(Rodillo) por probabilidad total.")
    P_R = P_L * P_R_dado_L + P_S * P_R_dado_S
    print(f"  Rama látex:       {P_L} × {P_R_dado_L} = {P_L * P_R_dado_L:.4f}")
    print(f"  Rama semiesmaltada: {P_S} × {P_R_dado_S} = {P_S * P_R_dado_S:.4f}")
    print(f"  → P(Rodillo) = {P_L * P_R_dado_L:.4f} + {P_S * P_R_dado_S:.4f} = {P_R:.4f}")
    print()

    print("Paso 2: Teorema de Bayes.")
    num = P_L * P_R_dado_L
    prob = num / P_R
    print(f"                P(R|L) × P(L)     {P_R_dado_L} × {P_L}     {num:.4f}")
    print(f"  P(L | R) = ──────────────── = ───────────── = ─────── = {prob:.4f}")
    print(f"                    P(R)              {P_R:.4f}        {P_R:.4f}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

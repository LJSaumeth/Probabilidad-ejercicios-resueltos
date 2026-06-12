import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(55)
    plt.bar(["P(En casa y compra)"], [prob], color="#2ecc71")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.84 — Venta por teléfono")
    plt.text(0, prob / 2, f"{prob:.2f}", ha="center", fontsize=14, fontweight="bold")
    guardar_figura(out, "venta_telefono")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.84
La probabilidad de que el jefe de familia esté en casa
cuando llame el representante de marketing es 0.4. Dado
que el jefe está en casa, la probabilidad de que se le
venda un producto es 0.3. Encuentre la probabilidad de que
el jefe esté en casa y compre productos.
=========================================================
"""
    print(enunciado)

    P_casa = 0.4
    P_compra_dado_casa = 0.3

    print("--- SOLUCIÓN ---")
    print("Explicación: Usamos la regla de la multiplicación:")
    print("P(En casa ∩ Compra) = P(En casa) × P(Compra | En casa)")
    prob = P_casa * P_compra_dado_casa
    print(f"-> P = {P_casa} × {P_compra_dado_casa} = {prob}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

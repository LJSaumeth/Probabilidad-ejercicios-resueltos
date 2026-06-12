import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(25)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db", "#f39c12", "#9b59b6", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.54 — Inversiones del cliente")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.2f}", ha="center")
    guardar_figura(out, "inversiones_cliente")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.54
Basado en su experiencia, un agente bursátil considera que
la probabilidad de que un cliente invierta en bonos libres
de impuestos es 0.6, en fondos comunes de inversión es 0.3
y en ambos es 0.15.

Encuentre la probabilidad de que un cliente invierta:

a) en bonos libres de impuestos o en fondos comunes;
b) en ninguno de esos dos instrumentos.
=========================================================
"""
    print(enunciado)

    P_B = 0.6
    P_F = 0.3
    P_B_int_F = 0.15

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Usamos la regla aditiva de probabilidad:")
    print("P(B ∪ F) = P(B) + P(F) − P(B ∩ F)")
    P_union = P_B + P_F - P_B_int_F
    print(f"-> P(B ∪ F) = {P_B} + {P_F} − {P_B_int_F} = {P_union}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'En ninguno' es el complemento de la unión:")
    print("P(ninguno) = 1 − P(B ∪ F)")
    P_ninguno = 1 - P_union
    print(f"-> P(ninguno) = 1 − {P_union} = {P_ninguno}")

    crear_graficas(
        ["P(Bonos)", "P(Fondos)", "P(B ∩ F)", "P(B ∪ F)", "P(Ninguno)"],
        [P_B, P_F, P_B_int_F, P_union, P_ninguno]
    )


if __name__ == "__main__":
    main()

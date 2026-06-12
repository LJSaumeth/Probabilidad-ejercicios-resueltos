import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(91)
    plt.bar(["P(Asistió al curso | Cumple cuota)"], [prob], color="#2ecc71")
    plt.ylabel("Probabilidad a posteriori")
    plt.title("Ejercicio 2.124 — Capacitación de operadores")
    plt.text(0, prob / 2, f"{prob:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "capacitacion_operadores")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.124
Una empresa capacita operadores. Los que asisten al curso
cumplen sus cuotas 90% de las veces. Los que no asisten
cumplen 65% de las veces. 50% de los nuevos operadores
asisten al curso. Dado que un nuevo operador cumple su
cuota, ¿cuál es la probabilidad de que haya asistido al
curso?
=========================================================
"""
    print(enunciado)

    P_A = 0.50                  # P(asiste al curso)
    P_noA = 1 - P_A
    P_C_dado_A = 0.90           # P(cumple | asiste)
    P_C_dado_noA = 0.65         # P(cumple | no asiste)

    print("--- PRELIMINAR ---")
    print(f"  P(No asiste) = 1 − {P_A} = {P_noA}")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print()

    print("Paso 1: P(Cumple) por probabilidad total.")
    P_C = P_A * P_C_dado_A + P_noA * P_C_dado_noA
    c1 = P_A * P_C_dado_A
    c2 = P_noA * P_C_dado_noA
    print(f"  Rama asiste:    {P_A} × {P_C_dado_A} = {c1:.4f}")
    print(f"  Rama no asiste: {P_noA} × {P_C_dado_noA} = {c2:.4f}")
    print(f"  → P(Cumple) = {P_C:.4f}")
    print()

    print("Paso 2: Bayes para P(Asiste | Cumple).")
    prob = c1 / P_C
    print(f"                       P(C|A) × P(A)     {P_C_dado_A} × {P_A}     {c1:.4f}")
    print(f"  P(Asiste | Cumple) = ────────────── = ───────────── = ─────── = {prob:.4f}")
    print(f"                           P(C)            {P_C:.4f}        {P_C:.4f}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

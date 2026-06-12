import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(85)
    plt.bar(["P(Cáncer | Resultado negativo)"], [prob], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.118 — Cáncer y prueba de sangre")
    plt.text(0, prob / 2, f"{prob:.6f}", ha="center", fontsize=14)
    guardar_figura(out, "cancer_prueba_sangre")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.118
Hay probabilidad de 0.07 de que mujeres de más de 60 años
desarrollen cierta forma de cáncer. Existe una prueba de
sangre: 10% de falso negativo (la prueba dice negativo
cuando sí hay cáncer) y 5% de falso positivo (prueba dice
positivo cuando no hay cáncer). Si una mujer de más de 60
años recibe un resultado NEGATIVO, ¿qué probabilidad hay
de que tenga la enfermedad?
=========================================================
"""
    print(enunciado)

    P_C = 0.07                  # P(cáncer a priori)
    P_noC = 1 - P_C
    # P(negativo | cáncer) = tasa de falso negativo
    P_N_dado_C = 0.10           # falso negativo
    # P(positivo | no cáncer) = tasa de falso positivo = 0.05
    # Por tanto P(negativo | no cáncer) = 1 − 0.05 = 0.95 (especificidad)
    P_N_dado_noC = 1 - 0.05

    print("--- PRELIMINAR: valores derivados ---")
    print(f"  P(No cáncer) = 1 − {P_C} = {P_noC}")
    print(f"  P(Negativo | Cáncer) = {P_N_dado_C}  (falso negativo, enunciado)")
    print(f"  P(Negativo | No cáncer) = 1 − 0.05 = {P_N_dado_noC}  (especificidad)")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Se pide: P(Cáncer | Resultado negativo).")
    print()

    print("Paso 1: P(Negativo) por probabilidad total.")
    P_N = P_C * P_N_dado_C + P_noC * P_N_dado_noC
    print(f"  Rama cáncer:    {P_C} × {P_N_dado_C} = {P_C * P_N_dado_C:.4f}")
    print(f"  Rama no cáncer: {P_noC} × {P_N_dado_noC} = {P_noC * P_N_dado_noC:.4f}")
    print(f"  → P(Negativo) = {P_N:.4f}")
    print()

    print("Paso 2: Bayes.")
    num = P_C * P_N_dado_C
    prob = num / P_N
    print(f"                          P(N|C) × P(C)     {P_N_dado_C} × {P_C}     {num:.4f}")
    print(f"  P(Cáncer | Negativo) = ────────────── = ───────────── = ─────── = {prob:.6f}")
    print(f"                              P(N)            {P_N:.4f}       {P_N:.4f}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

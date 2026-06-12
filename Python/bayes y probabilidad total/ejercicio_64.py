import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(P_C_dado_D):
    out = carpeta_graficas(64)
    plt.bar(["P(Cáncer | Diagnóstico)"], [P_C_dado_D], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.97 — Teorema de Bayes")
    plt.text(0, P_C_dado_D / 2, f"{P_C_dado_D:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "bayes_cancer")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.97
Remítase al ejercicio 2.95. ¿Cuál es la probabilidad de
que una persona a la que se le diagnostica cáncer
realmente tenga la enfermedad?
=========================================================
"""
    print(enunciado)

    # Datos del 2.95
    P_C = 0.05
    P_D_dado_C = 0.78
    P_D_dado_noC = 0.06
    P_noC = 1 - P_C
    P_D = P_C * P_D_dado_C + P_noC * P_D_dado_noC

    print("--- Datos del ejercicio 2.95 ---")
    print(f"  P(Cáncer) = {P_C}")
    print(f"  P(Diagnóstico | Cáncer) = {P_D_dado_C}")
    print(f"  P(Diagnóstico | No cáncer) = {P_D_dado_noC}")
    print(f"  P(Diagnóstico) = {P_D:.4f}  (calculado en 2.95)")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Se nos pide P(Cáncer | Diagnóstico), es decir, la probabilidad")
    print("a posteriori de tener cáncer dado un diagnóstico positivo.")
    print()
    print("              P(D|C) × P(C)")
    print("  P(C|D) = ───────────────────")
    print("                  P(D)")
    print()
    print(f"            {P_D_dado_C} × {P_C}       {P_D_dado_C * P_C:.4f}")
    print(f"  P(C|D) = ─────────────── = ─────── = {P_C_dado_D:.4f}")
    print(f"                {P_D:.4f}        {P_D:.4f}")
    print()
    P_C_dado_D = (P_D_dado_C * P_C) / P_D
    print(f"Una persona diagnosticada con cáncer tiene solo {P_C_dado_D*100:.1f}% de")
    print("probabilidad de tener realmente la enfermedad, debido a la baja")
    print("prevalencia de la enfermedad en la población (5%).")

    crear_graficas(P_C_dado_D)


if __name__ == "__main__":
    main()

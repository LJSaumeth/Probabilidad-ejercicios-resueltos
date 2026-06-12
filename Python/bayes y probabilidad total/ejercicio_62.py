import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(P_cancer, P_diag, P_no_cancer, P_falso_pos, P_diag_total):
    out = carpeta_graficas(62)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.bar(["P(Cáncer)"], [P_cancer], color="#e74c3c")
    ax1.bar(["P(No cáncer)"], [P_no_cancer], color="#3498db")
    ax1.set_title("Probabilidades a priori")

    ax2.bar(["P(Diagnosticar cáncer)"], [P_diag_total], color="#2ecc71")
    ax2.set_title("Probabilidad total (resultado)")
    ax2.text(0, P_diag_total / 2, f"{P_diag_total:.4f}", ha="center", fontsize=14)

    plt.suptitle("Ejercicio 2.95 — Diagnóstico de cáncer")
    guardar_figura(out, "diagnostico_cancer")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.95
En cierta región, la probabilidad de seleccionar un adulto
mayor de 40 años con cáncer es 0.05. La probabilidad de
que un doctor diagnostique correctamente que una persona
con cáncer tiene la enfermedad es 0.78, y la probabilidad
de que diagnostique incorrectamente que una persona sin
cáncer tiene la enfermedad es 0.06.

¿Cuál es la probabilidad de que a un adulto mayor de 40
años se le diagnostique cáncer?
=========================================================
"""
    print(enunciado)

    # Datos del enunciado
    P_C = 0.05          # Probabilidad de tener cáncer (a priori)
    P_D_dado_C = 0.78   # P(diagnosticar cáncer | tiene cáncer)
    P_D_dado_noC = 0.06 # P(diagnosticar cáncer | NO tiene cáncer)

    print("--- PRELIMINAR: valores derivados ---")
    P_noC = 1 - P_C
    print(f"  P(No cáncer) = 1 − P(Cáncer) = 1 − {P_C} = {P_noC}")
    print()

    print("--- SOLUCIÓN (Probabilidad total) ---")
    print("Explicación: Usamos la ley de probabilidad total. Una persona puede ser")
    print("diagnosticada con cáncer si realmente lo tiene (y el diagnóstico es")
    print("correcto) O si no lo tiene (y el diagnóstico es un falso positivo).")
    print()
    print("  P(D) = P(C) × P(D|C) + P(C') × P(D|C')")
    print()
    print(f"  Rama 1 (sí tiene cáncer):")
    print(f"    P(C) × P(D|C) = {P_C} × {P_D_dado_C} = {P_C * P_D_dado_C:.4f}")
    print()
    print(f"  Rama 2 (no tiene cáncer):")
    print(f"    P(C') × P(D|C') = {P_noC} × {P_D_dado_noC} = {P_noC * P_D_dado_noC:.4f}")
    print()
    P_D = P_C * P_D_dado_C + P_noC * P_D_dado_noC
    print(f"  → P(Diagnosticar cáncer) = {P_C * P_D_dado_C:.4f} + {P_noC * P_D_dado_noC:.4f}")
    print(f"                           = {P_D:.4f}")

    crear_graficas(P_C, P_D_dado_C, P_noC, P_D_dado_noC, P_D)


if __name__ == "__main__":
    main()

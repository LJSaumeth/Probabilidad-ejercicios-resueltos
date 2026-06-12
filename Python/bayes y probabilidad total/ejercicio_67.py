import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(totales, prob_C_dado_humano):
    out = carpeta_graficas(67)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.bar(["A", "B", "C"], totales, color=["#3498db", "#e74c3c", "#2ecc71"])
    ax1.set_title("Total de fallas por estación")
    ax2.bar(["P(C | error humano)"], [prob_C_dado_humano], color="#f39c12")
    ax2.set_title("Probabilidad a posteriori")
    ax2.text(0, prob_C_dado_humano / 2, f"{prob_C_dado_humano:.4f}", ha="center", fontsize=14)
    plt.suptitle("Ejercicio 2.100 — Estaciones de retransmisión")
    guardar_figura(out, "estaciones_retransmision")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.100
Una empresa telefónica opera tres estaciones de
retransmisión. Fallas reportadas en un año:

| Problema             | A | B | C |
|----------------------|---|---|---|
| Electricidad         | 2 | 1 | 1 |
| Computadora          | 4 | 3 | 2 |
| Errores humanos      | 5 | 4 | 2 |
| Otros                | 7 | 5 | 5 |

Si se reporta una falla y fue ocasionada por errores
humanos, ¿cuál es la probabilidad de que provenga de C?
=========================================================
"""
    print(enunciado)

    total_A = 2 + 4 + 5 + 7
    total_B = 1 + 3 + 4 + 5
    total_C = 1 + 2 + 2 + 5
    total_general = total_A + total_B + total_C

    print("--- PRELIMINAR: totales por estación ---")
    print(f"  Estación A: 2+4+5+7 = {total_A}")
    print(f"  Estación B: 1+3+4+5 = {total_B}")
    print(f"  Estación C: 1+2+2+5 = {total_C}")
    print(f"  Total general: {total_general}")
    print()

    P_A = total_A / total_general
    P_B = total_B / total_general
    P_C = total_C / total_general

    P_hum_dado_A = 5 / total_A
    P_hum_dado_B = 4 / total_B
    P_hum_dado_C = 2 / total_C

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("P(C | error humano) = P(error humano | C) × P(C) / P(error humano)")
    print()

    print("Paso 1: probabilidades a priori de cada estación.")
    print(f"  P(A) = {total_A}/{total_general} = {P_A:.4f}")
    print(f"  P(B) = {total_B}/{total_general} = {P_B:.4f}")
    print(f"  P(C) = {total_C}/{total_general} = {P_C:.4f}")
    print()

    print("Paso 2: probabilidad de error humano dada cada estación.")
    print(f"  P(Hum | A) = 5/{total_A} = {P_hum_dado_A:.4f}")
    print(f"  P(Hum | B) = 4/{total_B} = {P_hum_dado_B:.4f}")
    print(f"  P(Hum | C) = 2/{total_C} = {P_hum_dado_C:.4f}")
    print()

    print("Paso 3: probabilidad total de error humano.")
    P_hum = P_A * P_hum_dado_A + P_B * P_hum_dado_B + P_C * P_hum_dado_C
    print(f"  P(Hum) = {P_A:.4f}×{P_hum_dado_A:.4f} + {P_B:.4f}×{P_hum_dado_B:.4f} + {P_C:.4f}×{P_hum_dado_C:.4f}")
    print(f"         = {P_hum:.4f}")
    print()

    print("Paso 4: Teorema de Bayes para P(C | Hum).")
    num = P_C * P_hum_dado_C
    prob = num / P_hum
    print(f"  P(C | Hum) = ({P_C:.4f} × {P_hum_dado_C:.4f}) / {P_hum:.4f}")
    print(f"             = {num:.4f} / {P_hum:.4f} = {prob:.4f}")

    crear_graficas([total_A, total_B, total_C], prob)


if __name__ == "__main__":
    main()

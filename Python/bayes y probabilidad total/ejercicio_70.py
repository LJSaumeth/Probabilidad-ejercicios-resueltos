import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(P_inocente_dado_culpable):
    out = carpeta_graficas(70)
    plt.bar(["P(Inocente | Suero dice culpable)"], [P_inocente_dado_culpable], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.103 — Suero de la verdad")
    plt.text(0, P_inocente_dado_culpable / 2, f"{P_inocente_dado_culpable:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "suero_verdad")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.103
Un suero de la verdad: 90% de los culpables se juzgan
correctamente (10% se consideran inocentes). Los inocentes
se juzgan mal 1% de las veces. Se selecciona un sospechoso
de un grupo donde solo 5% ha cometido un delito. Si el
suero indica culpable, ¿cuál es la probabilidad de que sea
inocente?
=========================================================
"""
    print(enunciado)

    P_C = 0.05                  # P(culpable a priori)
    P_I = 1 - P_C               # P(inocente a priori)
    P_pos_dado_C = 0.90         # P(suero dice culpable | es culpable)
    P_pos_dado_I = 0.01         # P(suero dice culpable | es inocente) [falso positivo]

    print("--- PRELIMINAR ---")
    print(f"  P(Inocente) = 1 − {P_C} = {P_I}")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Se pide P(Inocente | Suero dice culpable).")
    print()

    print("Paso 1: P(Suero dice culpable) por probabilidad total.")
    P_pos = P_C * P_pos_dado_C + P_I * P_pos_dado_I
    print(f"  Rama culpable:   {P_C} × {P_pos_dado_C} = {P_C * P_pos_dado_C:.4f}")
    print(f"  Rama inocente:   {P_I} × {P_pos_dado_I} = {P_I * P_pos_dado_I:.4f}")
    print(f"  → P(dice culpable) = {P_pos:.4f}")
    print()

    print("Paso 2: Bayes para P(Inocente | dice culpable).")
    num = P_I * P_pos_dado_I
    prob = num / P_pos
    print(f"                                  P(+|I) × P(I)")
    print(f"  P(Inocente | +) = ─────────────────────────────")
    print(f"                              P(+)")
    print(f"                     {P_pos_dado_I} × {P_I}     {num:.4f}")
    print(f"                   = ───────────── = ─────── = {prob:.4f}")
    print(f"                         {P_pos:.4f}      {P_pos:.4f}")
    print()
    print(f"A pesar de la alta precisión del suero, hay {prob*100:.1f}% de probabilidad")
    print("de que un resultado 'culpable' corresponda a un inocente, debido a")
    print("la bajísima prevalencia de culpables (5%).")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

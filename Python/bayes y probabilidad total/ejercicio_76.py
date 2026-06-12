import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(P_falla, P_lake_dado_falla):
    out = carpeta_graficas(76)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.bar(["P(falla plomería)"], [P_falla], color="#e74c3c")
    ax1.set_title("Probabilidad total")
    ax1.text(0, P_falla / 2, f"{P_falla:.4f}", ha="center", fontsize=14)
    ax2.bar(["P(Lakeview | falla)"], [P_lake_dado_falla], color="#3498db")
    ax2.set_title("Probabilidad a posteriori")
    ax2.text(0, P_lake_dado_falla / 2, f"{P_lake_dado_falla:.4f}", ha="center", fontsize=14)
    plt.suptitle("Ejercicio 2.109 — Moteles y plomería")
    guardar_figura(out, "moteles_plomeria")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.109
Una empresa usa tres moteles: Ramada Inn (20% de clientes),
Sheraton (50%) y Lakeview (30%). Fallas de plomería: 5%
en Ramada, 4% en Sheraton, 8% en Lakeview.

a) ¿Probabilidad de que a un cliente se le asigne una
   habitación con falla de plomería?
b) ¿Probabilidad de que una persona con falla de plomería
   esté en Lakeview?
=========================================================
"""
    print(enunciado)

    P_R = 0.20
    P_S = 0.50
    P_L = 0.30
    P_F_dado_R = 0.05
    P_F_dado_S = 0.04
    P_F_dado_L = 0.08

    print("--- SOLUCIÓN a) Probabilidad total ---")
    print("P(F) = P(R)×P(F|R) + P(S)×P(F|S) + P(L)×P(F|L)")
    print()
    contrib_R = P_R * P_F_dado_R
    contrib_S = P_S * P_F_dado_S
    contrib_L = P_L * P_F_dado_L
    print(f"  Ramada:   {P_R} × {P_F_dado_R} = {contrib_R:.4f}")
    print(f"  Sheraton: {P_S} × {P_F_dado_S} = {contrib_S:.4f}")
    print(f"  Lakeview: {P_L} × {P_F_dado_L} = {contrib_L:.4f}")
    P_F = contrib_R + contrib_S + contrib_L
    print(f"  → P(falla) = {P_F:.4f}")
    print()

    print("--- SOLUCIÓN b) Teorema de Bayes ---")
    prob_b = contrib_L / P_F
    print(f"                       P(L) × P(F|L)     {contrib_L:.4f}")
    print(f"  P(Lakeview | falla) = ───────────── = ─────── = {prob_b:.4f}")
    print(f"                           P(F)           {P_F:.4f}")

    crear_graficas(P_F, prob_b)


if __name__ == "__main__":
    main()

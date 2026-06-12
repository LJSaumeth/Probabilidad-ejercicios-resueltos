import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_post):
    out = carpeta_graficas(94)
    plt.bar(["P(Portadora | 3 hijos sanos)"], [prob_post], color="#9b59b6")
    plt.ylabel("Probabilidad a posteriori")
    plt.title("Ejercicio 2.127 — Gen de la hemofilia")
    plt.text(0, prob_post / 2, f"{prob_post:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "hemofilia_reina")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.127
Hay 50% de probabilidad de que la reina tenga el gen de
la hemofilia. Si es portadora, cada príncipe tiene 50% de
probabilidad independiente de tener hemofilia. Si no es
portadora, el príncipe no tendrá la enfermedad. La reina
tuvo 3 príncipes, todos sanos. ¿Cuál es la probabilidad
de que la reina sea portadora?
=========================================================
"""
    print(enunciado)

    P_port = 0.50                     # P(portadora a priori)
    P_noPort = 1 - P_port

    print("--- PRELIMINAR: verosimilitudes ---")
    print("Si es portadora: cada hijo tiene P(sano) = 1 − 0.5 = 0.5.")
    P_3sanos_dado_port = 0.5 ** 3
    print(f"  P(3 sanos | portadora) = (0.5)³ = {P_3sanos_dado_port:.4f}")
    print()
    print("Si NO es portadora: cada hijo tiene P(sano) = 1.")
    P_3sanos_dado_noPort = 1.0
    print(f"  P(3 sanos | no portadora) = 1³ = {P_3sanos_dado_noPort}")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print()

    print("Paso 1: P(3 hijos sanos) por probabilidad total.")
    P_3sanos = P_port * P_3sanos_dado_port + P_noPort * P_3sanos_dado_noPort
    c1 = P_port * P_3sanos_dado_port
    c2 = P_noPort * P_3sanos_dado_noPort
    print(f"  Rama portadora:     {P_port} × {P_3sanos_dado_port:.4f} = {c1:.4f}")
    print(f"  Rama no portadora:  {P_noPort} × {P_3sanos_dado_noPort} = {c2:.4f}")
    print(f"  → P(3 sanos) = {P_3sanos:.4f}")
    print()

    print("Paso 2: Teorema de Bayes.")
    prob = c1 / P_3sanos
    print(f"                             P(3S|P) × P(P)     {P_3sanos_dado_port} × {P_port}     {c1:.4f}")
    print(f"  P(Portadora | 3 sanos) = ──────────────── = ─────────────── = ─────── = {prob:.4f}")
    print(f"                                 P(3S)              {P_3sanos:.4f}         {P_3sanos:.4f}")
    print()
    print(f"La evidencia (3 hijos sanos) reduce la probabilidad de que la reina sea")
    print(f"portadora de 50% a {prob*100:.1f}%.")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

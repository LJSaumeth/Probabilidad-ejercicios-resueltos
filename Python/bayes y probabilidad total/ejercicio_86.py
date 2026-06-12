import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(probs_post):
    out = carpeta_graficas(86)
    etiquetas = ["0 defectuosos", "1 defectuoso", "2 defectuosos"]
    plt.bar(etiquetas, probs_post, color=["#2ecc71", "#f39c12", "#e74c3c"])
    plt.ylabel("Probabilidad a posteriori")
    plt.title("Ejercicio 2.119 — Componentes electrónicos")
    for i, v in enumerate(probs_post):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "componentes_electronicos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.119
Un fabricante abastece lotes de 20 componentes. 60% de
los lotes no tiene defectuosos, 30% tiene 1 defectuoso,
10% tiene 2 defectuosos. De un lote se extraen 2
componentes al azar y se prueban: ninguno es defectuoso.

a) P(0 defectuosos en el lote | prueba ok)
b) P(1 defectuoso en el lote | prueba ok)
c) P(2 defectuosos en el lote | prueba ok)
=========================================================
"""
    print(enunciado)

    P_D0 = 0.60
    P_D1 = 0.30
    P_D2 = 0.10

    print("--- PRELIMINAR: P(probar 2 sin defecto | cada tipo de lote) ---")
    print("Se extraen 2 sin reemplazo de un lote de 20.")
    print()

    # D0: 0 defectuosos → probar 2 buenos = 1
    P_ok_dado_D0 = 1.0
    print(f"  Lote con 0 defect.: P(2 buenos) = 1")

    # D1: 1 defectuoso, 19 buenos
    P_ok_dado_D1 = math.comb(19, 2) / math.comb(20, 2)
    print(f"  Lote con 1 defect.: P(2 buenos) = C(19,2)/C(20,2) = {P_ok_dado_D1:.4f}")

    # D2: 2 defectuosos, 18 buenos
    P_ok_dado_D2 = math.comb(18, 2) / math.comb(20, 2)
    print(f"  Lote con 2 defect.: P(2 buenos) = C(18,2)/C(20,2) = {P_ok_dado_D2:.4f}")
    print()

    print("--- Paso 1: P(probar 2 sin defecto) por prob. total ---")
    P_ok = P_D0 * P_ok_dado_D0 + P_D1 * P_ok_dado_D1 + P_D2 * P_ok_dado_D2
    print(f"  P(ok) = {P_D0}×1 + {P_D1}×{P_ok_dado_D1:.4f} + {P_D2}×{P_ok_dado_D2:.4f}")
    print(f"        = {P_ok:.6f}")
    print()

    print("--- Paso 2: Bayes para cada caso ---")
    post = []
    priors = [P_D0, P_D1, P_D2]
    verosim = [P_ok_dado_D0, P_ok_dado_D1, P_ok_dado_D2]
    labels = ["0 defect.", "1 defect.", "2 defect."]

    for i in range(3):
        p = (priors[i] * verosim[i]) / P_ok
        post.append(p)
        print(f"  P({labels[i]} | ok) = ({priors[i]} × {verosim[i]:.4f}) / {P_ok:.6f} = {p:.4f}")

    print(f"\n  Verificación (debe sumar 1): {sum(post):.4f}")

    crear_graficas(post)


if __name__ == "__main__":
    main()

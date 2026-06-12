import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b, probs_posteriores):
    out = carpeta_graficas(82)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.bar(["a) P(exceso)", "b) P(sea A | exceso)"], [prob_a, prob_b], color=["#e74c3c", "#3498db"])
    ax1.set_title("Incisos a y b")
    ax2.bar(["A", "B", "C"], probs_posteriores, color=["#3498db", "#f39c12", "#e74c3c"])
    ax2.set_title("P(empresa | exceso)")
    for i, v in enumerate(probs_posteriores):
        ax2.text(i, v + 0.01, f"{v:.4f}", ha="center")
    plt.suptitle("Ejercicio 2.115 — Empresas consultoras")
    guardar_figura(out, "empresas_consultoras")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.115
Un organismo federal emplea 3 empresas consultoras (A, B,
C) con probabilidades 0.40, 0.35 y 0.25. Las probabilidades
de que rebasen costos son 0.05, 0.03 y 0.15. Si el
organismo experimenta un exceso en los costos:

a) ¿Probabilidad de que la empresa implicada sea C?
b) ¿Probabilidad de que sea A?
=========================================================
"""
    print(enunciado)

    P_emp = [0.40, 0.35, 0.25]
    P_exc_dado = [0.05, 0.03, 0.15]
    nombres = ["A", "B", "C"]

    print("--- Paso 1: Probabilidad total de exceso ---")
    P_exc = sum(P_emp[i] * P_exc_dado[i] for i in range(3))
    for i in range(3):
        c = P_emp[i] * P_exc_dado[i]
        print(f"  {nombres[i]}: {P_emp[i]} × {P_exc_dado[i]} = {c:.4f}")
    print(f"  → P(exceso) = {P_exc:.4f}")
    print()

    print("--- Solución a) P(C | exceso) ---")
    prob_C = (P_emp[2] * P_exc_dado[2]) / P_exc
    print(f"  P(C | exceso) = ({P_emp[2]} × {P_exc_dado[2]}) / {P_exc:.4f} = {prob_C:.4f}")
    print()

    print("--- Solución b) P(A | exceso) ---")
    prob_A = (P_emp[0] * P_exc_dado[0]) / P_exc
    print(f"  P(A | exceso) = ({P_emp[0]} × {P_exc_dado[0]}) / {P_exc:.4f} = {prob_A:.4f}")

    post = [(P_emp[i] * P_exc_dado[i]) / P_exc for i in range(3)]
    crear_graficas(P_exc, prob_A, post)


if __name__ == "__main__":
    main()

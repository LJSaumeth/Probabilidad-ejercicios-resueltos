import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(probs_posteriores):
    out = carpeta_graficas(65)
    ubicaciones = ["L1", "L2", "L3", "L4"]
    plt.bar(ubicaciones, probs_posteriores, color=["#3498db", "#e74c3c", "#f39c12", "#2ecc71"])
    plt.ylabel("Probabilidad a posteriori")
    plt.title("Ejercicio 2.98 — ¿Por cuál radar pasó?")
    for i, v in enumerate(probs_posteriores):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "bayes_radares")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.98
Si en el ejercicio 2.96 la persona es multada, ¿cuál es la
probabilidad de que haya pasado por el radar de L2?
=========================================================
"""
    print(enunciado)

    P_opera = [0.40, 0.30, 0.20, 0.30]
    P_pasa = [0.2, 0.1, 0.5, 0.2]

    print("--- Datos del ejercicio 2.96 ---")
    print(f"  P(pasa por Li): {P_pasa}")
    print(f"  P(radar opera en Li): {P_opera}")
    print()

    # Probabilidad total de multa
    P_multa = sum(P_pasa[i] * P_opera[i] for i in range(4))
    print(f"  P(multa) = {P_multa:.4f}  (calculado en 2.96)")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Se pide P(pasó por L2 | fue multado).")
    print()
    print("                P(multa | L2) × P(L2)")
    print("  P(L2 | multa) = ──────────────────────")
    print("                       P(multa)")
    print()

    # P(multa | L2) = P(radar opera en L2) = 0.30
    P_mult_dado_L2 = P_opera[1]
    num = P_pasa[1] * P_mult_dado_L2
    den = P_multa
    prob = num / den

    print(f"  P(multa | L2) = P(radar opera en L2) = {P_mult_dado_L2}")
    print(f"  P(L2) = P(pasa por L2) = {P_pasa[1]}")
    print(f"  Numerador: P(L2) × P(multa|L2) = {P_pasa[1]} × {P_mult_dado_L2} = {num:.4f}")
    print(f"  Denominador: P(multa) = {den:.4f}")
    print(f"  → P(L2 | multa) = {num:.4f} / {den:.4f} = {prob:.4f}")

    # Calcular todas las posteriores para la gráfica
    post = [(P_pasa[i] * P_opera[i]) / P_multa for i in range(4)]
    crear_graficas(post)


if __name__ == "__main__":
    main()

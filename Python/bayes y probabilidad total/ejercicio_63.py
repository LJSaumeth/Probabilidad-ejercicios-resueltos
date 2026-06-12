import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(ubicaciones, P_opera, P_pasa, contribuciones):
    out = carpeta_graficas(63)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.bar(ubicaciones, P_opera, color="#3498db")
    ax1.set_title("P(radar operando)")
    ax1.set_ylabel("Probabilidad")

    ax2.bar(ubicaciones, contribuciones, color="#e74c3c")
    ax2.set_title("Contribución a P(multa)")
    for i, v in enumerate(contribuciones):
        ax2.text(i, v + 0.002, f"{v:.4f}", ha="center")

    plt.suptitle("Ejercicio 2.96 — Radares de velocidad")
    guardar_figura(out, "radares_velocidad")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.96
La policía usa radar en 4 puntos a las orillas de la
ciudad. Las trampas en L1, L2, L3 y L4 operan 40%, 30%,
20% y 30% del tiempo. Una persona que excede el límite
pasa por esos lugares con probabilidades 0.2, 0.1, 0.5
y 0.2, respectivamente. ¿Probabilidad de que reciba una
multa?
=========================================================
"""
    print(enunciado)

    P_opera = [0.40, 0.30, 0.20, 0.30]   # P(radar activo en cada sitio)
    P_pasa = [0.2, 0.1, 0.5, 0.2]        # P(pasar por cada sitio)

    print("--- PRELIMINAR: interpretación ---")
    print("Para ser multado, el conductor debe pasar por un sitio Y el radar estar")
    print("operando en ese momento. Como solo pasa por un sitio, los eventos son")
    print("mutuamente excluyentes respecto a la ruta tomada.")
    print()

    print("--- SOLUCIÓN (Probabilidad total) ---")
    print("P(multa) = Σ P(pasa por Li) × P(radar opera en Li)")
    print()

    P_multa = 0
    for i in range(4):
        contrib = P_pasa[i] * P_opera[i]
        P_multa += contrib
        print(f"  L{i+1}: P(pasa) × P(opera) = {P_pasa[i]} × {P_opera[i]} = {contrib:.4f}")

    print(f"\n  → P(multa) = {P_multa:.4f}")

    crear_graficas(["L1", "L2", "L3", "L4"], P_opera, P_pasa,
                   [P_pasa[i] * P_opera[i] for i in range(4)])


if __name__ == "__main__":
    main()

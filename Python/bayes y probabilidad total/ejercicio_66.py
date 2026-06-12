import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(probs_posteriores, nombres):
    out = carpeta_graficas(66)
    plt.bar(nombres, probs_posteriores, color=["#e74c3c", "#3498db", "#f39c12", "#2ecc71"])
    plt.ylabel("P(inspector | sin fecha)")
    plt.title("Ejercicio 2.99 — Inspectores de película")
    for i, v in enumerate(probs_posteriores):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "inspectores_pelicula")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.99
Cuatro inspectores colocan la fecha de caducidad en
paquetes de película:
- John:  20% de paquetes, falla 1 de cada 200
- Tom:   60% de paquetes, falla 1 de cada 100
- Jeff:  15% de paquetes, falla 1 de cada 90
- Pat:    5% de paquetes, falla 1 de cada 200

Si un cliente se queja de que su paquete no muestra la
fecha, ¿cuál es la probabilidad de que haya sido
inspeccionado por John?
=========================================================
"""
    print(enunciado)

    P_insp = [0.20, 0.60, 0.15, 0.05]  # P(cada inspector)
    tasas_falla = [1/200, 1/100, 1/90, 1/200]
    nombres = ["John", "Tom", "Jeff", "Pat"]

    print("--- PRELIMINAR: organización de datos ---")
    for i in range(4):
        print(f"  {nombres[i]}: P(inspecciona) = {P_insp[i]}, P(falla | inspecciona) = {tasas_falla[i]:.5f}")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Primero calculamos P(falta de fecha) por probabilidad total:")
    P_falla = sum(P_insp[i] * tasas_falla[i] for i in range(4))
    for i in range(4):
        contrib = P_insp[i] * tasas_falla[i]
        print(f"  {nombres[i]}: {P_insp[i]} × {tasas_falla[i]:.5f} = {contrib:.6f}")
    print(f"  → P(falta fecha) = {P_falla:.6f}")
    print()

    print("Ahora aplicamos Bayes para John:")
    num = P_insp[0] * tasas_falla[0]
    prob_john = num / P_falla
    print(f"                        P(John) × P(falla|John)")
    print(f"  P(John | sin fecha) = ─────────────────────────")
    print(f"                              P(sin fecha)")
    print(f"                        {P_insp[0]} × {tasas_falla[0]:.5f}     {num:.6f}")
    print(f"                      = ─────────────── = ────────── = {prob_john:.4f}")
    print(f"                              {P_falla:.6f}     {P_falla:.6f}")

    post = [(P_insp[i] * tasas_falla[i]) / P_falla for i in range(4)]
    crear_graficas(post, nombres)


if __name__ == "__main__":
    main()

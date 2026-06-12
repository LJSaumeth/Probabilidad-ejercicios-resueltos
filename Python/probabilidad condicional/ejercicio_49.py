import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(49)
    plt.bar(["a) Sobrevive 1°, rechazado 2°", "b) Rechazado por 3er dpto."],
            [prob_a, prob_b], color=["#3498db", "#e74c3c"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.78 — Inspección de vacuna")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.002, f"{v:.4f}", ha="center")
    guardar_figura(out, "inspeccion_vacuna")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.78
Un fabricante de vacuna para la gripe tiene tres
departamentos que procesan lotes de suero con tasas de
rechazo de 0.10, 0.08 y 0.12, respectivamente. Las
inspecciones son secuenciales e independientes.

a) ¿Cuál es la probabilidad de que un lote sobreviva a la
   1ª inspección pero sea rechazado por la 2ª?
b) ¿Cuál es la probabilidad de que un lote sea rechazado
   por el 3er departamento?
=========================================================
"""
    print(enunciado)

    r1 = 0.10
    r2 = 0.08
    r3 = 0.12

    s1 = 1 - r1
    s2 = 1 - r2
    s3 = 1 - r3

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Para que sobreviva al 1° (no rechazado) Y sea rechazado por el 2°, multiplicamos las probabilidades independientes.")
    prob_a = s1 * r2
    print(f"-> P(sobrevive 1°) = 1 − {r1} = {s1}")
    print(f"-> P(rechazado 2°) = {r2}")
    print(f"-> P(sobrevive 1° y rechazado 2°) = {s1} × {r2} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para ser rechazado por el 3er departamento, el lote debe haber sobrevivido al 1° y al 2° primero (si fue rechazado antes, ya no llega al 3°).")
    print("P(rechazado 3°) = P(sobrevive 1°) × P(sobrevive 2°) × P(rechazado 3°)")
    prob_b = s1 * s2 * r3
    print(f"-> P = {s1} × {s2} × {r3} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

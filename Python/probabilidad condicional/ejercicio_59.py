import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b, esperados_c, prob_d):
    out = carpeta_graficas(59)
    etiquetas = ["a) P(No pasa)", "b) P(Falla 2 o 3)", "c) CDs rechazados", "d) P(Defect.|Probado)"]
    valores = [prob_a, prob_b, esperados_c / 100, prob_d]
    plt.bar(etiquetas, valores, color=["#e74c3c", "#f39c12", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad / Cantidad")
    plt.title("Ejercicio 2.88 — Prueba de CDs")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.005, f"{v:.4f}", ha="center")
    guardar_figura(out, "prueba_cds")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.88
Antes de distribuir software estadístico se prueba cada
4º CD. El proceso corre 4 programas independientes con
tasas de falla: 0.01, 0.03, 0.02 y 0.01.

a) ¿Probabilidad de que un CD probado no pase la prueba?
b) Dado que se prueba un CD, ¿probabilidad de que falle
   el programa 2 o 3?
c) En una muestra de 100 CDs, ¿cuántos se esperaría que
   se rechazaran?
d) Dado que un CD está defectuoso, ¿probabilidad de que
   se pruebe?
=========================================================
"""
    print(enunciado)

    f1 = 0.01
    f2 = 0.03
    f3 = 0.02
    f4 = 0.01

    p1 = 1 - f1
    p2 = 1 - f2
    p3 = 1 - f3
    p4 = 1 - f4

    print("--- SOLUCIÓN a) ---")
    print("Explicación: El CD no pasa la prueba si al menos un programa falla = 1 − P(todos pasan).")
    P_todos_pasan = p1 * p2 * p3 * p4
    prob_a = 1 - P_todos_pasan
    print(f"-> P(todos pasan) = {p1} × {p2} × {p3} × {p4} = {P_todos_pasan:.6f}")
    print(f"-> P(no pasa) = 1 − {P_todos_pasan:.6f} = {prob_a:.6f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(falla programa 2 o 3) = P(falla 2) + P(falla 3) − P(falla 2 y 3).")
    print("Como son independientes: P(falla 2 y 3) = f2 × f3.")
    prob_b = f2 + f3 - f2 * f3
    print(f"-> P(falla 2 ∪ 3) = {f2} + {f3} − ({f2}×{f3}) = {prob_b:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Solo se prueba 1 de cada 4 CDs. De los probados, la tasa de rechazo es P(no pasa).")
    print("Total de CDs probados en 100 = 100 / 4 = 25.")
    probados = 100 / 4
    esperados_c = probados * prob_a
    print(f"-> CDs probados: 100 / 4 = {probados:.0f}")
    print(f"-> Rechazados esperados: {probados:.0f} × {prob_a:.6f} = {esperados_c:.4f}\n")

    print("--- SOLUCIÓN d) ---")
    print("Explicación: P(Probado | Defectuoso). Se prueba 1 de cada 4 CDs. Si un CD es defectuoso, la probabilidad de que esté entre los probados es 1/4 = 0.25, ya que la selección para prueba es independiente de ser defectuoso.")
    prob_d = 1 / 4
    print(f"-> P(Probado | Defectuoso) = {prob_d}")

    crear_graficas(prob_a, prob_b, esperados_c, prob_d)


if __name__ == "__main__":
    main()

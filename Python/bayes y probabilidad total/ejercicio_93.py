import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(93)
    plt.bar(["a) P(Sindicato | misma área)", "b) P(Desempleado | sindicato)"],
            [prob_a, prob_b], color=["#3498db", "#e74c3c"])
    plt.ylabel("Probabilidad condicional")
    plt.title("Ejercicio 2.126 — Trabajadores sindicalizados")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "sindicato_trabajadores")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.126
Historia de 100 trabajadores desplazados por tecnología:

| Situación               | Sindicalizado | No sindicalizado |
|-------------------------|--------------|------------------|
| Misma empresa           | 40           | 15               |
| Otra empresa (misma área)| 13          | 10               |
| Nueva área              | 4            | 11               |
| Desempleado             | 2            | 5                |

a) Si encontró empleo en la misma área de otra empresa,
   ¿P(sea sindicalizado)?
b) Si es sindicalizado, ¿P(esté desempleado)?
=========================================================
"""
    print(enunciado)

    total = 100
    total_sindicato = 40 + 13 + 4 + 2
    total_no_sindicato = 15 + 10 + 11 + 5

    misma_area_otra = 13 + 10
    sindicato_misma_area = 13

    print("--- PRELIMINAR: totales ---")
    print(f"  Total sindicalizados: {total_sindicato}")
    print(f"  Total no sindicalizados: {total_no_sindicato}")
    print(f"  Total (verificación): {total_sindicato + total_no_sindicato}")
    print()

    print("--- SOLUCIÓN a) ---")
    print("P(Sindicalizado | Misma área en otra empresa)")
    print(f"  = {sindicato_misma_area} / {misma_area_otra}")
    prob_a = sindicato_misma_area / misma_area_otra
    print(f"  = {prob_a:.4f}")
    print()

    print("--- SOLUCIÓN b) ---")
    print("P(Desempleado | Sindicalizado)")
    desempleados_sindicato = 2
    prob_b = desempleados_sindicato / total_sindicato
    print(f"  = {desempleados_sindicato} / {total_sindicato}")
    print(f"  = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

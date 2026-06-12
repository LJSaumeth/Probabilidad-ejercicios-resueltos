import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(84)
    plt.bar(["a) P(conjunto específico de 2)", "b) P(temp. más alta en 2)"],
            [prob_a, prob_b], color=["#e74c3c", "#3498db"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.117 — Papas fritas (2 corridas)")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.0002, f"{v:.6f}", ha="center")
    guardar_figura(out, "papas_fritas_2")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.117
Considere el ejercicio 2.116. El fabricante solo puede
probar 2 combinaciones en un día.

a) ¿Probabilidad de que elija cualquier conjunto dado de
   2 corridas?
b) ¿Probabilidad de que utilice la temperatura más alta
   en cualquiera de estas 2 combinaciones?
=========================================================
"""
    print(enunciado)

    total_comb = 3 * 4 * 3

    print(f"Total de combinaciones posibles (del 2.116): {total_comb}")
    print()

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Se eligen 2 combinaciones de 36. Todas las selecciones son")
    print("igualmente probables (combinaciones, no importa el orden).")
    total_pares = math.comb(total_comb, 2)
    prob_a = 1 / total_pares
    print(f"  C(36, 2) = {total_pares:,}")
    print(f"  P(par específico) = 1 / {total_pares:,} = {prob_a:.6f}")
    print()

    print("--- SOLUCIÓN b) ---")
    print("Explicación: La temperatura más alta es 1 de los 3 niveles. Para cada")
    print("temperatura hay 4×3=12 combinaciones. Usamos complemento: que NINGUNA")
    print("de las 2 elegidas use la temperatura alta.")
    comb_sin_temp_alta = total_comb - 12
    pares_sin_alta = math.comb(comb_sin_temp_alta, 2)
    prob_b = 1 - pares_sin_alta / total_pares
    print(f"  Combinaciones sin temp. alta: {total_comb} − 12 = {comb_sin_temp_alta}")
    print(f"  Pares sin temp. alta: C({comb_sin_temp_alta}, 2) = {pares_sin_alta:,}")
    print(f"  P(al menos 1 con temp. alta) = 1 − {pares_sin_alta}/{total_pares} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

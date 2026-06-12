import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
import numpy as np
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(46)
    plt.bar(["a) P(Hombre | Secundaria)", "b) P(No Univ. | Mujer)"],
            [prob_a, prob_b], color=["#3498db", "#e74c3c"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.75 — Género y escolaridad")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "genero_escolaridad")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.75
Clasificación según género y nivel de escolaridad de una
muestra de 200 adultos:

| Escolaridad | Hombre | Mujer |
|-------------|--------|-------|
| Primaria    | 38     | 45    |
| Secundaria  | 28     | 50    |
| Universidad | 22     | 17    |

Si se elige una persona al azar, ¿cuál es la probabilidad
de que:

a) la persona sea hombre, dado que su escolaridad es de
   secundaria?
b) la persona no tenga un grado universitario, dado que
   es mujer?
=========================================================
"""
    print(enunciado)

    total = 200
    total_secundaria = 28 + 50
    hombres_secundaria = 28

    total_mujeres = 45 + 50 + 17
    mujeres_no_univ = 45 + 50

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(Hombre | Secundaria) = hombres con secundaria / total con secundaria.")
    prob_a = hombres_secundaria / total_secundaria
    print(f"-> Total con secundaria: {28} + {50} = {total_secundaria}")
    print(f"-> Hombres con secundaria: {hombres_secundaria}")
    print(f"-> P(Hombre | Secundaria) = {hombres_secundaria} / {total_secundaria} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(No universitario | Mujer) = mujeres sin universidad / total mujeres.")
    prob_b = mujeres_no_univ / total_mujeres
    print(f"-> Total mujeres: {45} + {50} + {17} = {total_mujeres}")
    print(f"-> Mujeres sin universidad (primaria + secundaria): {45} + {50} = {mujeres_no_univ}")
    print(f"-> P(No Univ. | Mujer) = {mujeres_no_univ} / {total_mujeres} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

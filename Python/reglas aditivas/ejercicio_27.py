import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(27)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db", "#f39c12", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.56 — Defectos de automóvil")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.005, f"{v:.2f}", ha="center")
    guardar_figura(out, "defectos_automovil")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.56
Un fabricante de automóviles está preocupado por el
posible retiro de su sedán de cuatro puertas. Si fuera
retirado habría 0.25 de probabilidad de defecto en
frenos, 0.18 en transmisión, 0.17 en sistema de
combustible y 0.40 en alguna otra área.

a) ¿Cuál es la probabilidad de que el defecto esté en
   los frenos o en el sistema de combustible, si la
   probabilidad de defectos simultáneos en ambos
   sistemas es 0.15?

b) ¿Cuál es la probabilidad de que no haya defecto en
   los frenos o en el sistema de combustible?
=========================================================
"""
    print(enunciado)

    P_F = 0.25
    P_C = 0.17
    P_F_int_C = 0.15

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Usamos la regla aditiva:")
    print("P(F ∪ C) = P(F) + P(C) − P(F ∩ C)")
    P_union = P_F + P_C - P_F_int_C
    print(f"-> P(F ∪ C) = {P_F} + {P_C} − {P_F_int_C} = {P_union}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'No haya defecto en frenos ni en combustible' = complemento de la unión:")
    print("P(F' ∩ C') = 1 − P(F ∪ C)")
    P_ninguno = 1 - P_union
    print(f"-> P(ninguno) = 1 − {P_union} = {P_ninguno}")

    crear_graficas(
        ["P(Frenos)", "P(Combustible)", "P(F ∩ C)", "P(F ∪ C)"],
        [P_F, P_C, P_F_int_C, P_union]
    )


if __name__ == "__main__":
    main()

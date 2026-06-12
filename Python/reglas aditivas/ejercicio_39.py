import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(39)
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.68 — Compra de hornos")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.3f}", ha="center")
    guardar_figura(out, "compra_hornos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.68
Existe interés por el tipo de horno (eléctrico o de gas)
que compran seis clientes distintos.

a) Suponga que hay 0.40 de probabilidad de que como máximo
   dos clientes compren horno eléctrico. ¿Cuál será la
   probabilidad de que al menos tres compren horno
   eléctrico?

b) Suponga que la probabilidad de que los seis compren
   horno eléctrico es 0.007, mientras que la probabilidad
   de que los seis compren horno de gas es 0.104. ¿Cuál es
   la probabilidad de vender al menos un horno de cada tipo?
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'Al menos 3 eléctricos' es el complemento de 'como máximo 2 eléctricos'.")
    P_max_2 = 0.40
    P_al_menos_3 = 1 - P_max_2
    print(f"-> P(≥ 3 eléctricos) = 1 − P(≤ 2 eléctricos) = 1 − {P_max_2} = {P_al_menos_3}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Al menos uno de cada tipo' es el complemento de 'todos del mismo tipo'.")
    print("Que todos sean del mismo tipo significa: todos eléctricos O todos de gas (eventos mutuamente excluyentes).")
    P_todos_electricos = 0.007
    P_todos_gas = 0.104
    P_todos_igual = P_todos_electricos + P_todos_gas
    P_al_menos_uno_cada = 1 - P_todos_igual
    print(f"-> P(todos eléctricos) = {P_todos_electricos}")
    print(f"-> P(todos gas) = {P_todos_gas}")
    print(f"-> P(todos igual) = {P_todos_electricos} + {P_todos_gas} = {P_todos_igual}")
    print(f"-> P(al menos uno de cada) = 1 − {P_todos_igual} = {P_al_menos_uno_cada}")

    crear_graficas(
        ["a) P(≥3 eléctricos)", "b) P(≥1 de cada)", "P(todos igual)"],
        [P_al_menos_3, P_al_menos_uno_cada, P_todos_igual]
    )


if __name__ == "__main__":
    main()

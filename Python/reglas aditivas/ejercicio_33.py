import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(combinaciones, prob_especifica):
    out = carpeta_graficas(33)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.bar(["Total combinaciones"], [combinaciones], color="#3498db")
    ax1.set_ylabel("Combinaciones")
    ax1.set_title("Espacio muestral")
    ax1.text(0, combinaciones / 2, str(combinaciones), ha="center", fontsize=14, fontweight="bold")

    ax2.bar(["Pasta delgada + Salsa estándar"], [prob_especifica], color="#e74c3c")
    ax2.set_ylabel("Probabilidad")
    ax2.set_title("Probabilidad específica")
    ax2.text(0, prob_especifica / 2, f"{prob_especifica:.4f}", ha="center", fontsize=14, fontweight="bold")

    plt.suptitle("Ejercicio 2.62 — Dom's Pizza")
    guardar_figura(out, "doms_pizza")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.62
Dom's Pizza utiliza pruebas de sabor antes de comercializar
productos nuevos. Considere un estudio con tres tipos de
pastas (delgada, delgada con ajo y orégano, delgada con
trozos de queso) y tres salsas (estándar, nueva salsa con
más ajo, nueva salsa con albahaca fresca).

a) ¿Cuántas combinaciones de pasta y salsa se incluyen?
b) ¿Cuál es la probabilidad de que un juez reciba una
   pasta delgada sencilla con salsa estándar en su primera
   prueba de sabor?
=========================================================
"""
    print(enunciado)

    num_pastas = 3
    num_salsas = 3

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Por el principio fundamental del conteo, multiplicamos el número de opciones de cada categoría.")
    combinaciones = num_pastas * num_salsas
    print(f"-> Tipos de pasta: {num_pastas}")
    print(f"-> Tipos de salsa: {num_salsas}")
    print(f"-> Total combinaciones = {num_pastas} × {num_salsas} = {combinaciones}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Solo hay 1 combinación específica (pasta delgada sencilla + salsa estándar) entre el total de combinaciones equiprobables.")
    prob = 1 / combinaciones
    print(f"-> Casos favorables: 1")
    print(f"-> Casos totales: {combinaciones}")
    print(f"-> P = 1 / {combinaciones} = {prob:.4f}")

    crear_graficas(combinaciones, prob)


if __name__ == "__main__":
    main()

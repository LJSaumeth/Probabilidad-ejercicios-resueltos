import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fractions import Fraction
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(78)
    plt.bar(["P(Mujer ≥ 25 años)"], [prob], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.111 — Reclusos")
    plt.text(0, prob / 2, f"{prob:.4f}", ha="center", fontsize=14)
    guardar_figura(out, "reclusos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.111
Se sabe que 2/3 de los reclusos en una prisión son menores
de 25 años. También que 3/5 son hombres y que 5/8 son
mujeres de 25 años o mayores. ¿Cuál es la probabilidad de
que un prisionero seleccionado al azar sea mujer y tenga
al menos 25 años?
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN ---")
    print("Explicación: 'Mujeres de 25 años o mayores' ya es dato directo.")
    print("El enunciado dice: '5/8 son mujeres de 25 años o mayores'.")
    print()
    print("Verificación de consistencia de los datos:")
    print(f"  P(menor de 25) = 2/3 = {2/3:.4f}")
    print(f"  P(hombre) = 3/5 = {3/5:.4f}")
    print(f"  P(mujer ≥ 25) = 5/8 = {5/8:.4f}")
    print()
    prob = 5/8
    print(f"  → P(mujer y ≥ 25 años) = 5/8 = {prob:.4f}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

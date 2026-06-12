import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(autos, probs):
    out = carpeta_graficas(73)
    colores = ["#3498db" if a <= 2 else "#e74c3c" if a <= 4 else "#f39c12" for a in autos]
    plt.bar(autos, probs, color=colores)
    plt.xlabel("Número de autos")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.106 — Gasolina en 30 min")
    for i, (a, p) in enumerate(zip(autos, probs)):
        plt.text(i, p + 0.005, f"{p}", ha="center")
    guardar_figura(out, "gasolina_30min")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.106
Las probabilidades de que una estación de servicio bombee
gasolina a 0, 1, 2, 3, 4, 5 o más automóviles en 30 min
son: 0.03, 0.18, 0.24, 0.28, 0.10 y 0.17.

Calcule la probabilidad de que en 30 minutos:
a) más de 2 automóviles reciban gasolina;
b) a lo sumo 4 automóviles reciban gasolina;
c) 4 o más automóviles reciban gasolina.
=========================================================
"""
    print(enunciado)

    autos = [0, 1, 2, 3, 4, "5+"]
    probs = [0.03, 0.18, 0.24, 0.28, 0.10, 0.17]

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'Más de 2' = P(3) + P(4) + P(5+).")
    prob_a = probs[3] + probs[4] + probs[5]
    print(f"  P(>2) = {probs[3]} + {probs[4]} + {probs[5]} = {prob_a}")
    print()

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'A lo sumo 4' = P(≤4) = 1 − P(5+).")
    prob_b = 1 - probs[5]
    print(f"  P(≤4) = 1 − P(5+) = 1 − {probs[5]} = {prob_b}")
    print()

    print("--- SOLUCIÓN c) ---")
    print("Explicación: '4 o más' = P(4) + P(5+).")
    prob_c = probs[4] + probs[5]
    print(f"  P(≥4) = {probs[4]} + {probs[5]} = {prob_c}")

    crear_graficas(autos, probs)


if __name__ == "__main__":
    main()

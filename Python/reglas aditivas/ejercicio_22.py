import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(cantidades, probs):
    out = carpeta_graficas(22)
    etiquetas = [f"${c}" for c in cantidades]
    plt.bar(etiquetas, probs, color=["#f39c12", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.51 — Distribución de sobres con dinero")
    for i, (v, c) in enumerate(zip(probs, cantidades)):
        plt.text(i, v + 0.01, f"{v:.3f} ({c} sobres)", ha="center")
    guardar_figura(out, "sobres_dinero")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.51
Una caja contiene 500 sobres, de los cuales 75 contienen
$100 en efectivo, 150 contienen $25 y 275 contienen $10.
Se puede comprar un sobre en $25.

¿Cuál es el espacio muestral para las diferentes
cantidades de dinero? Asigne probabilidades a los puntos
muestrales y después calcule la probabilidad de que el
primer sobre que se compre contenga menos de $100.
=========================================================
"""
    print(enunciado)

    total = 500
    c_100 = 75
    c_25 = 150
    c_10 = 275

    print("--- SOLUCIÓN: Espacio muestral y probabilidades ---")
    print("Explicación: El espacio muestral son las cantidades posibles de dinero contenidas en un sobre.")
    print("Como la compra es aleatoria, usamos la regla de Laplace: P(cantidad) = sobres de esa cantidad / total.")

    espacio = ["$10", "$25", "$100"]
    p_10 = c_10 / total
    p_25 = c_25 / total
    p_100 = c_100 / total

    print(f"-> Espacio muestral: {espacio}")
    print(f"-> P($10)  = {c_10} / {total} = {p_10:.4f}")
    print(f"-> P($25)  = {c_25} / {total} = {p_25:.4f}")
    print(f"-> P($100) = {c_100} / {total} = {p_100:.4f}")
    print(f"-> Verificación: {p_10:.4f} + {p_25:.4f} + {p_100:.4f} = {p_10 + p_25 + p_100:.4f}\n")

    print("--- SOLUCIÓN: Probabilidad de menos de $100 ---")
    print("Explicación: 'Menos de $100' incluye los sobres de $10 y $25. Por la regla aditiva (eventos mutuamente excluyentes):")
    p_menos_100 = p_10 + p_25
    print(f"-> P(< $100) = P($10) + P($25) = {p_10:.4f} + {p_25:.4f} = {p_menos_100:.4f}")
    print(f"-> O directamente: ({c_10} + {c_25}) / {total} = {c_10 + c_25} / {total} = {p_menos_100:.4f}")

    crear_graficas([10, 25, 100], [p_10, p_25, p_100])


if __name__ == "__main__":
    main()

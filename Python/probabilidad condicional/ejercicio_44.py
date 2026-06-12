import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas():
    out = carpeta_graficas(44)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis("off")
    texto = (
        "Probabilidad condicional:\n"
        "P(A|B) = P(A ∩ B) / P(B)\n\n"
        "a) P(R|D): probabilidad de robo a mano armada\n"
        "   dado que vende drogas.\n"
        "b) P(D'|R): probabilidad de no vender drogas\n"
        "   dado que cometió robo a mano armada.\n"
        "c) P(R'|D'): probabilidad de no cometer robo\n"
        "   dado que no vende drogas."
    )
    ax.text(0.5, 0.5, texto, transform=ax.transAxes, fontsize=12,
            verticalalignment="center", horizontalalignment="center",
            fontfamily="monospace",
            bbox=dict(boxstyle="round", facecolor="#ecf0f1", alpha=0.8))
    plt.title("Ejercicio 2.73 — Interpretación de probabilidad condicional")
    guardar_figura(out, "interpretacion_condicional")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.73
Si R es el evento de que un convicto cometa un robo a mano
armada y D es el evento de que venda drogas, exprese en
palabras lo que en probabilidades se indica como:

a) P(R|D)
b) P(D'|R)
c) P(R'|D')
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(R|D) se lee 'probabilidad de R dado D'.")
    print("-> Probabilidad de que un convicto cometa un robo a mano armada,")
    print("   dado que vende drogas.\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: D' es el complemento de D (no vende drogas).")
    print("-> Probabilidad de que un convicto no venda drogas,")
    print("   dado que cometió un robo a mano armada.\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: R' y D' son los complementos de ambos eventos.")
    print("-> Probabilidad de que un convicto no cometa un robo a mano armada,")
    print("   dado que no vende drogas.")

    crear_graficas()


if __name__ == "__main__":
    main()

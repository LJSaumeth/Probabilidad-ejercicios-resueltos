import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas():
    out = carpeta_graficas(69)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis("off")
    texto = (
        "PROBLEMA DE MONTY HALL\n\n"
        "Estrategia inicial: elegir puerta A.\n"
        "P(premio en A) = 1/3\n"
        "P(premio en B o C) = 2/3\n\n"
        "El presentador abre B (sin premio).\n"
        "→ P(premio en C | abrió B) = 2/3\n"
        "→ P(premio en A | abrió B) = 1/3\n\n"
        "Conclusión: conviene CAMBIAR a C.\n"
        "Probabilidad de ganar cambia de 1/3 a 2/3."
    )
    ax.text(0.5, 0.5, texto, transform=ax.transAxes, fontsize=12,
            verticalalignment="center", horizontalalignment="center",
            fontfamily="monospace",
            bbox=dict(boxstyle="round", facecolor="#ecf0f1", alpha=0.8))
    plt.title("Ejercicio 2.102 — Monty Hall")
    guardar_figura(out, "monty_hall")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.102 (Problema de Monty Hall)
Denote A, B, C los eventos de que el gran premio esté
detrás de cada puerta. Usted elige A. El presentador abre
B y muestra que no hay premio. ¿Conviene cambiar a C?

Utilice probabilidad para explicarlo.
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN ---")
    print()
    print("CASO 1: El premio está en A (probabilidad 1/3).")
    print("  El presentador puede abrir B o C (ambas vacías).")
    print("  Si abre B y usted se queda en A → GANA.")
    print("  Si abre B y usted cambia a C → PIERDE.")
    print("  P(ganar quedándose | premio en A) = 1")
    print()
    print("CASO 2: El premio está en B (probabilidad 1/3).")
    print("  El presentador NO puede abrir B (tiene premio).")
    print("  El presentador DEBE abrir C (la única vacía restante).")
    print("  → El presentador NO abrió B, abrió C. Este caso no ocurre aquí.")
    print()
    print("CASO 3: El premio está en C (probabilidad 1/3).")
    print("  El presentador NO puede abrir C (tiene premio).")
    print("  El presentador DEBE abrir B (la única vacía restante).")
    print("  → El presentador abre B. Si usted cambia a C → GANA.")
    print()

    print("Conclusión: dado que el presentador abrió B:")
    print("  - Si el premio estaba en A (1/3): quedarse gana.")
    print("  - Si el premio estaba en C (1/3): cambiar gana.")
    print("  - Si el premio estaba en B (1/3): el presentador habría abierto C, no B.")
    print()
    print("Por Bayes:")
    print("P(premio en C | abrió B) = P(abre B | premio en C)×P(C) / P(abre B)")
    print("  = (1)×(1/3) / (1/2) = (1/3)/(1/2) = 2/3")
    print()
    print("→ SÍ conviene cambiar. Con cambio: P(ganar) = 2/3.")
    print("  Sin cambio: P(ganar) = 1/3.")

    crear_graficas()


if __name__ == "__main__":
    main()

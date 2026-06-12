import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas():
    out = carpeta_graficas(72)
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.axis("off")
    texto = (
        "DIAGRAMA DE VENN\n\n"
        "a) (A ∩ B) ∪ (A ∩ B') = A ∩ (B ∪ B') = A ∩ S = A  ✓\n\n"
        "b) A' ∩ (B' ∪ C) = (A' ∩ B') ∪ (A' ∩ C)\n"
        "   Por ley distributiva de ∩ sobre ∪  ✓"
    )
    ax.text(0.5, 0.5, texto, transform=ax.transAxes, fontsize=12,
            verticalalignment="center", horizontalalignment="center",
            fontfamily="monospace",
            bbox=dict(boxstyle="round", facecolor="#ecf0f1", alpha=0.8))
    plt.title("Ejercicio 2.105 — Verificación con diagrama de Venn")
    guardar_figura(out, "verificacion_venn")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.105
Mediante diagramas de Venn verifique que:

a) (A ∩ B) ∪ (A ∩ B') = A
b) A' ∩ (B' ∪ C) = (A' ∩ B') ∪ (A' ∩ C)
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("  (A ∩ B) ∪ (A ∩ B')")
    print("  = A ∩ (B ∪ B')          [Factor común A por ley distributiva]")
    print("  = A ∩ S                 [B ∪ B' = S, el espacio muestral]")
    print("  = A                     [A ∩ S = A]")
    print()
    print("  Interpretación en Venn:")
    print("  (A ∩ B) es la región de A que solapa con B.")
    print("  (A ∩ B') es la región de A que NO solapa con B.")
    print("  La unión de ambas ES todo A. ∎")
    print()

    print("--- SOLUCIÓN b) ---")
    print("  A' ∩ (B' ∪ C)")
    print("  = (A' ∩ B') ∪ (A' ∩ C)    [Ley distributiva de ∩ sobre ∪]")
    print()
    print("  Es una identidad directa. La intersección se distribuye sobre la unión.")
    print("  Como en álgebra: x·(y+z) = x·y + x·z. ∎")

    crear_graficas()


if __name__ == "__main__":
    main()

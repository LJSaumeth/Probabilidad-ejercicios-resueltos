import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas():
    out = carpeta_graficas(43)
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.axis("off")
    texto = (
        "P(A' ∩ B') = P((A ∪ B)')         [De Morgan]\n"
        "           = 1 − P(A ∪ B)\n"
        "           = 1 − [P(A) + P(B) − P(A ∩ B)]\n"
        "           = 1 − P(A) − P(B) + P(A ∩ B)\n"
        "           = 1 + P(A ∩ B) − P(A) − P(B)  ✓"
    )
    ax.text(0.5, 0.5, texto, transform=ax.transAxes, fontsize=14,
            verticalalignment="center", horizontalalignment="center",
            fontfamily="monospace",
            bbox=dict(boxstyle="round", facecolor="#ecf0f1", alpha=0.8))
    plt.title("Ejercicio 2.72 — Demostración")
    guardar_figura(out, "demostracion")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.72
Demuestre que:

P(A' ∩ B') = 1 + P(A ∩ B) − P(A) − P(B)
=========================================================
"""
    print(enunciado)

    print("--- DEMOSTRACIÓN ---")
    print()
    print("Paso 1: Aplicamos la ley de De Morgan.")
    print("  P(A' ∩ B') = P((A ∪ B)')")
    print("  Justificación: El complemento de la intersección de los complementos es el complemento de la unión.")
    print()
    print("Paso 2: La probabilidad del complemento es 1 menos la probabilidad del evento.")
    print("  P((A ∪ B)') = 1 − P(A ∪ B)")
    print()
    print("Paso 3: Aplicamos la regla aditiva de probabilidad.")
    print("  P(A ∪ B) = P(A) + P(B) − P(A ∩ B)")
    print()
    print("Paso 4: Sustituimos en la expresión del paso 2.")
    print("  P(A' ∩ B') = 1 − [P(A) + P(B) − P(A ∩ B)]")
    print()
    print("Paso 5: Distribuimos el signo negativo.")
    print("  P(A' ∩ B') = 1 − P(A) − P(B) + P(A ∩ B)")
    print()
    print("Paso 6: Reordenamos los términos.")
    print("  P(A' ∩ B') = 1 + P(A ∩ B) − P(A) − P(B)")
    print()
    print("∎ Queda demostrado.")

    crear_graficas()


if __name__ == "__main__":
    main()

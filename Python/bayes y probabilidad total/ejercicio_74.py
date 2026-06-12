import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(manos):
    out = carpeta_graficas(74)
    plt.bar(["Manos de bridge"], [manos], color="#3498db")
    plt.ylabel("Número de manos")
    plt.title("Ejercicio 2.107 — Manos de bridge")
    plt.text(0, manos / 2, f"{manos:,}", ha="center", fontsize=14, fontweight="bold")
    guardar_figura(out, "manos_bridge")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.107
¿Cuántas manos de bridge que contengan 4 espadas,
6 diamantes, 1 trébol y 2 corazones son posibles?
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN (Combinatoria) ---")
    print("Una mano de bridge tiene 13 cartas. Cada palo tiene 13 cartas.")
    print("Elegimos independientemente de cada palo:")
    print()
    print("  4 espadas de 13:   C(13, 4)")
    print("  6 diamantes de 13:  C(13, 6)")
    print("  1 trébol de 13:     C(13, 1)")
    print("  2 corazones de 13:  C(13, 2)")
    print()

    c1 = math.comb(13, 4)
    c2 = math.comb(13, 6)
    c3 = math.comb(13, 1)
    c4 = math.comb(13, 2)

    print(f"  C(13, 4) = {c1:,}")
    print(f"  C(13, 6) = {c2:,}")
    print(f"  C(13, 1) = {c3}")
    print(f"  C(13, 2) = {c4}")
    print()

    total = c1 * c2 * c3 * c4
    print(f"  Total = {c1:,} × {c2:,} × {c3} × {c4} = {total:,} manos")

    crear_graficas(total)


if __name__ == "__main__":
    main()

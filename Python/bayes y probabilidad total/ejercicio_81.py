import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(formas):
    out = carpeta_graficas(81)
    plt.bar(["Formas de comprar 5 TV con ≥ 2 defectuosos"], [formas], color="#e74c3c")
    plt.ylabel("Número de formas")
    plt.title("Ejercicio 2.114 — Televisores defectuosos")
    plt.text(0, formas / 2, f"{formas}", ha="center", fontsize=14)
    guardar_figura(out, "televisores_defectuosos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.114
Un cargamento de 12 televisores contiene 3 defectuosos.
¿De cuántas formas puede un hotel comprar 5 de estos
aparatos y recibir al menos 2 defectuosos?
=========================================================
"""
    print(enunciado)

    total = 12
    defectuosos = 3
    buenos = 9
    comprar = 5

    print("--- SOLUCIÓN (Combinatoria) ---")
    print("'Al menos 2 defectuosos' = 2 defectuosos O 3 defectuosos.")
    print()

    print("Caso 1: exactamente 2 defectuosos (y 3 buenos).")
    c2 = math.comb(defectuosos, 2) * math.comb(buenos, 3)
    print(f"  C(3, 2) × C(9, 3) = {math.comb(3,2)} × {math.comb(9,3)} = {c2}")
    print()

    print("Caso 2: exactamente 3 defectuosos (y 2 buenos).")
    c3 = math.comb(defectuosos, 3) * math.comb(buenos, 2)
    print(f"  C(3, 3) × C(9, 2) = {math.comb(3,3)} × {math.comb(9,2)} = {c3}")
    print()

    total_formas = c2 + c3
    print(f"  Total = {c2} + {c3} = {total_formas} formas")

    crear_graficas(total_formas)


if __name__ == "__main__":
    main()

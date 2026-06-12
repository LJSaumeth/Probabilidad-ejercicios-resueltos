import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
import numpy as np
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(probabilidades, etiquetas):
    out = carpeta_graficas(23)
    plt.bar(etiquetas, probabilidades, color=["#e74c3c", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.52 — Hábitos de estudiantes")
    for i, v in enumerate(probabilidades):
        plt.text(i, v + 0.01, f"{v:.3f}", ha="center")
    guardar_figura(out, "habitos_estudiantes")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.52
En un grupo de 500 estudiantes universitarios de último
año: 210 fuman, 258 consumen bebidas alcohólicas, 216
comen entre comidas, 122 fuman y consumen bebidas
alcohólicas, 83 comen entre comidas y consumen bebidas
alcohólicas, 97 fuman y comen entre comidas y 52 tienen
esos tres hábitos nocivos. Si se selecciona al azar a un
miembro, calcule la probabilidad de que el estudiante:

a) fume pero no consuma bebidas alcohólicas;
b) coma entre comidas y consuma bebidas alcohólicas pero
   no fume;
c) no fume ni coma entre comidas.
=========================================================
"""
    print(enunciado)

    total = 500
    F = 210
    B = 258
    C = 216
    F_B = 122
    C_B = 83
    F_C = 97
    F_B_C = 52

    print("--- SOLUCIÓN: Análisis por diagrama de Venn ---")
    print("Explicación: Usamos un diagrama de Venn de 3 conjuntos y el principio de inclusión-exclusión para encontrar las regiones individuales.")

    solo_F_B = F_B - F_B_C
    solo_C_B = C_B - F_B_C
    solo_F_C = F_C - F_B_C

    solo_F = F - solo_F_B - solo_F_C - F_B_C
    solo_B = B - solo_F_B - solo_C_B - F_B_C
    solo_C = C - solo_F_C - solo_C_B - F_B_C

    print(f"-> Solo fuman:                        F - F∩B - F∩C + F∩B∩C = {solo_F}")
    print(f"-> Solo beben:                        B - F∩B - C∩B + F∩B∩C = {solo_B}")
    print(f"-> Solo comen:                        C - F∩C - C∩B + F∩B∩C = {solo_C}")
    print(f"-> Fuman y beben (no comen):          F∩B - F∩B∩C = {solo_F_B}")
    print(f"-> Comen y beben (no fuman):          C∩B - F∩B∩C = {solo_C_B}")
    print(f"-> Fuman y comen (no beben):          F∩C - F∩B∩C = {solo_F_C}")
    print(f"-> Los tres hábitos:                  F∩B∩C = {F_B_C}")

    ninguno = total - (solo_F + solo_B + solo_C + solo_F_B + solo_C_B + solo_F_C + F_B_C)
    print(f"-> Ningún hábito:                     Total - suma = {ninguno}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'Fume pero no beba' = estudiantes que fuman menos los que fuman y beben.")
    p_a = (F - F_B) / total
    print(f"-> F - (F∩B) = {F} - {F_B} = {F - F_B}")
    print(f"-> P = {F - F_B} / {total} = {p_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Coma y beba pero no fume' = (C∩B) - (F∩B∩C).")
    p_b = solo_C_B / total
    print(f"-> (C∩B) - (F∩B∩C) = {C_B} - {F_B_C} = {solo_C_B}")
    print(f"-> P = {solo_C_B} / {total} = {p_b:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: 'No fume ni coma' = complemento de (F ∪ C). Usamos: |F ∪ C| = |F| + |C| - |F∩C|.")
    union_FC = F + C - F_C
    p_c = 1 - union_FC / total
    print(f"-> |F ∪ C| = {F} + {C} - {F_C} = {union_FC}")
    print(f"-> P(no F y no C) = 1 - {union_FC}/{total} = 1 - {union_FC/total:.4f} = {p_c:.4f}")

    crear_graficas([p_a, p_b, p_c], ["a) Fuma no bebe", "b) Come y bebe no fuma", "c) No fuma ni come"])


if __name__ == "__main__":
    main()

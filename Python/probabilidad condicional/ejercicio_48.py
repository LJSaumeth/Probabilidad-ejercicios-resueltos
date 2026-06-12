import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(48)
    plt.bar(["a) P(3 materias | Psic.)", "b) P(Hist y Mat | No Psic.)"],
            [prob_a, prob_b], color=["#9b59b6", "#f39c12"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.77 — Estudiantes: 3 materias")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.005, f"{v:.4f}", ha="center")
    guardar_figura(out, "tres_materias")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.77
En un grupo de 100 estudiantes de bachillerato del último
año: 42 cursaron matemáticas, 68 psicología, 54 historia,
22 matemáticas e historia, 25 matemáticas y psicología,
7 historia pero ni matemáticas ni psicología, 10 las tres
materias y 8 no cursaron ninguna de las tres.

Seleccione al azar un estudiante y calcule:

a) Una persona inscrita en psicología cursa las tres
   materias;
b) Una persona que no está inscrita en psicología esté
   cursando historia y matemáticas.
=========================================================
"""
    print(enunciado)

    total = 100
    M = 42
    P = 68
    H = 54
    M_H = 22
    M_P = 25
    solo_H = 7
    M_P_H = 10
    ninguno = 8

    print("--- SOLUCIÓN: Análisis por diagrama de Venn ---")
    print("Explicación: Desglosamos cada región del diagrama de Venn de 3 conjuntos.")

    M_P_solo = M_P - M_P_H
    M_H_solo = M_H - M_P_H

    P_H = H - solo_H - M_H_solo - M_P_H
    P_H_solo = P_H - M_P_H

    solo_M = M - M_P_solo - M_H_solo - M_P_H
    solo_P = P - M_P_solo - P_H_solo - M_P_H

    print(f"-> Solo Matemáticas:                {solo_M}")
    print(f"-> Solo Psicología:                 {solo_P}")
    print(f"-> Solo Historia:                   {solo_H}")
    print(f"-> M y P (sin H):                   {M_P_solo}")
    print(f"-> M y H (sin P):                   {M_H_solo}")
    print(f"-> P y H (sin M):                   {P_H_solo}")
    print(f"-> Las tres (M ∩ P ∩ H):            {M_P_H}")
    print(f"-> Ninguna:                         {ninguno}")

    verif = solo_M + solo_P + solo_H + M_P_solo + M_H_solo + P_H_solo + M_P_H + ninguno
    print(f"-> Verificación (debe ser {total}): {verif}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(cursa las 3 | cursa Psicología) = P(M∩P∩H) / P(P).")
    prob_a = M_P_H / P
    print(f"-> |M ∩ P ∩ H| = {M_P_H}")
    print(f"-> |P| = {P}")
    print(f"-> P(las 3 | Psic.) = {M_P_H} / {P} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(Historia y Matemáticas | No Psicología) = P(H∩M∩P') / P(P').")
    no_P = total - P
    prob_b = M_H_solo / no_P
    print(f"-> |M ∩ H sin P| = {M_H_solo}")
    print(f"-> |No Psicología| = {total} − {P} = {no_P}")
    print(f"-> P(H y M | No Psic.) = {M_H_solo} / {no_P} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

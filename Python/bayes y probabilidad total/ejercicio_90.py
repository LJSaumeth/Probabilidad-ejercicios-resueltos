import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(90)
    plt.bar(["P(Hospital ∪ Regresar al día sig.)"], [prob], color="#9b59b6")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.123 — Trabajadores lesionados")
    plt.text(0, prob / 2, f"{prob:.2f}", ha="center", fontsize=14)
    guardar_figura(out, "trabajadores_lesionados")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.123
Registros de trabajadores lesionados: 10% son llevados al
hospital, 15% regresan al trabajo al día siguiente, 2%
son llevados al hospital Y regresan al día siguiente. Si
un trabajador se lesiona, ¿cuál es la probabilidad de que
sea llevado al hospital, de que regrese al día siguiente,
o de ambas cosas?
=========================================================
"""
    print(enunciado)

    P_H = 0.10
    P_R = 0.15
    P_H_int_R = 0.02

    print("--- SOLUCIÓN (Regla aditiva) ---")
    print("Se pide P(H ∪ R).")
    print("P(H ∪ R) = P(H) + P(R) − P(H ∩ R)")
    prob = P_H + P_R - P_H_int_R
    print(f"  P(H ∪ R) = {P_H} + {P_R} − {P_H_int_R} = {prob}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

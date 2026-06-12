import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b):
    out = carpeta_graficas(47)
    plt.bar(["a) P(H | Emp.)", "b) P(No fuma | SH)"],
            [prob_a, prob_b], color=["#e74c3c", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.76 — Fumar e hipertensión")
    for i, v in enumerate([prob_a, prob_b]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "fumar_hipertension")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.76
Relación entre hábito de fumar e hipertensión arterial
para 180 individuos:

|                 | Fum. moderados | Fum. empedernidos | No fumadores |
|-----------------|----------------|-------------------|--------------|
| Hipertensión (H)| 21             | 36                | 30           |
| Sin hipertensión| 48             | 26                | 19           |

Si se selecciona uno al azar, calcule la probabilidad:

a) sufra hipertensión, dado que es fumador empedernido;
b) no fume, dado que no padece hipertensión.
=========================================================
"""
    print(enunciado)

    total_empedernidos = 36 + 26
    H_empedernidos = 36

    total_SH = 48 + 26 + 19
    no_fuma_SH = 19

    print("--- SOLUCIÓN a) ---")
    print("Explicación: P(Hipertensión | Fumador empedernido) = H ∩ Emp / Emp.")
    prob_a = H_empedernidos / total_empedernidos
    print(f"-> Total fumadores empedernidos: {36} + {26} = {total_empedernidos}")
    print(f"-> Con hipertensión y empedernidos: {H_empedernidos}")
    print(f"-> P(H | Emp.) = {H_empedernidos} / {total_empedernidos} = {prob_a:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(No fumador | Sin hipertensión) = No fuma ∩ SH / SH.")
    prob_b = no_fuma_SH / total_SH
    print(f"-> Total sin hipertensión: {48} + {26} + {19} = {total_SH}")
    print(f"-> No fuman y sin hipertensión: {no_fuma_SH}")
    print(f"-> P(No fuma | SH) = {no_fuma_SH} / {total_SH} = {prob_b:.4f}")

    crear_graficas(prob_a, prob_b)


if __name__ == "__main__":
    main()

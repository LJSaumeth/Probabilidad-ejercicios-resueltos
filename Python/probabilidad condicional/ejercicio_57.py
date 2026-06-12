import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_a, prob_b, prob_c):
    out = carpeta_graficas(57)
    plt.bar(["a) P(Mujer|Univ. 1970)", "b) P(Univ. 1990|Mujer)", "c) P(No Univ. 1990|Hombre)"],
            [prob_a, prob_b, prob_c], color=["#e74c3c", "#3498db", "#f39c12"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.86 — Educación universitaria por género")
    for i, v in enumerate([prob_a, prob_b, prob_c]):
        plt.text(i, v + 0.01, f"{v:.4f}", ha="center")
    guardar_figura(out, "educacion_genero")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.86
En 1970, 11% de los estadounidenses completaron 4 años de
universidad; de ese porcentaje 43% eran mujeres. En 1990,
22% completaron 4 años de universidad, y de ellos 53%
fueron mujeres. (Time, 1996).

a) Dado que una persona completó 4 años de universidad en
   1970, ¿cuál es la probabilidad de que sea mujer?
b) ¿Cuál es la probabilidad de que una mujer haya terminado
   4 años de universidad en 1990?
c) ¿Cuál es la probabilidad de que en 1990 un hombre no
   haya terminado la universidad?
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Es dato directo: P(Mujer | Universidad 1970).")
    prob_a = 0.43
    print(f"-> Dato directo del enunciado: 43% de los graduados en 1970 eran mujeres.")
    print(f"-> P(Mujer | Univ. 1970) = {prob_a}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(Universidad 1990 | Mujer) = P(Univ ∩ Mujer) / P(Mujer).")
    print("Asumiendo que la población es ~50% mujeres, P(Mujer) ≈ 0.5.")
    P_univ_1990 = 0.22
    P_mujer_dado_univ_1990 = 0.53
    P_univ_mujer_1990 = P_univ_1990 * P_mujer_dado_univ_1990
    P_mujer = 0.5
    prob_b = P_univ_mujer_1990 / P_mujer
    print(f"-> P(Univ ∩ Mujer) = P(Univ) × P(Mujer|Univ) = {P_univ_1990} × {P_mujer_dado_univ_1990} = {P_univ_mujer_1990:.4f}")
    print(f"-> P(Univ 1990 | Mujer) = {P_univ_mujer_1990:.4f} / {P_mujer} = {prob_b:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: P(No Universidad 1990 | Hombre) = 1 − P(Universidad 1990 | Hombre).")
    P_hombre = 0.5
    P_hombre_dado_univ_1990 = 1 - P_mujer_dado_univ_1990
    P_univ_hombre_1990 = P_univ_1990 * P_hombre_dado_univ_1990
    P_univ_dado_hombre = P_univ_hombre_1990 / P_hombre
    prob_c = 1 - P_univ_dado_hombre
    print(f"-> P(Hombre | Univ. 1990) = 1 − {P_mujer_dado_univ_1990} = {P_hombre_dado_univ_1990}")
    print(f"-> P(Univ ∩ Hombre) = {P_univ_1990} × {P_hombre_dado_univ_1990} = {P_univ_hombre_1990:.4f}")
    print(f"-> P(Univ 1990 | Hombre) = {P_univ_hombre_1990:.4f} / {P_hombre} = {P_univ_dado_hombre:.4f}")
    print(f"-> P(No Univ 1990 | Hombre) = 1 − {P_univ_dado_hombre:.4f} = {prob_c:.4f}")

    crear_graficas(prob_a, prob_b, prob_c)


if __name__ == "__main__":
    main()

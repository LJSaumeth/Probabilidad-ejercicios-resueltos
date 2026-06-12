import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
import numpy as np
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(probs, etiquetas):
    out = carpeta_graficas(50)
    x = np.arange(len(etiquetas))
    plt.bar(x, probs, color=["#e74c3c", "#3498db", "#f39c12", "#2ecc71"])
    plt.xticks(x, etiquetas, fontsize=8)
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.79 — Ropa para dormir al viajar")
    for i, v in enumerate(probs):
        plt.text(i, v + 0.005, f"{v:.4f}", ha="center")
    guardar_figura(out, "ropa_dormir")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.79
Resultados de encuesta sobre uso de ropa para dormir
mientras se viaja (USA Today, 1996):

|                | Hombre | Mujer | Total  |
|----------------|--------|-------|--------|
| Ropa interior  | 0.020  | 0.024 | 0.244  |
| Camisón        | 0.002  | 0.180 | 0.182  |
| Nada           | 0.160  | 0.018 | 0.178  |
| Pijama         | 0.102  | 0.073 | 0.175  |
| Camiseta       | 0.046  | 0.088 | 0.134  |
| Otros          | 0.084  | 0.003 | 0.087  |

a) P(mujer que duerme desnuda)
b) P(viajero sea hombre)
c) P(duerma con pijama | hombre)
d) P(hombre | duerme con pijama o camiseta)
=========================================================
"""
    print(enunciado)

    p_hombre = 0.020 + 0.002 + 0.160 + 0.102 + 0.046 + 0.084

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Directamente de la tabla: Mujer y 'Nada'.")
    p_mujer_nada = 0.018
    print(f"-> P(Mujer ∩ Nada) = {p_mujer_nada}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Sumamos todas las probabilidades de la columna 'Hombre'.")
    print(f"-> P(Hombre) = 0.020 + 0.002 + 0.160 + 0.102 + 0.046 + 0.084 = {p_hombre:.3f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: P(Pijama | Hombre) = P(Pijama ∩ Hombre) / P(Hombre).")
    p_pijama_hombre = 0.102
    p_pijama_dado_hombre = p_pijama_hombre / p_hombre
    print(f"-> P(Pijama | Hombre) = {p_pijama_hombre} / {p_hombre:.3f} = {p_pijama_dado_hombre:.4f}\n")

    print("--- SOLUCIÓN d) ---")
    print("Explicación: P(Hombre | Pijama ∪ Camiseta) = P(Hombre ∩ (Pijama ∪ Camiseta)) / P(Pijama ∪ Camiseta).")
    p_hombre_pijama = 0.102
    p_hombre_camiseta = 0.046
    p_pijama_total = 0.175
    p_camiseta_total = 0.134

    p_hombre_pijama_o_camiseta = p_hombre_pijama + p_hombre_camiseta
    p_pijama_o_camiseta = p_pijama_total + p_camiseta_total
    prob_d = p_hombre_pijama_o_camiseta / p_pijama_o_camiseta
    print(f"-> P(Hombre ∩ (Pij ∪ Cam)) = {p_hombre_pijama} + {p_hombre_camiseta} = {p_hombre_pijama_o_camiseta}")
    print(f"-> P(Pij ∪ Cam) = {p_pijama_total} + {p_camiseta_total} = {p_pijama_o_camiseta}")
    print(f"-> P(Hombre | Pij ∪ Cam) = {p_hombre_pijama_o_camiseta} / {p_pijama_o_camiseta} = {prob_d:.4f}")

    crear_graficas(
        [p_mujer_nada, p_hombre, p_pijama_dado_hombre, prob_d],
        ["a) Mujer desnuda", "b) P(Hombre)", "c) P(Pij|Hom)", "d) P(Hom|Pij∪Cam)"]
    )


if __name__ == "__main__":
    main()

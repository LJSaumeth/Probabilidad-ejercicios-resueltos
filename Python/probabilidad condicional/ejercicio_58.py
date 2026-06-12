import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(58)
    plt.bar(["P(Entrar a la casa)"], [prob], color="#2ecc71")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.87 — Agente de bienes raíces")
    plt.text(0, prob / 2, f"{prob:.4f}", ha="center", fontsize=14, fontweight="bold")
    guardar_figura(out, "agente_bienes_raices")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.87
Un agente de bienes raíces tiene 8 llaves maestras para
abrir varias casas nuevas. Sólo 1 llave maestra abrirá
cualquiera de las casas. Si 40% de estas casas por lo
general se dejan abiertas, ¿cuál es la probabilidad de que
el agente pueda entrar en una casa específica, si
selecciona 3 llaves maestras al azar antes de salir?
=========================================================
"""
    print(enunciado)

    total_llaves = 8
    llaves_seleccionadas = 3
    P_abierta = 0.40

    print("--- SOLUCIÓN ---")
    print("Explicación: El agente puede entrar si la casa está abierta O si tiene la llave correcta entre las 3 seleccionadas.")
    print()
    print("Caso 1: La casa está abierta (no necesita llave).")
    print(f"-> P(Casa abierta) = {P_abierta}")
    print()
    print("Caso 2: La casa está cerrada PERO el agente tiene la llave correcta entre las 3 que eligió.")
    P_cerrada = 1 - P_abierta
    print(f"-> P(Casa cerrada) = 1 − {P_abierta} = {P_cerrada}")
    print("De las 8 llaves, solo 1 es la correcta. El agente elige 3 al azar.")
    print("La probabilidad de que la llave correcta esté entre las 3 elegidas:")
    print("P(llave correcta | 3 seleccionadas) = (formas de incluir la correcta) / (formas totales de elegir 3)")
    formas_con_correcta = math.comb(7, 2)
    formas_totales = math.comb(total_llaves, 3)
    P_llave_en_seleccion = formas_con_correcta / formas_totales
    print(f"-> Formas de elegir 3 llaves incluyendo la correcta: C(7, 2) = {formas_con_correcta}")
    print(f"-> Formas totales de elegir 3 llaves: C(8, 3) = {formas_totales}")
    print(f"-> P(tiene la llave) = {formas_con_correcta} / {formas_totales} = {P_llave_en_seleccion:.4f}")
    print()
    print("Probabilidad total de entrar:")
    print("P(Entrar) = P(Abierta) + P(Cerrada) × P(Tiene llave)")
    prob = P_abierta + P_cerrada * P_llave_en_seleccion
    print(f"-> P(Entrar) = {P_abierta} + ({P_cerrada}) × ({P_llave_en_seleccion:.4f})")
    print(f"-> P(Entrar) = {P_abierta} + {P_cerrada * P_llave_en_seleccion:.4f} = {prob:.4f}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

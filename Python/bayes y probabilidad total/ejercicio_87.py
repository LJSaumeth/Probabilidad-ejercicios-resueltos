import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(87)
    plt.bar(["P(Enfermedad | Prueba positiva)"], [prob], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.120 — Enfermedad rara")
    plt.text(0, prob / 2, f"{prob:.6f}", ha="center", fontsize=14)
    guardar_figura(out, "enfermedad_rara")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.120
Una extraña enfermedad afecta a 1 de cada 500 individuos.
Una prueba tiene 95% de resultados correctos positivos
(sensibilidad) y 1% de falsos positivos. Si un individuo
elegido al azar recibe un resultado positivo, ¿cuál es la
probabilidad de que realmente tenga la enfermedad?
=========================================================
"""
    print(enunciado)

    P_E = 1/500                   # Prevalencia
    P_pos_dado_E = 0.95           # Sensibilidad
    P_pos_dado_noE = 0.01         # 1 − especificidad (falso positivo)

    P_noE = 1 - P_E

    print("--- PRELIMINAR ---")
    print(f"  P(Enfermedad) = 1/500 = {P_E:.4f}")
    print(f"  P(No enfermedad) = 1 − {P_E:.4f} = {P_noE:.4f}")
    print(f"  P(Positivo | Enfermedad) = {P_pos_dado_E}  (sensibilidad, enunciado)")
    print(f"  P(Positivo | Sano) = {P_pos_dado_noE}  (falso positivo, enunciado)")
    print()

    print("--- SOLUCIÓN (Teorema de Bayes) ---")
    print("Se pide P(Enfermedad | Prueba positiva).")
    print()

    print("Paso 1: P(Positivo) por probabilidad total.")
    P_pos = P_E * P_pos_dado_E + P_noE * P_pos_dado_noE
    c1 = P_E * P_pos_dado_E
    c2 = P_noE * P_pos_dado_noE
    print(f"  Rama enfermo: {P_E:.4f} × {P_pos_dado_E} = {c1:.6f}")
    print(f"  Rama sano:    {P_noE:.4f} × {P_pos_dado_noE} = {c2:.6f}")
    print(f"  → P(Positivo) = {P_pos:.6f}")
    print()

    print("Paso 2: Teorema de Bayes.")
    prob = c1 / P_pos
    print(f"                            {P_pos_dado_E} × {P_E:.4f}     {c1:.6f}")
    print(f"  P(Enfermo | Positivo) = ──────────────── = ─────── = {prob:.6f}")
    print(f"                               {P_pos:.6f}      {P_pos:.6f}")
    print()
    print(f"A pesar de la alta precisión de la prueba (95%), solo {prob*100:.2f}%")
    print("de los positivos realmente tienen la enfermedad, debido a la")
    print("extremadamente baja prevalencia (0.2%).")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

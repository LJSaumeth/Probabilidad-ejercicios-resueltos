import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(ubicaciones, probs):
    out = carpeta_graficas(34)
    plt.figure(figsize=(8, 5))
    plt.bar(ubicaciones, probs, color=["#e74c3c", "#e74c3c", "#e74c3c", "#3498db", "#f39c12"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.63 — Ubicación de PC en casa")
    for i, v in enumerate(probs):
        plt.text(i, v + 0.01, f"{v:.2f}", ha="center")
    guardar_figura(out, "ubicacion_pc")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.63
Porcentajes de probables ubicaciones de PC en una casa
(Consumer Digest, 1996):

- Dormitorio de adultos:     0.03
- Dormitorio de niños:       0.15
- Otro dormitorio:           0.14
- Oficina o estudio:         0.40
- Otra habitación:           0.28

a) ¿Cuál es la probabilidad de que una PC esté en un
   dormitorio?
b) ¿Cuál es la probabilidad de que no esté en un
   dormitorio?
c) Si se selecciona una casa al azar, ¿en qué habitación
   esperaría encontrar una PC?
=========================================================
"""
    print(enunciado)

    p_adultos = 0.03
    p_ninos = 0.15
    p_otro_dorm = 0.14
    p_oficina = 0.40
    p_otra = 0.28

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Sumamos las probabilidades de todos los tipos de dormitorio (eventos mutuamente excluyentes).")
    p_dormitorio = p_adultos + p_ninos + p_otro_dorm
    print(f"-> P(dormitorio) = P(adultos) + P(niños) + P(otro)")
    print(f"-> P(dormitorio) = {p_adultos} + {p_ninos} + {p_otro_dorm} = {p_dormitorio}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Es el complemento de 'estar en un dormitorio'.")
    p_no_dormitorio = 1 - p_dormitorio
    print(f"-> P(no dormitorio) = 1 − {p_dormitorio} = {p_no_dormitorio}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: La habitación con mayor probabilidad es donde 'esperaríamos' encontrar la PC (moda de la distribución).")
    probs = {
        "Dorm. adultos": p_adultos,
        "Dorm. niños": p_ninos,
        "Otro dorm.": p_otro_dorm,
        "Oficina/estudio": p_oficina,
        "Otra habitación": p_otra
    }
    max_hab = max(probs, key=probs.get)
    print(f"-> Probabilidades: {probs}")
    print(f"-> Mayor probabilidad: {max_hab} con P = {probs[max_hab]}")
    print(f"-> Se esperaría encontrar la PC en: {max_hab}")

    crear_graficas(
        list(probs.keys()),
        list(probs.values())
    )


if __name__ == "__main__":
    main()

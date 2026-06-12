import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(autos, probs, consultas):
    out = carpeta_graficas(38)
    colores = []
    for a in autos:
        if a in [3, 4]:
            colores.append("#e74c3c")
        elif a < 8:
            colores.append("#f39c12")
        else:
            colores.append("#3498db")
    plt.bar(autos, probs, color=colores)
    plt.xlabel("Número de autos")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.67 — Distribución de servicio del mecánico")
    for i, (a, p) in enumerate(zip(autos, probs)):
        plt.text(i, p + 0.005, f"{p:.2f}", ha="center")
    guardar_figura(out, "mecanico_servicio")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.67
Considere la situación del ejemplo 2.32 (página 58).
Las probabilidades de que un mecánico automotriz dé servicio
a 3, 4, 5, 6, 7, 8 o más vehículos en un día de trabajo
dado son 0.12, 0.19, 0.28, 0.24, 0.10 y 0.07,
respectivamente.

a) ¿Cuál es la probabilidad de que el número de automóviles
   no sea mayor de 4?
b) ¿Cuál es la probabilidad de que dé servicio a menos de
   8 automóviles?
c) ¿Cuál es la probabilidad de que dé servicio a 3 o 4
   automóviles?
=========================================================
"""
    print(enunciado)

    autos = [3, 4, 5, 6, 7, "8+"]
    probs = [0.12, 0.19, 0.28, 0.24, 0.10, 0.07]

    total = sum(probs)
    print(f"-> Verificación de suma total: {total:.2f}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: 'No mayor de 4' significa ≤ 4, es decir, 3 o 4 autos. Sumamos sus probabilidades.")
    p_menor_igual_4 = probs[0] + probs[1]
    print(f"-> P(≤ 4) = P(3) + P(4) = {probs[0]} + {probs[1]} = {p_menor_igual_4}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Menos de 8' incluye 3, 4, 5, 6 y 7 autos.")
    p_menos_8 = sum(probs[:5])
    detalle = " + ".join(str(p) for p in probs[:5])
    print(f"-> P(< 8) = {detalle} = {p_menos_8}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: '3 o 4 autos' es la suma directa de sus probabilidades (mismo resultado que el inciso a).")
    p_3_o_4 = probs[0] + probs[1]
    print(f"-> P(3 o 4) = P(3) + P(4) = {probs[0]} + {probs[1]} = {p_3_o_4}")

    crear_graficas(autos, probs, [p_menor_igual_4, p_menos_8, p_3_o_4])


if __name__ == "__main__":
    main()

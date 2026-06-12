import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(aseveraciones, valores, correctos):
    out = carpeta_graficas(20)
    x = range(len(aseveraciones))
    ancho = 0.35
    plt.bar([i - ancho/2 for i in x], valores, ancho, label="Valores dados", color="#e74c3c")
    plt.bar([i + ancho/2 for i in x], correctos, ancho, label="Valores correctos", color="#2ecc71")
    plt.xticks(x, aseveraciones, fontsize=8)
    plt.ylabel("Suma de probabilidades")
    plt.title("Ejercicio 2.49 — Errores en aseveraciones")
    plt.legend()
    guardar_figura(out, "errores_aseveraciones")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.49
Encuentre los errores en cada una de las siguientes
aseveraciones:

a) Las probabilidades de que un vendedor de automóviles
   venda 0, 1, 2 o 3 unidades en un día dado de febrero
   son 0.19, 0.38, 0.29 y 0.15, respectivamente.

b) La probabilidad de que llueva mañana es 0.40 y la
   probabilidad de que no llueva es 0.52.

c) Las probabilidades de que una impresora cometa
   0, 1, 2, 3 o 4 o más errores al imprimir un documento
   son 0.19, 0.34, -0.25, 0.43 y 0.29, respectivamente.

d) Al sacar una carta de una baraja en un solo intento
   la probabilidad de seleccionar un corazón es 1/4, la
   probabilidad de seleccionar una carta negra es 1/2, y
   la probabilidad de seleccionar una carta negra es 1/8.
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: La suma de las probabilidades de todos los resultados posibles debe ser exactamente 1.")
    suma_a = 0.19 + 0.38 + 0.29 + 0.15
    print(f"-> Suma = 0.19 + 0.38 + 0.29 + 0.15 = {suma_a}")
    if suma_a != 1:
        print(f"-> ERROR: La suma es {suma_a} ≠ 1. Las probabilidades no son válidas.\n")
    else:
        print("-> Las probabilidades son válidas.\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: P(llueva) + P(no llueva) debe ser 1, pues son eventos complementarios.")
    suma_b = 0.40 + 0.52
    print(f"-> Suma = 0.40 + 0.52 = {suma_b}")
    print(f"-> ERROR: La suma es {suma_b} ≠ 1. Además, es imposible que P(no llueva) = 0.52 si P(llueva) = 0.40, ya que son complementos.\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Ninguna probabilidad puede ser negativa.")
    valores_c = [0.19, 0.34, -0.25, 0.43, 0.29]
    print(f"-> Valores dados: {valores_c}")
    print(f"-> ERROR: La probabilidad -0.25 es negativa, lo cual es imposible (axioma de no negatividad).\n")

    print("--- SOLUCIÓN d) ---")
    print("Explicación: En una baraja estándar de 52 cartas hay 13 corazones (P=13/52=1/4), 26 cartas negras (P=26/52=1/2) y 13 diamantes (P=13/52=1/4).")
    print("El enunciado repite 'carta negra' dos veces con valores 1/2 y 1/8, lo cual es inconsistente.")
    print("Además, P(corazón) + P(negra) + P(negra otra vez) = 1/4 + 1/2 + 1/8 = 2/8 + 4/8 + 1/8 = 7/8 ≠ 1.")
    print("La tercera probabilidad debería referirse a diamantes (carta roja no corazón), con valor 1/4, no 1/8.")
    print("-> ERROR: La tercera aseveración repite 'carta negra' y da un valor incorrecto de 1/8.\n")

    crear_graficas(
        ["a) Vendedor", "b) Lluvia", "c) Impresora", "d) Cartas"],
        [suma_a, suma_b, sum(valores_c), 1/4 + 1/2 + 1/8],
        [1, 1, 1, 1]
    )


if __name__ == "__main__":
    main()

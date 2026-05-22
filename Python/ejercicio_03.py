import math

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(total_codigos, codigos_diferentes, codigos_pares):
    out = carpeta_graficas(3)
    categorias = ["Todos los códigos", "Dígitos distintos", "Terminan en par"]
    valores = [total_codigos, codigos_diferentes, codigos_pares]
    plt.bar(categorias, valores, color=["#34495e", "#1abc9c", "#f39c12"])
    plt.ylabel("Cantidad de códigos")
    plt.title("Conteo de códigos de 4 dígitos")
    plt.xticks(rotation=15, ha="right")
    guardar_figura(out, "conteo_codigos")

    plt.figure()
    probs = [v / total_codigos for v in valores[1:]]
    plt.bar(
        ["Dígitos distintos", "Terminan en par"],
        probs,
        color=["#1abc9c", "#f39c12"],
    )
    plt.ylabel("Probabilidad")
    plt.ylim(0, 1)
    plt.title("Probabilidades solicitadas")
    guardar_figura(out, "probabilidades")


def main():
    enunciado = """
=========================================================
EJERCICIO 3
Un código de acceso consta de 4 dígitos (del 0 al 9) que pueden repetirse.
a) ¿Cuántos códigos diferentes son posibles?
b) ¿Cuál es la probabilidad de que un código elegido al azar tenga todos sus dígitos diferentes?
c) ¿Cuál es la probabilidad de que el código termine en un número par?
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Al tener 4 posiciones y 10 posibles dígitos por posición (0-9) con repetición permitida, por el principio multiplicativo tenemos 10^4 combinaciones.")
    total_codigos = 10 ** 4
    print(f"-> Códigos diferentes posibles: {total_codigos}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Si todos los dígitos deben ser diferentes, buscamos permutaciones sin repetición de 10 elementos elegidos de a 4: P(10,4).")
    codigos_diferentes = math.perm(10, 4)
    prob_diferentes = codigos_diferentes / total_codigos
    print(f"-> Códigos sin repetición: {codigos_diferentes}")
    print(f"-> Probabilidad = {codigos_diferentes} / {total_codigos} = {prob_diferentes:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Para terminar en par, la última posición solo tiene 5 opciones posibles (0, 2, 4, 6, 8). Las primeras 3 posiciones tienen 10 opciones cada una (10*10*10*5).")
    codigos_pares = (10 ** 3) * 5
    prob_pares = codigos_pares / total_codigos
    print(f"-> Códigos que terminan en par: {codigos_pares}")
    print(f"-> Probabilidad = {codigos_pares} / {total_codigos} = {prob_pares:.4f}")

    crear_graficas(total_codigos, codigos_diferentes, codigos_pares)


if __name__ == "__main__":
    main()

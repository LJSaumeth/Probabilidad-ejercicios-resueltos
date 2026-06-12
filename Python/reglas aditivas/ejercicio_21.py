import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(espacio, A, C, interseccion):
    out = carpeta_graficas(21)
    categorias = ["Espacio muestral |S|", "Evento A", "Evento C", "A ∩ C"]
    tamanos = [espacio, A, C, interseccion]
    colores = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12"]
    plt.bar(categorias, tamanos, color=colores)
    plt.ylabel("Número de elementos")
    plt.title("Ejercicio 2.50 — Conjuntos del experimento")
    for i, v in enumerate(tamanos):
        plt.text(i, v + 0.3, str(v), ha="center", fontweight="bold")
    guardar_figura(out, "conjuntos")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.50
Suponga que todos los elementos de S en el ejercicio 2.8
de la página 42 tienen la misma probabilidad de ocurrencia
y calcule:

a) la probabilidad del evento A;
b) la probabilidad del evento C;
c) la probabilidad del evento A ∩ C.

[Nota: El ejercicio 2.8 define S = {0, 1, 2, ..., 9},
A = {0, 2, 4, 6, 8} (números pares) y
C = {0, 1, 2, 3, 4, 5}.]
=========================================================
"""
    print(enunciado)

    S = set(range(10))
    A = {0, 2, 4, 6, 8}
    C = {0, 1, 2, 3, 4, 5}
    total = len(S)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Si todos los elementos son equiprobables, P(A) = |A| / |S| (regla de Laplace).")
    prob_A = len(A) / total
    print(f"-> A = {A}")
    print(f"-> |A| = {len(A)}, |S| = {total}")
    print(f"-> P(A) = {len(A)} / {total} = {prob_A:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    prob_C = len(C) / total
    print(f"-> C = {C}")
    print(f"-> |C| = {len(C)}")
    print(f"-> P(C) = {len(C)} / {total} = {prob_C:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    A_int_C = A & C
    prob_int = len(A_int_C) / total
    print(f"-> A ∩ C = {A_int_C}")
    print(f"-> |A ∩ C| = {len(A_int_C)}")
    print(f"-> P(A ∩ C) = {len(A_int_C)} / {total} = {prob_int:.4f}")

    crear_graficas(total, len(A), len(C), len(A_int_C))


if __name__ == "__main__":
    main()

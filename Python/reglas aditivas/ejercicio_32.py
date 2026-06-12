import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(32)
    plt.bar(etiquetas, valores, color=["#3498db", "#e74c3c", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.61 — Estudiantes: Matemáticas e Historia")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01, f"{v:.3f}", ha="center")
    guardar_figura(out, "estudiantes_mate_historia")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.61
En un grupo de 100 estudiantes graduados de preparatoria,
54 estudiaron matemáticas, 69 estudiaron historia y 35
cursaron matemáticas e historia. Si se selecciona al azar
uno de estos estudiantes, calcule la probabilidad de que:

a) el estudiante haya cursado matemáticas o historia;
b) el estudiante no haya llevado ninguna de estas materias;
c) el estudiante haya cursado historia pero no matemáticas.
=========================================================
"""
    print(enunciado)

    total = 100
    M = 54
    H = 69
    M_int_H = 35

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Usamos la regla aditiva: P(M ∪ H) = P(M) + P(H) − P(M ∩ H)")
    union = M + H - M_int_H
    p_union = union / total
    print(f"-> |M ∪ H| = {M} + {H} − {M_int_H} = {union}")
    print(f"-> P(M ∪ H) = {union} / {total} = {p_union:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: 'Ninguna materia' = complemento de la unión.")
    ninguno = total - union
    p_ninguno = ninguno / total
    print(f"-> |Ninguna| = {total} − {union} = {ninguno}")
    print(f"-> P(ninguna) = {ninguno} / {total} = {p_ninguno:.4f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: 'Historia pero no matemáticas' = H − (M ∩ H).")
    solo_H = H - M_int_H
    p_solo_H = solo_H / total
    print(f"-> |H − M| = {H} − {M_int_H} = {solo_H}")
    print(f"-> P(historia pero no matemáticas) = {solo_H} / {total} = {p_solo_H:.4f}")

    crear_graficas(
        ["a) M ∪ H", "b) Ninguna", "c) Solo Historia"],
        [p_union, p_ninguno, p_solo_H]
    )


if __name__ == "__main__":
    main()

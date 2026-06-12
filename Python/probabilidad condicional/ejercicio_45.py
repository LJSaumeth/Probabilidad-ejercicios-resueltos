import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(distribucion, prob_cond):
    out = carpeta_graficas(45)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    categorias = list(distribucion.keys())
    valores = list(distribucion.values())
    ax1.bar(categorias, valores, color=["#3498db", "#e74c3c", "#2ecc71"])
    ax1.set_ylabel("Número de estudiantes")
    ax1.set_title("Distribución de estudiantes")
    for i, v in enumerate(valores):
        ax1.text(i, v + 0.5, str(v), ha="center")

    ax2.bar(["P(último año | calif. 10)"], [prob_cond], color="#f39c12")
    ax2.set_ylabel("Probabilidad")
    ax2.set_title("Probabilidad condicional")
    ax2.text(0, prob_cond / 2, f"{prob_cond:.4f}", ha="center", fontsize=14)

    plt.suptitle("Ejercicio 2.74 — Estudiantes de física")
    guardar_figura(out, "estudiantes_fisica")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.74
Un grupo de estudiantes de física avanzada se compone de
10 de primer año, 30 de último año y 10 graduados. Las
calificaciones finales muestran que 3 de primer año, 10 de
último año y 5 graduados obtuvieron 10. Si se elige un
estudiante al azar y se descubre que obtuvo 10, ¿cuál es
la probabilidad de que sea de último año?
=========================================================
"""
    print(enunciado)

    total = 10 + 30 + 10
    diez_primero = 3
    diez_ultimo = 10
    diez_graduado = 5
    total_diez = diez_primero + diez_ultimo + diez_graduado

    print("--- SOLUCIÓN ---")
    print("Explicación: Usamos la probabilidad condicional P(último año | calificación 10).")
    print("P(último | 10) = P(último ∩ 10) / P(10)")
    print()
    print(f"-> Total de estudiantes: {total}")
    print(f"-> Estudiantes con 10: {diez_primero} + {diez_ultimo} + {diez_graduado} = {total_diez}")
    print(f"-> De último año con 10: {diez_ultimo}")
    print()
    prob_cond = diez_ultimo / total_diez
    print(f"-> P(último año | 10) = {diez_ultimo} / {total_diez} = {prob_cond:.4f}")

    crear_graficas(
        {"Primer año": 10, "Último año": 30, "Graduados": 10},
        prob_cond
    )


if __name__ == "__main__":
    main()

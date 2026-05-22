import graficas_util  # noqa: F401

import matplotlib.pyplot as plt
import numpy as np

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas():
    out = carpeta_graficas(4)
    carreras = ["Ing. Datos", "Ing. Sistemas", "Otras"]
    p_carrera = [0.60, 0.30, 0.10]
    p_tp = [0.40, 0.50, 0.20]
    x = np.arange(len(carreras))
    ancho = 0.35
    fig, ax = plt.subplots()
    ax.bar(x - ancho / 2, p_carrera, ancho, label="P(carrera)", color="#3498db")
    ax.bar(x + ancho / 2, p_tp, ancho, label="P(TP | carrera)", color="#e67e22")
    ax.set_xticks(x)
    ax.set_xticklabels(carreras)
    ax.set_ylabel("Probabilidad")
    ax.set_title("Probabilidad total y condicional de transporte público")
    ax.legend()
    ax.set_ylim(0, 1)
    guardar_figura(out, "carreras_y_transporte")

    contrib = [a * b for a, b in zip(p_carrera, p_tp)]
    plt.figure()
    plt.bar(carreras, contrib, color=["#2980b9", "#27ae60", "#8e44ad"])
    plt.ylabel("P(carrera ∩ TP)")
    plt.title("Contribución de cada carrera a P(TP)")
    guardar_figura(out, "contribucion_tp")


def main():
    enunciado = """
=========================================================
EJERCICIO 4
En una facultad, el 60% de los estudiantes estudia Ingeniería de Datos, el 30% Ingeniería de Sistemas y el resto otra carrera.
El 40% de los de Ing. de Datos usa transporte público (TP), el 50% de Sistemas lo usa y el 20% de otras carreras lo usa.
a) Si se selecciona un estudiante al azar, ¿cuál es la probabilidad de que use transporte público?
b) ¿Cuál es la probabilidad de que sea de Ingeniería de Datos dado que usa transporte público?
=========================================================
"""
    print(enunciado)

    p_datos = 0.60
    p_sistemas = 0.30
    p_otras = 0.10  # 1 - 0.60 - 0.30

    p_tp_dado_datos = 0.40
    p_tp_dado_sistemas = 0.50
    p_tp_dado_otras = 0.20

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Utilizamos el Teorema de la Probabilidad Total. Multiplicamos la probabilidad de cada carrera por su respectiva probabilidad de usar TP y sumamos.")
    p_tp = (p_datos * p_tp_dado_datos) + (p_sistemas * p_tp_dado_sistemas) + (p_otras * p_tp_dado_otras)
    print(f"-> P(TP) = (0.60 * 0.40) + (0.30 * 0.50) + (0.10 * 0.20) = {p_tp:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Usamos el Teorema de Bayes para calcular P(Datos | TP). Es la probabilidad de la rama de Ing. de Datos dividida entre la Probabilidad Total de usar TP calculada en a).")
    p_datos_dado_tp = (p_datos * p_tp_dado_datos) / p_tp
    print(f"-> P(Datos|TP) = P(Datos y TP) / P(TP) = {(p_datos * p_tp_dado_datos):.4f} / {p_tp:.4f} = {p_datos_dado_tp:.4f}")

    crear_graficas()


if __name__ == "__main__":
    main()

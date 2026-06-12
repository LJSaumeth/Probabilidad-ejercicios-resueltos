import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob):
    out = carpeta_graficas(56)
    plt.bar(["P(Diagnóstico incorrecto y demanda)"], [prob], color="#e74c3c")
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.85 — Diagnóstico médico")
    plt.text(0, prob / 2, f"{prob:.2f}", ha="center", fontsize=14, fontweight="bold")
    guardar_figura(out, "diagnostico_medico")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.85
La probabilidad de que un doctor diagnostique correctamente
una enfermedad es 0.7. Dado que el doctor hace un
diagnóstico incorrecto, la probabilidad de que el paciente
entable una demanda legal es 0.9. ¿Cuál es la probabilidad
de que el doctor haga un diagnóstico incorrecto y el
paciente lo demande?
=========================================================
"""
    print(enunciado)

    P_correcto = 0.7
    P_incorrecto = 1 - P_correcto
    P_demanda_dado_incorrecto = 0.9

    print("--- SOLUCIÓN ---")
    print("Explicación: Usamos la regla de la multiplicación:")
    print("P(Incorrecto ∩ Demanda) = P(Incorrecto) × P(Demanda | Incorrecto)")
    prob = P_incorrecto * P_demanda_dado_incorrecto
    print(f"-> P(Incorrecto) = 1 − {P_correcto} = {P_incorrecto}")
    print(f"-> P(Demanda | Incorrecto) = {P_demanda_dado_incorrecto}")
    print(f"-> P(Incorrecto ∩ Demanda) = {P_incorrecto} × {P_demanda_dado_incorrecto} = {prob}")

    crear_graficas(prob)


if __name__ == "__main__":
    main()

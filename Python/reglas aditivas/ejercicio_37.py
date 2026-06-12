import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
import numpy as np
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(turnos, inseguras, humanas):
    out = carpeta_graficas(37)
    x = np.arange(len(turnos))
    ancho = 0.35
    plt.bar(x - ancho/2, inseguras, ancho, label="Condiciones inseguras", color="#e74c3c")
    plt.bar(x + ancho/2, humanas, ancho, label="Fallas humanas", color="#3498db")
    plt.xticks(x, turnos)
    plt.ylabel("Porcentaje de accidentes")
    plt.title("Ejercicio 2.66 — Accidentes por turno y causa")
    plt.legend()
    guardar_figura(out, "accidentes_fabrica")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.66
A los obreros se les motiva a practicar tolerancia cero.
El año pasado ocurrieron 300 accidentes. Los porcentajes
por la combinación de condiciones son:

| Turno     | Condiciones inseguras | Fallas humanas |
|-----------|----------------------|----------------|
| Matutino  | 5%                   | 32%            |
| Vespertino| 6%                   | 25%            |
| Nocturno  | 2%                   | 30%            |

Si se elige aleatoriamente un reporte de entre los 300:

a) P(accidente en turno nocturno)
b) P(accidente por falla humana)
c) P(accidente por condiciones inseguras)
d) P(accidente en turno vespertino o nocturno)
=========================================================
"""
    print(enunciado)

    p_mat_inseg = 0.05
    p_mat_hum = 0.32
    p_vesp_inseg = 0.06
    p_vesp_hum = 0.25
    p_noc_inseg = 0.02
    p_noc_hum = 0.30

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Sumamos los porcentajes del turno nocturno (condiciones inseguras + fallas humanas).")
    p_nocturno = p_noc_inseg + p_noc_hum
    print(f"-> P(nocturno) = {p_noc_inseg} + {p_noc_hum} = {p_nocturno}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Sumamos los porcentajes de fallas humanas de todos los turnos.")
    p_falla_humana = p_mat_hum + p_vesp_hum + p_noc_hum
    print(f"-> P(falla humana) = {p_mat_hum} + {p_vesp_hum} + {p_noc_hum} = {p_falla_humana}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Sumamos los porcentajes de condiciones inseguras de todos los turnos.")
    p_inseguras = p_mat_inseg + p_vesp_inseg + p_noc_inseg
    print(f"-> P(inseguras) = {p_mat_inseg} + {p_vesp_inseg} + {p_noc_inseg} = {p_inseguras}\n")

    print("--- SOLUCIÓN d) ---")
    print("Explicación: Sumamos los porcentajes totales de los turnos vespertino y nocturno (eventos mutuamente excluyentes).")
    p_vespertino = p_vesp_inseg + p_vesp_hum
    p_vesp_o_noc = p_vespertino + p_nocturno
    print(f"-> P(vespertino) = {p_vesp_inseg} + {p_vesp_hum} = {p_vespertino}")
    print(f"-> P(nocturno) = {p_nocturno}")
    print(f"-> P(vespertino o nocturno) = {p_vespertino} + {p_nocturno} = {p_vesp_o_noc}")

    crear_graficas(
        ["Matutino", "Vespertino", "Nocturno"],
        [p_mat_inseg, p_vesp_inseg, p_noc_inseg],
        [p_mat_hum, p_vesp_hum, p_noc_hum]
    )


if __name__ == "__main__":
    main()

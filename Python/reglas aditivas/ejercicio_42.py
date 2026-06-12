import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(42)
    plt.bar(etiquetas, valores, color=["#2ecc71", "#e74c3c", "#f39c12", "#3498db"])
    plt.ylabel("Probabilidad / Dólares")
    plt.title("Ejercicio 2.71 — Control de calidad (peso)")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.01 if v < 1 else v + 1000, f"{v:.4f}" if v < 1 else f"${v:,.0f}", ha="center")
    guardar_figura(out, "control_calidad_peso")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.71
Los procedimientos estadísticos se usan para control de
calidad de peso de productos empacados. Datos históricos:
P(cumplir especificaciones) = 0.95, P(demasiado ligero) = 0.002.
Costo de producción: $20.00. Precio de venta: $25.00.

a) ¿Cuál es la probabilidad de que un paquete sea demasiado
   pesado?
b) Si todos los paquetes cumplen especificaciones, ¿qué
   utilidad por 10,000 paquetes?
c) Si los paquetes defectuosos se rechazan y pierden su
   valor, ¿a cuánto se reduce la utilidad de 10,000 paquetes?
=========================================================
"""
    print(enunciado)

    P_cumple = 0.95
    P_ligero = 0.002
    n_paquetes = 10000
    costo = 20.00
    precio = 25.00

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Los eventos 'cumple', 'ligero' y 'pesado' son mutuamente excluyentes y exhaustivos.")
    P_pesado = 1 - P_cumple - P_ligero
    print(f"-> P(pesado) = 1 − P(cumple) − P(ligero) = 1 − {P_cumple} − {P_ligero} = {P_pesado}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Utilidad = ingresos − costos. Todos se venden a $25 y cuestan $20.")
    utilidad_ideal = n_paquetes * (precio - costo)
    print(f"-> Utilidad = {n_paquetes} × (${precio} − ${costo}) = {n_paquetes} × $5.00 = ${utilidad_ideal:,.2f}\n")

    print("--- SOLUCIÓN c) ---")
    print("Explicación: Los defectuosos (ligeros + pesados) no generan ingresos pero sí costaron producirlos.")
    P_defectuoso = P_ligero + P_pesado
    defectuosos_esperados = n_paquetes * P_defectuoso
    ingresos_reales = (n_paquetes - defectuosos_esperados) * precio
    utilidad_real = ingresos_reales - n_paquetes * costo
    reduccion = utilidad_ideal - utilidad_real
    print(f"-> P(defectuoso) = {P_ligero} + {P_pesado} = {P_defectuoso}")
    print(f"-> Paquetes defectuosos esperados: {n_paquetes} × {P_defectuoso} = {defectuosos_esperados:.0f}")
    print(f"-> Ingresos reales:  ({n_paquetes} − {defectuosos_esperados:.0f}) × ${precio} = ${ingresos_reales:,.2f}")
    print(f"-> Costos totales:   {n_paquetes} × ${costo} = ${n_paquetes * costo:,.2f}")
    print(f"-> Utilidad real:    ${utilidad_real:,.2f}")
    print(f"-> Reducción:        ${utilidad_ideal:,.2f} − ${utilidad_real:,.2f} = ${reduccion:,.2f}")

    crear_graficas(
        ["P(Cumple)", "P(Ligero)", "P(Pesado)", f"Utilidad ideal"],
        [P_cumple, P_ligero, P_pesado, utilidad_ideal]
    )


if __name__ == "__main__":
    main()

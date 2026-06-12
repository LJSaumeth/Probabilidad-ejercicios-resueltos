import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(etiquetas, valores):
    out = carpeta_graficas(41)
    plt.bar(etiquetas, valores, color=["#2ecc71", "#e74c3c"])
    plt.ylabel("Dólares ($)")
    plt.title("Ejercicio 2.70 — Utilidad semanal de detergente")
    for i, v in enumerate(valores):
        plt.text(i, v + 200, f"${v:,.2f}", ha="center")
    guardar_figura(out, "utilidad_detergente")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.70
Considere la situación del ejercicio 2.69. Suponga que se
producen 50,000 cajas de detergente por semana. Los clientes
devuelven las cajas insuficientemente llenas y solicitan
reembolso. Costo de producción por caja: $4.00. Precio de
venta: $4.50.

a) ¿Cuál es la utilidad semanal cuando no hay devoluciones?
b) ¿Cuál es la pérdida en utilidades esperada debido a la
   devolución de cajas insuficientemente llenadas?
=========================================================
"""
    print(enunciado)

    produccion = 50000
    costo_unitario = 4.00
    precio_venta = 4.50
    P_insuficiente = 0.001

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Sin devoluciones, todas las cajas se venden. Utilidad = ingresos − costos.")
    utilidad_sin_devol = produccion * (precio_venta - costo_unitario)
    print(f"-> Ingresos:  {produccion} × ${precio_venta} = ${produccion * precio_venta:,.2f}")
    print(f"-> Costos:    {produccion} × ${costo_unitario} = ${produccion * costo_unitario:,.2f}")
    print(f"-> Utilidad:  {produccion} × ${precio_venta - costo_unitario} = ${utilidad_sin_devol:,.2f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Las cajas devueltas generan costo de producción pero no ingreso (se reembolsa al cliente).")
    print("La pérdida por cada caja devuelta es el precio de venta (ingreso perdido) pues el costo ya se incurrió de todas formas.")
    esperadas_devueltas = produccion * P_insuficiente
    perdida_esperada = esperadas_devueltas * precio_venta
    utilidad_con_dev = utilidad_sin_devol - perdida_esperada
    print(f"-> Cajas devueltas esperadas:  {produccion} × {P_insuficiente} = {esperadas_devueltas:.0f}")
    print(f"-> Pérdida esperada:           {esperadas_devueltas:.0f} × ${precio_venta} = ${perdida_esperada:,.2f}")
    print(f"-> Utilidad esperada (con devoluciones): ${utilidad_con_dev:,.2f}")

    crear_graficas(
        ["Utilidad sin devoluciones", "Pérdida esperada"],
        [utilidad_sin_devol, perdida_esperada]
    )


if __name__ == "__main__":
    main()

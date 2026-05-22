import itertools

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(espacio_muestral):
    out = carpeta_graficas(1)
    conteos = {0: 0, 1: 0, 2: 0, 3: 0}
    for resultado in espacio_muestral:
        conteos[resultado.count("C")] += 1
    etiquetas = [f"{k} caras" for k in conteos]
    plt.bar(etiquetas, list(conteos.values()), color=["#4c72b0", "#55a868", "#c44e52", "#8172b2"])
    plt.ylabel("Número de resultados")
    plt.title("Distribución del número de caras (3 monedas)")
    guardar_figura(out, "distribucion_caras")


def main():
    enunciado = """
=========================================================
EJERCICIO 1
Se lanzan tres monedas justas al aire.
a) Determine el espacio muestral del experimento.
b) ¿Cuál es la probabilidad de obtener exactamente dos caras?
c) ¿Cuál es la probabilidad de obtener al menos una cruz?
=========================================================
"""
    print(enunciado)

    # a) Espacio muestral
    print("--- SOLUCIÓN a) ---")
    print("Explicación: El espacio muestral de lanzar 3 monedas se obtiene combinando los resultados posibles (Cara 'C' o Cruz 'X') para cada una de las 3 posiciones.")
    moneda = ['C', 'X']
    espacio_muestral = list(itertools.product(moneda, repeat=3))
    print(f"-> Espacio muestral: {espacio_muestral}")
    print(f"-> Tamaño del espacio muestral: {len(espacio_muestral)}\n")

    # b) Probabilidad de obtener exactamente dos caras
    print("--- SOLUCIÓN b) ---")
    print("Explicación: Buscamos los eventos donde la 'C' aparece exactamente 2 veces. La probabilidad es la regla de Laplace (Casos Favorables / Casos Totales).")
    dos_caras = [resultado for resultado in espacio_muestral if resultado.count('C') == 2]
    prob_dos_caras = len(dos_caras) / len(espacio_muestral)
    print(f"-> Eventos favorables (exactamente 2 caras): {dos_caras}")
    print(f"-> Probabilidad = {len(dos_caras)} / {len(espacio_muestral)} = {prob_dos_caras:.4f}\n")

    # c) Probabilidad de obtener al menos una cruz
    print("--- SOLUCIÓN c) ---")
    print("Explicación: Buscamos eventos donde la 'X' aparece 1 o más veces. Esto es igual a decir que el resultado no sean todo caras (C,C,C).")
    al_menos_una_cruz = [resultado for resultado in espacio_muestral if resultado.count('X') >= 1]
    prob_al_menos_una_cruz = len(al_menos_una_cruz) / len(espacio_muestral)
    print(f"-> Probabilidad = {len(al_menos_una_cruz)} / {len(espacio_muestral)} = {prob_al_menos_una_cruz:.4f}")

    crear_graficas(espacio_muestral)


if __name__ == "__main__":
    main()

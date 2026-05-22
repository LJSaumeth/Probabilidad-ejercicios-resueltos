import math

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(N, K, n):
    out = carpeta_graficas(15)
    x_vals = list(range(min(n, K) + 1))
    probs = []
    for x in x_vals:
        if n - x <= N - K:
            probs.append(
                (math.comb(K, x) * math.comb(N - K, n - x)) / math.comb(N, n)
            )
        else:
            probs.append(0)
    plt.bar([str(x) for x in x_vals], probs, color="#1abc9c")
    plt.xlabel("Defectuosos en la muestra")
    plt.ylabel("P(X = x)")
    plt.title(f"Hipergeométrica (N={N}, K={K}, n={n})")
    guardar_figura(out, "hipergeometrica_pmf")


def main():
    enunciado = """
=========================================================
EJERCICIO 15
En una caja hay 12 bombillos, de los cuales 4 están defectuosos. 
Se seleccionan 5 bombillos al azar sin reemplazo.
a) ¿Cuál es la probabilidad de que exactamente 2 estén defectuosos?
b) ¿Cuál es el número esperado de bombillos defectuosos en la muestra?
=========================================================
"""
    print(enunciado)

    N = 12  # Tamaño total de la población (bombillos)
    K = 4   # Elementos con la característica deseada (defectuosos)
    n = 5   # Tamaño de la muestra (seleccionados)
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Al ser un muestreo sin reemplazo desde una población finita, usamos la Distribución Hipergeométrica.")
    print("Fórmula: P(X=x) = [ C(K, x) * C(N-K, n-x) ] / C(N, n).")
    print("Calculamos combinaciones de sacar 2 de 4 defectuosos, por las combinaciones de sacar 3 de 8 no defectuosos, todo sobre formas de sacar 5 de 12 totales.")
    x = 2
    formas_defectuosos = math.comb(K, x)
    formas_buenos = math.comb(N - K, n - x)
    formas_totales = math.comb(N, n)
    
    prob_2_def = (formas_defectuosos * formas_buenos) / formas_totales
    print(f"-> Formas de sacar 2 defectuosos (4C2): {formas_defectuosos}")
    print(f"-> Formas de sacar 3 buenos (8C3): {formas_buenos}")
    print(f"-> Formas totales de sacar 5 (12C5): {formas_totales}")
    print(f"-> Probabilidad de exactamente 2 defectuosos: {prob_2_def:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: El valor esperado (media) para una distribución Hipergeométrica es E[X] = n * (K / N).")
    esperado = n * (K / N)
    print(f"-> Número esperado de defectuosos (Media) = {n} * ({K}/{N}) = {esperado:.4f}")

    crear_graficas(N, K, n)


if __name__ == "__main__":
    main()

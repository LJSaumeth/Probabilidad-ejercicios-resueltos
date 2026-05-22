import math

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(r, p, k_max=25):
    out = carpeta_graficas(14)
    k_vals = list(range(r, k_max + 1))
    probs = [
        math.comb(k - 1, r - 1) * (p**r) * ((1 - p) ** (k - r)) for k in k_vals
    ]
    plt.bar([str(k) for k in k_vals], probs, color="#9b59b6")
    plt.xlabel("Número de clientes k")
    plt.ylabel("P(X = k)")
    plt.title(f"Binomial negativa (r={r}, p={p})")
    guardar_figura(out, "binomial_negativa_pmf")


def main():
    enunciado = """
=========================================================
EJERCICIO 14
La probabilidad de que un cliente compre un producto en una tienda en línea es 0.3. 
Se observan los clientes hasta encontrar el quinto que compra.
a) ¿Cuál es la probabilidad de que se necesiten exactamente 10 clientes?
b) ¿Cuál es el número esperado de clientes que se deben observar?
=========================================================
"""
    print(enunciado)

    r = 5  # Número de éxitos objetivo (quinto que compra)
    p = 0.3  # Probabilidad de éxito (comprar)
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Esta es una Distribución Binomial Negativa. Queremos saber la probabilidad de necesitar 'k' intentos totales para obtener 'r' éxitos.")
    print("Para que el éxito número 5 ocurra exactamente en el cliente 10, debe haber exactamente 4 éxitos en los primeros 9 clientes, y que el 10mo sea un éxito obligatoriamente.")
    print("Fórmula: C(k-1, r-1) * p^r * (1-p)^(k-r).")
    k = 10
    prob_10 = math.comb(k - 1, r - 1) * (p ** r) * ((1 - p) ** (k - r))
    print(f"-> Combinaciones de 4 éxitos en 9 intentos (9C4): {math.comb(k - 1, r - 1)}")
    print(f"-> Probabilidad de que se necesiten exactamente 10 clientes: {prob_10:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: En la parametrización de número total de intentos, el valor esperado o media de la Binomial Negativa es E[X] = r / p.")
    esperado = r / p
    print(f"-> Número esperado de clientes a observar (Media): {r} / {p} = {esperado:.4f}")

    crear_graficas(r, p)


if __name__ == "__main__":
    main()

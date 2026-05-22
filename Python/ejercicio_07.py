import math

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(n, p):
    out = carpeta_graficas(7)
    k_vals = list(range(n + 1))
    probs = [math.comb(n, k) * (p**k) * ((1 - p) ** (n - k)) for k in k_vals]
    plt.bar([str(k) for k in k_vals], probs, color="#16a085")
    plt.xlabel("Piezas defectuosas (k)")
    plt.ylabel("P(X = k)")
    plt.title(f"Distribución binomial (n={n}, p={p})")
    guardar_figura(out, "binomial_pmf")


def main():
    enunciado = """
=========================================================
EJERCICIO 7
Una máquina produce piezas. La probabilidad de que una pieza sea defectuosa es 0.05. Se toman tres piezas al azar (con independencia).
a) Calcule la probabilidad de que exactamente una sea defectuosa.
b) Calcule la probabilidad de que al menos una sea defectuosa.
=========================================================
"""
    print(enunciado)

    n = 3
    p = 0.05
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Modelamos esto como una Distribución Binomial, con n=3 intentos y probabilidad de éxito p=0.05 (éxito es que sea defectuosa).")
    print("Aplicamos la fórmula de probabilidad Binomial para k=1: C(n, k) * p^k * (1-p)^(n-k).")
    k_a = 1
    prob_exactamente_una = math.comb(n, k_a) * (p ** k_a) * ((1 - p) ** (n - k_a))
    print(f"-> Probabilidad de exactamente 1 pieza defectuosa: {prob_exactamente_una:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: La probabilidad de 'al menos una' (k>=1) es igual a 1 menos la probabilidad de 'ninguna' (k=0).")
    print("Calculamos P(X=0) y se lo restamos a 1 para no tener que sumar las probabilidades de k=1, k=2 y k=3.")
    k_0 = 0
    prob_ninguna = math.comb(n, k_0) * (p ** k_0) * ((1 - p) ** (n - k_0))
    prob_al_menos_una = 1 - prob_ninguna
    print(f"-> Probabilidad de ninguna defectuosa P(X=0) = {prob_ninguna:.4f}")
    print(f"-> Probabilidad de al menos una P(X>=1) = 1 - {prob_ninguna:.4f} = {prob_al_menos_una:.4f}")

    crear_graficas(n, p)


if __name__ == "__main__":
    main()

import math

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def prob_poisson(lmbda, k):
    return math.exp(-lmbda) * (lmbda ** k) / math.factorial(k)

def crear_graficas(lmbda, nombre_archivo, k_max=12):
    out = carpeta_graficas(17)
    k_vals = list(range(k_max + 1))
    probs = [prob_poisson(lmbda, k) for k in k_vals]
    plt.bar([str(k) for k in k_vals], probs, color="#3498db")
    plt.xlabel("Llamadas k")
    plt.ylabel("P(X = k)")
    plt.title(f"Poisson (lambda={lmbda})")
    guardar_figura(out, nombre_archivo)


def main():
    enunciado = """
=========================================================
EJERCICIO 17
El número de llamadas que recibe un call center por minuto sigue una distribución de Poisson con media 4 llamadas por minuto.
a) ¿Cuál es la probabilidad de que en un minuto dado se reciban exactamente 3 llamadas?
b) ¿Cuál es la probabilidad de que en un minuto se reciban 2 o menos llamadas?
c) ¿Cuál es la probabilidad de que en 2 minutos se reciban al menos 10 llamadas?
=========================================================
"""
    print(enunciado)

    lmbda_1 = 4
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Usamos la Distribución de Poisson. La fórmula es P(X=k) = (e^(-λ) * λ^k) / k!.")
    print("Aquí λ=4 (media por minuto) y k=3 llamadas.")
    prob_3 = prob_poisson(lmbda_1, 3)
    print(f"-> Probabilidad de recibir exactamente 3 llamadas en 1 min: {prob_3:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para calcular '2 o menos llamadas' tenemos que sumar las probabilidades individuales de recibir 0, 1 y 2 llamadas.")
    prob_2_o_menos = sum(prob_poisson(lmbda_1, k) for k in range(3))
    print(f"-> P(X≤2) = P(X=0) + P(X=1) + P(X=2)")
    print(f"-> Probabilidad de recibir 2 o menos llamadas en 1 min: {prob_2_o_menos:.4f}\n")
    
    print("--- SOLUCIÓN c) ---")
    print("Explicación: Al duplicarse el intervalo de tiempo a 2 minutos, la media λ también se duplica: λ = 4 * 2 = 8 llamadas promedio.")
    print("Para calcular 'al menos 10 llamadas' P(X≥10), es más fácil usar el complemento: 1 - P(X≤9).")
    lmbda_2 = 8
    prob_9_o_menos = sum(prob_poisson(lmbda_2, k) for k in range(10))
    prob_al_menos_10 = 1 - prob_9_o_menos
    print(f"-> Nueva media (λ) para 2 min = 8")
    print(f"-> P(X≤9) = {prob_9_o_menos:.4f}")
    print(f"-> P(X≥10) = 1 - {prob_9_o_menos:.4f} = {prob_al_menos_10:.4f}")

    crear_graficas(lmbda_1, "poisson_1_min")
    crear_graficas(lmbda_2, "poisson_2_min", k_max=16)


if __name__ == "__main__":
    main()

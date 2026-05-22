import math

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(n, p):
    out = carpeta_graficas(12)
    k_vals = list(range(n + 1))
    probs = [math.comb(n, k) * (p**k) * ((1 - p) ** (n - k)) for k in k_vals]
    plt.bar([str(k) for k in k_vals], probs, color="#2ecc71")
    plt.xlabel("Aciertos k")
    plt.ylabel("P(X = k)")
    plt.title(f"Binomial (n={n}, p={p})")
    guardar_figura(out, "binomial_pmf")


def main():
    enunciado = """
=========================================================
EJERCICIO 12
Un examen tiene 10 preguntas de opción múltiple, cada una con 4 opciones (solo una correcta). 
Un estudiante responde al azar todas las preguntas.
a) ¿Cuál es la probabilidad de que acierte exactamente 6 preguntas?
b) ¿Cuál es la probabilidad de que acierte al menos 8 preguntas?
c) ¿Cuál es el número esperado de aciertos y su desviación estándar?
=========================================================
"""
    print(enunciado)

    n = 10  # número de preguntas
    p = 1/4 # probabilidad de acierto por pregunta (1 correcta de 4)
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Es una Distribución Binomial. Queremos exactamente k=6 aciertos. Fórmula: C(n, k) * p^k * (1-p)^(n-k).")
    k_a = 6
    prob_exact_6 = math.comb(n, k_a) * (p ** k_a) * ((1 - p) ** (n - k_a))
    print(f"-> Probabilidad de exactamente 6 aciertos: {prob_exact_6:.6f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para 'al menos 8 aciertos' P(X>=8), calculamos y sumamos las probabilidades individuales de k=8, k=9 y k=10.")
    prob_al_menos_8 = 0
    for k in range(8, 11):
        p_k = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        prob_al_menos_8 += p_k
        print(f"   - P(X={k}) = {p_k:.6f}")
    print(f"-> Probabilidad de al menos 8 aciertos: {prob_al_menos_8:.6f}\n")
    
    print("--- SOLUCIÓN c) ---")
    print("Explicación: En una Binomial, el número esperado (Media) es n * p. La varianza es n * p * (1-p) y la desviación estándar es la raíz cuadrada de esta.")
    media = n * p
    varianza = n * p * (1 - p)
    desviacion = math.sqrt(varianza)
    
    print(f"-> Número esperado de aciertos (Media) = 10 * 0.25 = {media:.4f}")
    print(f"-> Desviación estándar = {desviacion:.4f}")

    crear_graficas(n, p)


if __name__ == "__main__":
    main()

import math

def main():
    # Distribución Binomial
    n = 10  # número de preguntas
    p = 1/4 # probabilidad de acierto por pregunta
    
    # a) Probabilidad de que acierte exactamente 6 preguntas (k=6)
    k_a = 6
    prob_exact_6 = math.comb(n, k_a) * (p ** k_a) * ((1 - p) ** (n - k_a))
    print(f"a) Probabilidad de acertar exactamente 6 preguntas: {prob_exact_6:.6f}")
    
    # b) Probabilidad de que acierte al menos 8 preguntas P(X >= 8)
    # P(X >= 8) = P(X=8) + P(X=9) + P(X=10)
    prob_al_menos_8 = 0
    for k in range(8, 11):
        prob_al_menos_8 += math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    print(f"b) Probabilidad de acertar al menos 8 preguntas: {prob_al_menos_8:.6f}")
    
    # c) Número esperado de aciertos (Media) y desviación estándar
    # Media E[X] = n * p
    media = n * p
    
    # Varianza = n * p * (1 - p)
    varianza = n * p * (1 - p)
    # Desviación estándar = sqrt(Varianza)
    desviacion = math.sqrt(varianza)
    
    print(f"c) Número esperado de aciertos (Media): {media:.4f}")
    print(f"   Desviación estándar: {desviacion:.4f}")

if __name__ == "__main__":
    main()

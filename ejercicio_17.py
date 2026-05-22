import math

def prob_poisson(lmbda, k):
    """Calcula P(X = k) para una distribución de Poisson con media lmbda."""
    return math.exp(-lmbda) * (lmbda ** k) / math.factorial(k)

def main():
    # Distribución de Poisson
    # Media: 4 llamadas por minuto
    lmbda_1 = 4
    
    # a) Probabilidad de que en un minuto dado se reciban exactamente 3 llamadas (k=3)
    prob_3 = prob_poisson(lmbda_1, 3)
    print(f"a) Probabilidad de recibir exactamente 3 llamadas en 1 min: {prob_3:.4f}")
    
    # b) Probabilidad de que en un minuto se reciban 2 o menos llamadas P(X <= 2)
    # P(X <= 2) = P(X=0) + P(X=1) + P(X=2)
    prob_2_o_menos = sum(prob_poisson(lmbda_1, k) for k in range(3))
    print(f"b) Probabilidad de recibir 2 o menos llamadas en 1 min: {prob_2_o_menos:.4f}")
    
    # c) Probabilidad de que en 2 minutos se reciban al menos 10 llamadas P(X >= 10)
    # La nueva media (lambda) para 2 minutos es 4 * 2 = 8
    lmbda_2 = 8
    # P(X >= 10) = 1 - P(X <= 9)
    prob_9_o_menos = sum(prob_poisson(lmbda_2, k) for k in range(10))
    prob_al_menos_10 = 1 - prob_9_o_menos
    print(f"c) Probabilidad de recibir al menos 10 llamadas en 2 min (λ=8): {prob_al_menos_10:.4f}")

if __name__ == "__main__":
    main()

import math

def main():
    # Binomial
    n = 3
    p = 0.05
    
    # a) Probabilidad de que exactamente una sea defectuosa (k = 1)
    k_a = 1
    prob_exactamente_una = math.comb(n, k_a) * (p ** k_a) * ((1 - p) ** (n - k_a))
    print(f"a) Probabilidad de exactamente una pieza defectuosa: {prob_exactamente_una:.4f}")

    # b) Probabilidad de que al menos una sea defectuosa P(X >= 1)
    # Es más fácil calcular por el complemento: 1 - P(X = 0)
    k_0 = 0
    prob_ninguna = math.comb(n, k_0) * (p ** k_0) * ((1 - p) ** (n - k_0))
    prob_al_menos_una = 1 - prob_ninguna
    print(f"b) Probabilidad de al menos una pieza defectuosa: {prob_al_menos_una:.4f}")

if __name__ == "__main__":
    main()

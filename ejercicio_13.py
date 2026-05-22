import math

def coef_multinomial(n, k_lista):
    """Calcula el coeficiente multinomial n! / (k1! * k2! * ...)"""
    coef = math.factorial(n)
    for k in k_lista:
        coef //= math.factorial(k)
    return coef

def main():
    n = 8
    p_A = 0.40
    p_B = 0.35
    p_C = 0.25
    
    # a) Probabilidad de que exactamente 4 favorezcan a A, 2 a B y 2 a C
    # Usando Distribución Multinomial
    k_A, k_B, k_C = 4, 2, 2
    coef = coef_multinomial(n, [k_A, k_B, k_C])
    prob_a = coef * (p_A ** k_A) * (p_B ** k_B) * (p_C ** k_C)
    
    print(f"a) Probabilidad de exactamente 4 para A, 2 para B y 2 para C: {prob_a:.4f}")
    
    # b) Probabilidad de que ninguno favorezca a C
    # Puede ser visto como una Binomial donde éxito es 'No elegir a C'
    # Probabilidad de no elegir a C es p_A + p_B = 0.75
    p_no_C = p_A + p_B
    prob_ninguno_C = p_no_C ** n
    print(f"b) Probabilidad de que ninguno favorezca a C: {prob_ninguno_C:.4f}")

if __name__ == "__main__":
    main()

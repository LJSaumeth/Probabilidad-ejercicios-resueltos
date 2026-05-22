import math

def coef_multinomial(n, k_lista):
    """Calcula el coeficiente multinomial n! / (k1! * k2! * ...)"""
    coef = math.factorial(n)
    for k in k_lista:
        coef //= math.factorial(k)
    return coef

def main():
    enunciado = """
=========================================================
EJERCICIO 13
En una votación, el 40% de los electores favorece al candidato A, el 35% al B y el 25% al C. 
Se seleccionan 8 votantes al azar con reemplazo.
a) ¿Cuál es la probabilidad de que exactamente 4 favorezcan a A, 2 a B y 2 a C?
b) ¿Cuál es la probabilidad de que ninguno favorezca a C?
=========================================================
"""
    print(enunciado)

    n = 8
    p_A = 0.40
    p_B = 0.35
    p_C = 0.25
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Se usa la Distribución Multinomial ya que hay más de dos posibles resultados excluyentes.")
    print("Fórmula: [n! / (k_A! * k_B! * k_C!)] * (p_A^k_A) * (p_B^k_B) * (p_C^k_C).")
    k_A, k_B, k_C = 4, 2, 2
    coef = coef_multinomial(n, [k_A, k_B, k_C])
    prob_a = coef * (p_A ** k_A) * (p_B ** k_B) * (p_C ** k_C)
    
    print(f"-> Coeficiente multinomial (formas de agruparlos): {coef}")
    print(f"-> Probabilidad de exactamente 4 para A, 2 para B y 2 para C: {prob_a:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: El evento 'ninguno favorece a C' significa que los 8 eligen a A o B.")
    print("Esto se puede reducir a una Distribución Binomial donde el 'éxito' es 'No elegir a C'. La probabilidad base es p_A + p_B = 0.75.")
    p_no_C = p_A + p_B
    prob_ninguno_C = p_no_C ** n
    print(f"-> Probabilidad de (A o B) en un solo votante: {p_no_C:.2f}")
    print(f"-> Probabilidad de que los 8 elijan (A o B) = {p_no_C:.2f}^8 = {prob_ninguno_C:.4f}")

if __name__ == "__main__":
    main()

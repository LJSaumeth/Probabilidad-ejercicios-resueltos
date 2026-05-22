import scipy.stats as stats

def main():
    enunciado = """
=========================================================
EJERCICIO 19
El diámetro de un rodamiento producido por una máquina sigue una distribución normal con media 2.5 cm y desviación estándar 0.05 cm. 
Las especificaciones requieren que el diámetro esté entre 2.4 cm y 2.6 cm.
a) ¿Qué proporción de rodamientos cumple con las especificaciones?
b) Si se toma una muestra de 4 rodamientos, ¿cuál es la probabilidad de que los cuatro cumplan?
=========================================================
"""
    print(enunciado)

    mu = 2.5      # media en cm
    sigma = 0.05  # desviación estándar en cm
    limite_inf = 2.4
    limite_sup = 2.6
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Calculamos la probabilidad de que la variable aleatoria normal caiga en el rango de tolerancia [2.4, 2.6].")
    print("Restamos la probabilidad acumulada CDF(2.6) menos CDF(2.4).")
    prob_cumple = stats.norm.cdf(limite_sup, loc=mu, scale=sigma) - stats.norm.cdf(limite_inf, loc=mu, scale=sigma)
    print(f"-> CDF(2.6) - CDF(2.4) = {prob_cumple:.4f}")
    print(f"-> Proporción que cumple las especificaciones: {prob_cumple:.4f} ({prob_cumple*100:.2f}%)\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: Como la selección de cada rodamiento es un evento independiente del resto, usamos la regla de la multiplicación.")
    print("Multiplicamos la probabilidad de éxito de un rodamiento por sí misma 4 veces (P^4).")
    n_muestra = 4
    prob_4_cumplen = prob_cumple ** n_muestra
    print(f"-> Probabilidad de que 1 rodamiento cumpla: {prob_cumple:.4f}")
    print(f"-> Probabilidad de que los {n_muestra} cumplan = {prob_cumple:.4f}^4 = {prob_4_cumplen:.4f}")

if __name__ == "__main__":
    main()

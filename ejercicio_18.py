import scipy.stats as stats

def main():
    enunciado = """
=========================================================
EJERCICIO 18
Los puntajes de una prueba de admisión se distribuyen normalmente con media 500 y desviación estándar 100.
a) ¿Qué porcentaje de estudiantes obtiene un puntaje entre 400 y 600?
b) Si un estudiante obtuvo 650, ¿en qué percentil se encuentra aproximadamente?
c) Determine el puntaje mínimo necesario para estar en el 10% superior de la distribución.
=========================================================
"""
    print(enunciado)

    mu = 500     # media
    sigma = 100  # desviación estándar
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Para una Distribución Normal, P(400 ≤ X ≤ 600) se halla restando la función de distribución acumulada (CDF) evaluada en 600 menos la evaluada en 400.")
    prob_400_600 = stats.norm.cdf(600, loc=mu, scale=sigma) - stats.norm.cdf(400, loc=mu, scale=sigma)
    porcentaje = prob_400_600 * 100
    print(f"-> CDF(600) - CDF(400) = {prob_400_600:.4f}")
    print(f"-> Porcentaje de estudiantes entre 400 y 600 puntos: {porcentaje:.2f}%\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: El percentil es el porcentaje acumulado que se ubica por debajo del puntaje dado. Lo obtenemos evaluando la CDF en 650 y multiplicando por 100.")
    prob_650 = stats.norm.cdf(650, loc=mu, scale=sigma)
    percentil = prob_650 * 100
    print(f"-> Probabilidad acumulada hasta 650: {prob_650:.4f}")
    print(f"-> Un puntaje de 650 está aproximadamente en el percentil: {int(round(percentil))}\n")
    
    print("--- SOLUCIÓN c) ---")
    print("Explicación: Estar en el 10% superior significa estar en el percentil 90 (0.90 del área a la izquierda).")
    print("Usamos la función inversa de la CDF (conocida como PPF o Percent Point Function) que dado un área bajo la curva devuelve el valor X correspondiente.")
    puntaje_minimo = stats.norm.ppf(0.90, loc=mu, scale=sigma)
    print(f"-> PPF(0.90) con media=500 y std=100 = {puntaje_minimo:.2f}")
    print(f"-> Puntaje mínimo para estar en el 10% superior: {puntaje_minimo:.2f}")

if __name__ == "__main__":
    main()

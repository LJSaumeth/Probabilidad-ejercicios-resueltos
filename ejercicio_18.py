
import scipy.stats as stats

def main():
    # Distribución Normal
    mu = 500     # media
    sigma = 100  # desviación estándar
    
    # a) ¿Qué porcentaje de estudiantes obtiene un puntaje entre 400 y 600?
    # P(400 <= X <= 600) = CDF(600) - CDF(400)
    prob_400_600 = stats.norm.cdf(600, loc=mu, scale=sigma) - stats.norm.cdf(400, loc=mu, scale=sigma)
    porcentaje = prob_400_600 * 100
    print(f"a) Porcentaje de estudiantes entre 400 y 600 puntos: {porcentaje:.2f}% (Prob: {prob_400_600:.4f})")
    
    # b) Si un estudiante obtuvo 650, ¿en qué percentil se encuentra aproximadamente?
    # El percentil es la probabilidad acumulada hasta ese punto multiplicada por 100
    prob_650 = stats.norm.cdf(650, loc=mu, scale=sigma)
    percentil = prob_650 * 100
    print(f"b) Un puntaje de 650 está en el percentil: {percentil:.2f} (aprox. percentil {int(round(percentil))})")
    
    # c) Determine el puntaje mínimo necesario para estar en el 10% superior de la distribución.
    # El 10% superior corresponde al percentil 90 (0.90 en probabilidad acumulada)
    # Se usa ppf (Percent Point Function) que es la inversa de la CDF
    puntaje_minimo = stats.norm.ppf(0.90, loc=mu, scale=sigma)
    print(f"c) Puntaje mínimo para estar en el 10% superior (percentil 90): {puntaje_minimo:.2f}")

if __name__ == "__main__":
    main()

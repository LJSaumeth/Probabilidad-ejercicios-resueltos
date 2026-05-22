
import scipy.stats as stats

def main():
    # Distribución Normal
    mu = 2.5      # media en cm
    sigma = 0.05  # desviación estándar en cm
    
    # Especificaciones: diámetro entre 2.4 cm y 2.6 cm
    limite_inf = 2.4
    limite_sup = 2.6
    
    # a) ¿Qué proporción de rodamientos cumple con las especificaciones?
    # P(2.4 <= X <= 2.6) = CDF(2.6) - CDF(2.4)
    prob_cumple = stats.norm.cdf(limite_sup, loc=mu, scale=sigma) - stats.norm.cdf(limite_inf, loc=mu, scale=sigma)
    print(f"a) Proporción que cumple las especificaciones [2.4, 2.6]: {prob_cumple:.4f} ({prob_cumple*100:.2f}%)")
    
    # b) Si se toma una muestra de 4 rodamientos, ¿cuál es la probabilidad de que los cuatro cumplan?
    # Como la extracción de cada rodamiento es independiente
    # P(Los 4 cumplan) = P(cumple) * P(cumple) * P(cumple) * P(cumple) = P(cumple)^4
    n_muestra = 4
    prob_4_cumplen = prob_cumple ** n_muestra
    print(f"b) Probabilidad de que los {n_muestra} rodamientos cumplan: {prob_4_cumplen:.4f}")

if __name__ == "__main__":
    main()

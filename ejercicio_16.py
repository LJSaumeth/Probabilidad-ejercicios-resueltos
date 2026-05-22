def main():
    # Distribución Geométrica
    # Probabilidad de error en una página
    p = 0.02
    
    # a) Probabilidad de que la primera página con error sea la décima (k = 10)
    # La fórmula es P(X = k) = (1 - p)^(k - 1) * p
    # Significa que hay k-1 fracasos antes del primer éxito (el error)
    k = 10
    prob_10 = ((1 - p) ** (k - 1)) * p
    print(f"a) Probabilidad de que el primer error sea en la 10ma página: {prob_10:.4f}")
    
    # b) Probabilidad de que se necesiten más de 5 páginas para encontrar el primer error
    # P(X > 5) = (1 - p)^5
    # Es decir, que las primeras 5 páginas no tengan error
    k_mas_de = 5
    prob_mas_de_5 = (1 - p) ** k_mas_de
    print(f"b) Probabilidad de necesitar más de 5 páginas para el primer error: {prob_mas_de_5:.4f}")

if __name__ == "__main__":
    main()

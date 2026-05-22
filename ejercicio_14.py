import math

def main():
    # Distribución Binomial Negativa
    # Buscar el r-ésimo éxito en el k-ésimo ensayo
    r = 5  # Número de éxitos (el quinto que compra)
    p = 0.3  # Probabilidad de éxito (comprar)
    
    # a) Probabilidad de que se necesiten exactamente 10 clientes (k = 10 ensayos)
    # Fórmula: C(k-1, r-1) * p^r * (1-p)^(k-r)
    k = 10
    prob_10 = math.comb(k - 1, r - 1) * (p ** r) * ((1 - p) ** (k - r))
    print(f"a) Probabilidad de que se necesiten exactamente 10 clientes: {prob_10:.4f}")
    
    # b) Número esperado de clientes que se deben observar
    # Para esta parametrización de la Binomial Negativa (número total de intentos para r éxitos),
    # la media o valor esperado es: E[X] = r / p
    esperado = r / p
    print(f"b) Número esperado de clientes a observar (Media): {esperado:.4f}")

if __name__ == "__main__":
    main()

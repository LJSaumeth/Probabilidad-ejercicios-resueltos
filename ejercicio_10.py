def main():
    # Valores de la variable aleatoria X y sus respectivas probabilidades P(X=x)
    x_vals = [1, 2, 3, 4]
    p_x = [0.2, 0.3, 0.4, 0.1]
    
    # a) Calcule la media (esperanza) de X: E[X] = sum(x * P(X=x))
    media = sum(x * p for x, p in zip(x_vals, p_x))
    print(f"a) Media (Esperanza) de X: {media:.4f}")
    
    # b) Calcule la varianza de X: Var(X) = E[X^2] - (E[X])^2
    esperanza_x2 = sum((x ** 2) * p for x, p in zip(x_vals, p_x))
    varianza = esperanza_x2 - (media ** 2)
    print(f"b) Varianza de X: {varianza:.4f}")
    
    # c) Calcule P(1 <= X <= 3) = P(X=1) + P(X=2) + P(X=3)
    p_1_a_3 = p_x[0] + p_x[1] + p_x[2]
    print(f"c) Probabilidad P(1 <= X <= 3): {p_1_a_3:.4f}")

if __name__ == "__main__":
    main()

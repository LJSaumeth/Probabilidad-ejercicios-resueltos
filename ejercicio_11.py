def main():
    # a) Determine el valor de k
    # Para que f(y) sea función de densidad, la integral de 0 a 2 debe ser 1
    # ∫(k*y)dy de 0 a 2 = k * [y^2 / 2] evaluado de 0 a 2
    # k * (4/2 - 0) = 2k
    # 2k = 1 => k = 0.5
    k = 0.5
    print(f"a) El valor de k para que f sea una función de densidad válida es: {k:.2f}")
    
    # b) Calcule P(Y <= 1)
    # Es la integral de f(y) de 0 a 1
    # ∫(0.5*y)dy de 0 a 1 = 0.5 * [y^2 / 2] evaluado de 0 a 1 = 0.5 * 0.5 = 0.25
    prob_y_menor_1 = 0.5 * (1**2 / 2)
    print(f"b) P(Y <= 1) = {prob_y_menor_1:.4f}")
    
    # c) Calcule la media y la varianza de Y
    # Media E[Y] = ∫(y * f(y))dy de 0 a 2 = ∫(0.5 * y^2)dy de 0 a 2
    # E[Y] = 0.5 * [y^3 / 3] evaluado de 0 a 2 = 0.5 * (8/3)
    media = 0.5 * (2**3 / 3)
    
    # Varianza Var(Y) = E[Y^2] - (E[Y])^2
    # E[Y^2] = ∫(y^2 * f(y))dy de 0 a 2 = ∫(0.5 * y^3)dy de 0 a 2
    # E[Y^2] = 0.5 * [y^4 / 4] evaluado de 0 a 2 = 0.5 * (16/4)
    esperanza_y2 = 0.5 * (2**4 / 4)
    
    varianza = esperanza_y2 - (media ** 2)
    
    print(f"c) Media (Esperanza) de Y: {media:.4f} (aprox 4/3)")
    print(f"   Varianza de Y: {varianza:.4f}")

if __name__ == "__main__":
    main()

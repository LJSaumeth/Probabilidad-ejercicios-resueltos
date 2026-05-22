def main():
    # Probabilidades a priori de cada máquina
    p_m1 = 0.50
    p_m2 = 0.30
    p_m3 = 0.20
    
    # Probabilidades condicionales: P(Defectuosa | Máquina)
    p_d_m1 = 0.02
    p_d_m2 = 0.03
    p_d_m3 = 0.05
    
    # Probabilidad total de pieza defectuosa P(D)
    p_d = (p_m1 * p_d_m1) + (p_m2 * p_d_m2) + (p_m3 * p_d_m3)
    
    # a) Probabilidad de que haya sido producida por M1 dado que es defectuosa P(M1 | D)
    # Por el Teorema de Bayes
    p_m1_d = (p_m1 * p_d_m1) / p_d
    print(f"a) Probabilidad de que sea de M1 dado que es defectuosa P(M1 | D): {p_m1_d:.4f}")
    
    # b) Probabilidad de que una pieza no sea defectuosa P(D') = 1 - P(D)
    p_no_d = 1 - p_d
    print(f"b) Probabilidad de que la pieza NO sea defectuosa P(D'): {p_no_d:.4f}")

if __name__ == "__main__":
    main()

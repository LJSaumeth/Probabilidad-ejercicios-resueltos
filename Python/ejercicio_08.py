def main():
    enunciado = """
=========================================================
EJERCICIO 8
Tres máquinas (M1, M2, M3) producen el 50%, 30% y 20% de la producción total de una fábrica. 
Los porcentajes de piezas defectuosas de cada máquina son 2%, 3% y 5% respectivamente.
a) Si se selecciona una pieza al azar y resulta defectuosa, ¿cuál es la probabilidad de que haya sido producida por M1?
b) ¿Cuál es la probabilidad de que una pieza no sea defectuosa?
=========================================================
"""
    print(enunciado)

    p_m1 = 0.50
    p_m2 = 0.30
    p_m3 = 0.20
    
    p_d_m1 = 0.02
    p_d_m2 = 0.03
    p_d_m3 = 0.05
    
    print("--- PASO PREVIO ---")
    print("Explicación: Calculamos la Probabilidad Total de que una pieza salga defectuosa P(D), sumando las contribuciones de cada máquina (prob de elegir máquina * prob de defecto en esa máquina).")
    p_d = (p_m1 * p_d_m1) + (p_m2 * p_d_m2) + (p_m3 * p_d_m3)
    print(f"-> P(D) = (0.5*0.02) + (0.3*0.03) + (0.2*0.05) = {p_d:.4f}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Aplicamos Teorema de Bayes para hallar la probabilidad de que venga de M1 dado que ya sabemos que está Defectuosa: P(M1 | D).")
    p_m1_d = (p_m1 * p_d_m1) / p_d
    print(f"-> P(M1 | D) = P(M1 ∩ D) / P(D) = {(p_m1 * p_d_m1):.4f} / {p_d:.4f} = {p_m1_d:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: La probabilidad de que no sea defectuosa P(D') es simplemente el evento complementario de P(D).")
    p_no_d = 1 - p_d
    print(f"-> P(D') = 1 - P(D) = 1 - {p_d:.4f} = {p_no_d:.4f}")

if __name__ == "__main__":
    main()

def main():
    enunciado = """
=========================================================
EJERCICIO 9
Una prueba para detectar una enfermedad tiene una sensibilidad del 95% y una especificidad del 90%.
La prevalencia de la enfermedad en la población es del 1%. 
Si una persona da positivo en la prueba, ¿cuál es la probabilidad de que realmente esté enferma?
=========================================================
"""
    print(enunciado)

    sensibilidad = 0.95    # P(Positivo | Enfermo)
    especificidad = 0.90   # P(Negativo | Sano)
    prevalencia = 0.01     # P(Enfermo)
    
    p_enfermo = prevalencia
    p_sano = 1 - prevalencia
    
    p_pos_enfermo = sensibilidad
    p_pos_sano = 1 - especificidad  # Tasa de falsos positivos
    
    print("--- SOLUCIÓN ÚNICA ---")
    print("Explicación paso a paso:")
    print("Paso 1: Identificamos las probabilidades de que una persona esté enferma (0.01) o sana (0.99) debido a la prevalencia.")
    print("Paso 2: Calculamos la probabilidad de dar positivo siendo sano (falso positivo), que es 1 - Especificidad (1 - 0.90 = 0.10).")
    print("Paso 3: Calculamos la Probabilidad Total de dar positivo P(Pos). Es la suma de verdaderos positivos (0.01*0.95) y falsos positivos (0.99*0.10).")
    
    p_pos = (p_enfermo * p_pos_enfermo) + (p_sano * p_pos_sano)
    print(f"-> P(Positivo) = (0.01 * 0.95) + (0.99 * 0.10) = {p_pos:.4f}")
    
    print("\nPaso 4: Aplicamos el Teorema de Bayes para hallar la probabilidad de estar enfermo si da positivo: P(Enfermo | Positivo).")
    p_enfermo_pos = (p_enfermo * p_pos_enfermo) / p_pos
    
    print(f"-> P(Enfermo | Positivo) = P(Positivo y Enfermo) / P(Positivo) = {(p_enfermo * p_pos_enfermo):.4f} / {p_pos:.4f} = {p_enfermo_pos:.4f}")
    print(f"-> A pesar de la alta sensibilidad, hay solo un {p_enfermo_pos*100:.2f}% de probabilidad de estar enfermo si da positivo debido a que la prevalencia base (1%) es muy baja.")

if __name__ == "__main__":
    main()

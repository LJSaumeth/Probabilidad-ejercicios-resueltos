def main():
    # Datos dados en el problema
    sensibilidad = 0.95    # P(Positivo | Enfermo)
    especificidad = 0.90   # P(Negativo | Sano)
    prevalencia = 0.01     # P(Enfermo)
    
    p_enfermo = prevalencia
    p_sano = 1 - prevalencia
    
    p_pos_enfermo = sensibilidad
    p_pos_sano = 1 - especificidad  # Tasa de falsos positivos
    
    # Probabilidad total de dar positivo P(Positivo)
    p_pos = (p_enfermo * p_pos_enfermo) + (p_sano * p_pos_sano)
    
    # Probabilidad de estar enfermo dado que dio positivo P(Enfermo | Positivo)
    # Teorema de Bayes
    p_enfermo_pos = (p_enfermo * p_pos_enfermo) / p_pos
    
    print("Aplicación del Teorema de Bayes (Prueba diagnóstica):")
    print(f"Sensibilidad: {sensibilidad:.2f}")
    print(f"Especificidad: {especificidad:.2f}")
    print(f"Prevalencia: {prevalencia:.2f}")
    print(f"\nProbabilidad total de dar positivo P(Positivo): {p_pos:.4f}")
    print(f"Probabilidad real de estar enfermo dado que es positivo P(Enfermo|Positivo): {p_enfermo_pos:.4f}")
    print(f"(Aproximadamente {p_enfermo_pos*100:.2f}%)")

if __name__ == "__main__":
    main()

import math

def main():
    # Distribución Hipergeométrica
    N = 12  # Tamaño total de la población (bombillos)
    K = 4   # Elementos con la característica deseada (defectuosos)
    n = 5   # Tamaño de la muestra (seleccionados)
    
    # a) Probabilidad de que exactamente 2 estén defectuosos (x = 2)
    # P(X = x) = [C(K, x) * C(N - K, n - x)] / C(N, n)
    x = 2
    formas_defectuosos = math.comb(K, x)
    formas_buenos = math.comb(N - K, n - x)
    formas_totales = math.comb(N, n)
    
    prob_2_def = (formas_defectuosos * formas_buenos) / formas_totales
    print(f"a) Probabilidad de que exactamente 2 estén defectuosos: {prob_2_def:.4f}")
    
    # b) Número esperado de bombillos defectuosos en la muestra
    # E[X] = n * (K / N)
    esperado = n * (K / N)
    print(f"b) Número esperado de defectuosos en la muestra (Media): {esperado:.4f}")

if __name__ == "__main__":
    main()

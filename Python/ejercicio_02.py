import math

def main():
    enunciado = """
=========================================================
EJERCICIO 2
En una urna hay 5 bolas rojas, 3 azules y 2 verdes. 
Se extraen dos bolas sin reemplazo.
a) ¿Cuántos elementos tiene el espacio muestral?
b) Calcule la probabilidad de que ambas bolas sean del mismo color.
=========================================================
"""
    print(enunciado)

    rojas = 5
    azules = 3
    verdes = 2
    total_bolas = rojas + azules + verdes

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Se extraen 2 bolas de un total de 10 sin reemplazo. Como no importa el orden, usamos la fórmula de combinaciones: C(10, 2).")
    espacio_muestral = math.comb(total_bolas, 2)
    print(f"-> Elementos del espacio muestral (10C2): {espacio_muestral}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para que ambas sean del mismo color, sumamos las probabilidades de sacar 2 rojas O 2 azules O 2 verdes.")
    print("Calculamos las combinaciones posibles de extraer 2 bolas de cada color respectivo y las dividimos por el total del espacio muestral.")
    formas_rojas = math.comb(rojas, 2)
    formas_azules = math.comb(azules, 2)
    formas_verdes = math.comb(verdes, 2)
    
    formas_mismo_color = formas_rojas + formas_azules + formas_verdes
    prob_mismo_color = formas_mismo_color / espacio_muestral
    
    print(f"-> Formas de sacar 2 rojas (5C2): {formas_rojas}")
    print(f"-> Formas de sacar 2 azules (3C2): {formas_azules}")
    print(f"-> Formas de sacar 2 verdes (2C2): {formas_verdes}")
    print(f"-> Total de casos favorables: {formas_mismo_color}")
    print(f"-> Probabilidad = {formas_mismo_color} / {espacio_muestral} = {prob_mismo_color:.4f}")

if __name__ == "__main__":
    main()

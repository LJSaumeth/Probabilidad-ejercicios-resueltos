import math

def main():
    rojas = 5
    azules = 3
    verdes = 2
    total_bolas = rojas + azules + verdes

    # a) Elementos del espacio muestral (combinaciones de 10 bolas en grupos de 2)
    # Ya que se extraen dos bolas sin reemplazo y no importa el orden
    espacio_muestral = math.comb(total_bolas, 2)
    print(f"a) Elementos del espacio muestral (10C2): {espacio_muestral}")

    # b) Probabilidad de que ambas bolas sean del mismo color
    # Es la suma de las probabilidades de sacar 2 rojas, 2 azules o 2 verdes
    formas_rojas = math.comb(rojas, 2)
    formas_azules = math.comb(azules, 2)
    formas_verdes = math.comb(verdes, 2)
    
    formas_mismo_color = formas_rojas + formas_azules + formas_verdes
    prob_mismo_color = formas_mismo_color / espacio_muestral
    
    print(f"\nb) Probabilidad de que ambas sean del mismo color:")
    print(f"   Formas de sacar 2 rojas: {formas_rojas}")
    print(f"   Formas de sacar 2 azules: {formas_azules}")
    print(f"   Formas de sacar 2 verdes: {formas_verdes}")
    print(f"   Total de formas favorables: {formas_mismo_color}")
    print(f"   Probabilidad = {formas_mismo_color}/{espacio_muestral} = {prob_mismo_color:.4f}")

if __name__ == "__main__":
    main()

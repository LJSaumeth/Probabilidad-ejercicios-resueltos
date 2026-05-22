import itertools

def main():
    # a) Espacio muestral
    moneda = ['C', 'X']  # C para Cara, X para Cruz
    espacio_muestral = list(itertools.product(moneda, repeat=3))
    print("a) Espacio muestral:", espacio_muestral)
    print(f"   Tamaño del espacio muestral: {len(espacio_muestral)}")

    # b) Probabilidad de obtener exactamente dos caras
    dos_caras = [resultado for resultado in espacio_muestral if resultado.count('C') == 2]
    prob_dos_caras = len(dos_caras) / len(espacio_muestral)
    print(f"\nb) Probabilidad de exactamente dos caras:")
    print(f"   Eventos favorables: {dos_caras}")
    print(f"   Probabilidad = {len(dos_caras)}/{len(espacio_muestral)} = {prob_dos_caras:.4f}")

    # c) Probabilidad de obtener al menos una cruz
    al_menos_una_cruz = [resultado for resultado in espacio_muestral if resultado.count('X') >= 1]
    prob_al_menos_una_cruz = len(al_menos_una_cruz) / len(espacio_muestral)
    print(f"\nc) Probabilidad de al menos una cruz:")
    print(f"   Probabilidad = {len(al_menos_una_cruz)}/{len(espacio_muestral)} = {prob_al_menos_una_cruz:.4f}")

if __name__ == "__main__":
    main()

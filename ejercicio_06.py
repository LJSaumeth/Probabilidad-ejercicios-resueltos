def main():
    p_portatil = 0.70
    p_tableta = 0.40
    p_ambos = 0.25

    # a) Si se elige un empleado al azar y se sabe que tiene portátil, 
    # probabilidad de que también tenga tableta.
    # Usamos probabilidad condicional: P(Tableta | Portátil) = P(Tableta ∩ Portátil) / P(Portátil)
    p_tableta_dado_portatil = p_ambos / p_portatil
    print(f"a) Probabilidad de que tenga tableta dado que tiene portátil P(Tableta | Portátil): {p_tableta_dado_portatil:.4f}")

    # b) ¿Los eventos “tener portátil” y “tener tableta” son independientes?
    # Son independientes si P(Portátil ∩ Tableta) == P(Portátil) * P(Tableta)
    print("\nb) Independencia de los eventos:")
    p_producto = p_portatil * p_tableta
    if abs(p_ambos - p_producto) < 1e-9:
        print(f"   Son independientes. P(Ambos) = {p_ambos:.4f} es igual a P(Portátil)*P(Tableta) = {p_producto:.4f}")
    else:
        print(f"   NO son independientes. P(Ambos) = {p_ambos:.4f} es distinto de P(Portátil)*P(Tableta) = {p_producto:.4f}")

if __name__ == "__main__":
    main()

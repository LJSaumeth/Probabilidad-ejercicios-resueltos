import itertools

def main():
    # Espacio muestral de lanzar dos dados
    dados = [1, 2, 3, 4, 5, 6]
    espacio = list(itertools.product(dados, repeat=2))
    n_s = len(espacio)

    # Definición de eventos
    # A: la suma de los dos lanzamientos es 7
    A = [(d1, d2) for d1, d2 in espacio if d1 + d2 == 7]
    
    # B: el primer lanzamiento es 4
    B = [(d1, d2) for d1, d2 in espacio if d1 == 4]
    
    # A ∩ B: la suma es 7 Y el primer lanzamiento es 4
    A_inter_B = [resultado for resultado in A if resultado in B]

    # a) Calcule P(A), P(B) y P(A ∩ B)
    p_A = len(A) / n_s
    p_B = len(B) / n_s
    p_A_inter_B = len(A_inter_B) / n_s

    print("a) Probabilidades:")
    print(f"   P(A) = {len(A)}/{n_s} = {p_A:.4f} (Eventos: {A})")
    print(f"   P(B) = {len(B)}/{n_s} = {p_B:.4f} (Eventos: {B})")
    print(f"   P(A ∩ B) = {len(A_inter_B)}/{n_s} = {p_A_inter_B:.4f} (Eventos: {A_inter_B})")

    # b) Verifique si A y B son independientes
    # Son independientes si y solo si P(A ∩ B) = P(A) * P(B)
    print("\nb) Independencia:")
    if abs(p_A_inter_B - (p_A * p_B)) < 1e-9:
        print(f"   Los eventos A y B SON independientes.")
        print(f"   P(A ∩ B) = {p_A_inter_B:.4f} es igual a P(A)*P(B) = {p_A * p_B:.4f}")
    else:
        print(f"   Los eventos A y B NO son independientes.")
        print(f"   P(A ∩ B) = {p_A_inter_B:.4f} no es igual a P(A)*P(B) = {p_A * p_B:.4f}")

if __name__ == "__main__":
    main()

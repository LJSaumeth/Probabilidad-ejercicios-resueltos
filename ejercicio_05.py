import itertools

def main():
    enunciado = """
=========================================================
EJERCICIO 5
Se lanza un dado justo de 6 caras dos veces. 
Sea A el evento “la suma de los dos lanzamientos es 7” y B el evento “el primer lanzamiento es 4”.
a) Calcule P(A), P(B) y P(A ∩ B).
b) Verifique si A y B son independientes usando los axiomas de probabilidad.
=========================================================
"""
    print(enunciado)

    print("--- PASO PREVIO ---")
    print("Explicación: Construimos el espacio muestral al lanzar 2 dados (todas las combinaciones de (1..6, 1..6)) para contar los casos posibles totales.")
    dados = [1, 2, 3, 4, 5, 6]
    espacio = list(itertools.product(dados, repeat=2))
    n_s = len(espacio)
    print(f"-> Casos posibles totales: {n_s}\n")

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Contamos los casos donde se cumple el evento A (suman 7), los del evento B (primer dado es 4) y la intersección A∩B (empiezan con 4 y suman 7).")
    A = [(d1, d2) for d1, d2 in espacio if d1 + d2 == 7]
    B = [(d1, d2) for d1, d2 in espacio if d1 == 4]
    A_inter_B = [resultado for resultado in A if resultado in B]

    p_A = len(A) / n_s
    p_B = len(B) / n_s
    p_A_inter_B = len(A_inter_B) / n_s

    print(f"-> Eventos A (suma 7): {A}")
    print(f"-> Eventos B (empieza 4): {B}")
    print(f"-> Eventos A ∩ B: {A_inter_B}")
    print(f"-> P(A) = {len(A)} / {n_s} = {p_A:.4f}")
    print(f"-> P(B) = {len(B)} / {n_s} = {p_B:.4f}")
    print(f"-> P(A ∩ B) = {len(A_inter_B)} / {n_s} = {p_A_inter_B:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Dos eventos son matemáticamente independientes si la probabilidad de su intersección es igual al producto de sus probabilidades individuales ( P(A ∩ B) == P(A)*P(B) ).")
    if abs(p_A_inter_B - (p_A * p_B)) < 1e-9:
        print(f"-> Son INDEPENDIENTES. P(A ∩ B) = {p_A_inter_B:.4f} coincide con P(A)*P(B) = {p_A * p_B:.4f}")
    else:
        print(f"-> NO son independientes. P(A ∩ B) = {p_A_inter_B:.4f} NO coincide con P(A)*P(B) = {p_A * p_B:.4f}")

if __name__ == "__main__":
    main()

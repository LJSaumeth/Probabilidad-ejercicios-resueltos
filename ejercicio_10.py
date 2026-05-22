def main():
    enunciado = """
=========================================================
EJERCICIO 10
Sea X una variable aleatoria discreta con función de probabilidad:
P(X=1)=0.2, P(X=2)=0.3, P(X=3)=0.4, P(X=4)=0.1.
a) Calcule la media (esperanza) de X.
b) Calcule la varianza de X.
c) Calcule P(1 ≤ X ≤ 3).
=========================================================
"""
    print(enunciado)

    x_vals = [1, 2, 3, 4]
    p_x = [0.2, 0.3, 0.4, 0.1]
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: La media (o valor esperado) de una variable discreta se calcula sumando el producto de cada valor por su probabilidad: E[X] = sum(x * P(x)).")
    media = sum(x * p for x, p in zip(x_vals, p_x))
    print(f"-> Media E[X] = (1*0.2) + (2*0.3) + (3*0.4) + (4*0.1) = {media:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: La varianza se define como Var(X) = E[X^2] - (E[X])^2.")
    print("Primero calculamos la esperanza de X^2 multiplicando cada x al cuadrado por su probabilidad, y luego restamos el cuadrado de la media calculada en a).")
    esperanza_x2 = sum((x ** 2) * p for x, p in zip(x_vals, p_x))
    varianza = esperanza_x2 - (media ** 2)
    print(f"-> E[X^2] = (1^2*0.2) + (2^2*0.3) + (3^2*0.4) + (4^2*0.1) = {esperanza_x2:.4f}")
    print(f"-> Var(X) = {esperanza_x2:.4f} - ({media:.4f})^2 = {varianza:.4f}\n")
    
    print("--- SOLUCIÓN c) ---")
    print("Explicación: Para P(1 ≤ X ≤ 3), simplemente sumamos las probabilidades individuales de que X valga 1, 2 o 3.")
    p_1_a_3 = p_x[0] + p_x[1] + p_x[2]
    print(f"-> P(1 ≤ X ≤ 3) = P(X=1) + P(X=2) + P(X=3) = 0.2 + 0.3 + 0.4 = {p_1_a_3:.4f}")

if __name__ == "__main__":
    main()

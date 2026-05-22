def main():
    enunciado = """
=========================================================
EJERCICIO 6
En una empresa, el 70% de los empleados tiene computador portátil, el 40% tiene tableta y el 25% tiene ambos dispositivos.
a) Si se elige un empleado al azar y se sabe que tiene portátil, ¿cuál es la probabilidad de que también tenga tableta?
b) ¿Los eventos “tener portátil” y “tener tableta” son independientes? Justifique.
=========================================================
"""
    print(enunciado)

    p_portatil = 0.70
    p_tableta = 0.40
    p_ambos = 0.25

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Esto es una Probabilidad Condicional. Sabemos que ya ocurrió el evento 'tiene portátil'.")
    print("La fórmula es P(Tableta | Portátil) = P(Ambos) / P(Portátil).")
    p_tableta_dado_portatil = p_ambos / p_portatil
    print(f"-> P(Tableta | Portátil) = {p_ambos} / {p_portatil} = {p_tableta_dado_portatil:.4f}\n")

    print("--- SOLUCIÓN b) ---")
    print("Explicación: Comprobamos independencia verificando si la intersección P(Ambos) equivale a la multiplicación de sus probabilidades aisladas P(Portátil) * P(Tableta).")
    p_producto = p_portatil * p_tableta
    if abs(p_ambos - p_producto) < 1e-9:
        print(f"-> Son INDEPENDIENTES. P(Ambos) = {p_ambos:.4f} coincide con el producto {p_producto:.4f}")
    else:
        print(f"-> NO son independientes. P(Ambos) = {p_ambos:.4f} es distinto de P(Portátil)*P(Tableta) = {p_producto:.4f}")

if __name__ == "__main__":
    main()

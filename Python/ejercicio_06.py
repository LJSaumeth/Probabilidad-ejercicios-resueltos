import graficas_util  # noqa: F401

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(p_portatil, p_tableta, p_ambos):
    out = carpeta_graficas(6)
    solo_portatil = p_portatil - p_ambos
    solo_tableta = p_tableta - p_ambos
    ninguno = 1 - p_portatil - p_tableta + p_ambos
    plt.bar(
        ["Solo portátil", "Solo tableta", "Ambos", "Ninguno"],
        [solo_portatil, solo_tableta, p_ambos, ninguno],
        color=["#3498db", "#e74c3c", "#9b59b6", "#bdc3c7"],
    )
    plt.ylabel("Proporción")
    plt.title("Diagrama de partición (empleados)")
    plt.ylim(0, 1)
    guardar_figura(out, "venn_empleados")


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

    crear_graficas(p_portatil, p_tableta, p_ambos)


if __name__ == "__main__":
    main()

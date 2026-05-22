import graficas_util  # noqa: F401

import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(p, k_max=20):
    out = carpeta_graficas(16)
    k_vals = list(range(1, k_max + 1))
    probs = [((1 - p) ** (k - 1)) * p for k in k_vals]
    plt.bar([str(k) for k in k_vals], probs, color="#e67e22")
    plt.xlabel("Página k (primer error)")
    plt.ylabel("P(X = k)")
    plt.title(f"Distribución geométrica (p={p})")
    guardar_figura(out, "geometrica_pmf")


def main():
    enunciado = """
=========================================================
EJERCICIO 16
La probabilidad de que una página web tenga un error de carga es 0.02. Cada página es independiente.
a) ¿Cuál es la probabilidad de que la primera página con error sea la décima que se visita?
b) ¿Cuál es la probabilidad de que se necesiten más de 5 páginas para encontrar el primer error?
=========================================================
"""
    print(enunciado)

    p = 0.02
    
    print("--- SOLUCIÓN a) ---")
    print("Explicación: Esto corresponde a una Distribución Geométrica. Queremos saber la probabilidad de que el primer 'éxito' (encontrar un error) ocurra exactamente en el ensayo k.")
    print("La fórmula es P(X=k) = (1-p)^(k-1) * p. Significa que hay k-1 intentos fallidos antes de un éxito.")
    k = 10
    prob_10 = ((1 - p) ** (k - 1)) * p
    print(f"-> Para k=10: P(X=10) = (1 - {p})^9 * {p}")
    print(f"-> Probabilidad de que el primer error sea en la décima página: {prob_10:.4f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para P(X > 5), estamos buscando la probabilidad de que NO haya ningún error en los primeros 5 intentos.")
    print("Esto es simplemente la probabilidad de 'no error' (1-p) multiplicada 5 veces.")
    k_mas_de = 5
    prob_mas_de_5 = (1 - p) ** k_mas_de
    print(f"-> P(X > 5) = (1 - {p})^5")
    print(f"-> Probabilidad de necesitar más de 5 páginas para el primer error: {prob_mas_de_5:.4f}")

    crear_graficas(p)


if __name__ == "__main__":
    main()

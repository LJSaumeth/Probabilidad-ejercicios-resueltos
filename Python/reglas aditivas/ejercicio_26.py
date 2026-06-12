import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(prob_vocal, prob_par, prob_total):
    out = carpeta_graficas(26)
    etiquetas = ["Primera letra vocal", "Último dígito par", "Probabilidad conjunta"]
    valores = [prob_vocal, prob_par, prob_total]
    plt.bar(etiquetas, valores, color=["#e74c3c", "#3498db", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.55 — Código de catálogo")
    for i, v in enumerate(valores):
        plt.text(i, v + 0.002, f"{v:.4f}", ha="center")
    guardar_figura(out, "codigo_catalogo")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.55
Si cada artículo codificado en un catálogo empieza con
3 letras distintas seguidas por 4 dígitos distintos de
cero, calcule la probabilidad de seleccionar aleatoriamente
uno de estos artículos codificados que tenga como primera
letra una vocal y el último dígito sea par.
=========================================================
"""
    print(enunciado)

    total_letras = 26
    vocales = 5
    total_digitos = 9
    digitos_pares = 4

    print("--- SOLUCIÓN ---")
    print("Explicación: La primera letra y el último dígito se eligen de manera independiente del resto de posiciones.")
    print("Como solo nos importan esas dos posiciones específicas, las demás posiciones pueden ser cualquier valor válido.")
    print()
    print("Paso 1: Probabilidad de que la primera letra sea vocal.")
    p_vocal = vocales / total_letras
    print(f"-> Hay {vocales} vocales (a, e, i, o, u) de {total_letras} letras.")
    print(f"-> P(primera letra vocal) = {vocales} / {total_letras} = {p_vocal:.4f}")
    print()
    print("Paso 2: Probabilidad de que el último dígito sea par.")
    print("Los dígitos distintos de cero son: {1, 2, 3, 4, 5, 6, 7, 8, 9}.")
    print(f"Los pares entre ellos: {{2, 4, 6, 8}} → {digitos_pares} dígitos.")
    p_par = digitos_pares / total_digitos
    print(f"-> P(último dígito par) = {digitos_pares} / {total_digitos} = {p_par:.4f}")
    print()
    print("Paso 3: Probabilidad conjunta (eventos independientes).")
    p_total = p_vocal * p_par
    print(f"-> P(vocal y par) = ({vocales}/{total_letras}) × ({digitos_pares}/{total_digitos})")
    print(f"-> P = {p_vocal:.4f} × {p_par:.4f} = {p_total:.4f}")
    print(f"-> P ≈ {p_total:.6f}")

    crear_graficas(p_vocal, p_par, p_total)


if __name__ == "__main__":
    main()

import numpy as np
import matplotlib.pyplot as plt

from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(k=0.5):
    out = carpeta_graficas(11)
    y = np.linspace(0, 2, 200)
    f = np.where((y >= 0) & (y <= 2), k * y, 0)
    plt.plot(y, f, color="#d35400", linewidth=2)
    plt.fill_between(y, f, where=(y >= 0) & (y <= 1), alpha=0.3, color="#3498db", label="P(Y ≤ 1)")
    plt.xlabel("y")
    plt.ylabel("f(y)")
    plt.title(f"Densidad f(y) = {k}·y en [0, 2]")
    plt.legend()
    guardar_figura(out, "densidad_continua")


def main():
    enunciado = """
=========================================================
EJERCICIO 11
Una variable aleatoria continua Y tiene función de densidad f(y) = k·y para 0 ≤ y ≤ 2, y 0 en otro caso.
a) Determine el valor de k para que f sea una función de densidad válida.
b) Calcule P(Y ≤ 1).
c) Calcule la media y la varianza de Y.
=========================================================
"""
    print(enunciado)

    print("--- SOLUCIÓN a) ---")
    print("Explicación: Para que f(y) sea válida, la integral definida en todo su dominio (de 0 a 2) debe ser igual a 1.")
    print("La integral de k*y dy es k*(y^2)/2. Evaluando de 0 a 2, obtenemos k*(4/2) = 2k.")
    print("Igualamos a 1: 2k = 1 -> k = 0.5")
    k = 0.5
    print(f"-> Valor de k = {k:.2f}\n")
    
    print("--- SOLUCIÓN b) ---")
    print("Explicación: Para P(Y ≤ 1), calculamos la integral de f(y) = 0.5*y desde 0 hasta 1.")
    print("La integral es 0.5 * (y^2 / 2). Evaluando en 1 da 0.5 * (1/2) = 0.25.")
    prob_y_menor_1 = 0.5 * (1**2 / 2)
    print(f"-> P(Y ≤ 1) = {prob_y_menor_1:.4f}\n")
    
    print("--- SOLUCIÓN c) ---")
    print("Explicación: La media E[Y] se calcula integrando (y * f(y)) dy = (0.5 * y^2) dy de 0 a 2.")
    print("Esto es 0.5 * (y^3 / 3) evaluado en 2, o sea 0.5 * (8/3) = 4/3.")
    media = 0.5 * (2**3 / 3)
    
    print("Luego la varianza requiere calcular E[Y^2], que es la integral de (y^2 * f(y)) dy = (0.5 * y^3) dy de 0 a 2.")
    print("Esto es 0.5 * (y^4 / 4) evaluado en 2, o sea 0.5 * (16/4) = 2.")
    print("Varianza = E[Y^2] - (E[Y])^2.")
    esperanza_y2 = 0.5 * (2**4 / 4)
    varianza = esperanza_y2 - (media ** 2)
    
    print(f"-> Media (Esperanza) E[Y] = {media:.4f} (aprox 4/3)")
    print(f"-> E[Y^2] = {esperanza_y2:.4f}")
    print(f"-> Varianza Var(Y) = {varianza:.4f}")

    crear_graficas(k)


if __name__ == "__main__":
    main()

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from graficas_util import carpeta_graficas, guardar_figura


def crear_graficas(resultados, etiquetas):
    out = carpeta_graficas(61)
    plt.bar(etiquetas, resultados, color=["#e74c3c", "#3498db", "#f39c12", "#2ecc71"])
    plt.ylabel("Probabilidad")
    plt.title("Ejercicio 2.90 — Contaminación de ríos")
    for i, v in enumerate(resultados):
        plt.text(i, v + 0.005, f"{v:.6f}", ha="center")
    guardar_figura(out, "contaminacion_rios")


def main():
    enunciado = """
=========================================================
EJERCICIO 2.90
Contaminación de ríos de Estados Unidos. Eventos:
A: el río está contaminado.
B: al probar una muestra de agua se detecta contaminación.
C: se permite pescar.

P(A) = 0.3, P(B|A) = 0.75, P(B|A') = 0.20,
P(C|A∩B) = 0.20, P(C|A'∩B) = 0.15,
P(C|A∩B') = 0.80, P(C|A'∩B') = 0.90.

a) P(A ∩ B ∩ C)
b) P(B' ∩ C)
c) P(C)
d) P(A | C ∩ B')  (río contaminado dado que se permite
   pescar y no se detectó contaminación)
=========================================================
"""
    print(enunciado)

    #
    # ── 1. DATOS DEL ENUNCIADO ──
    #
    P_A = 0.3                     # Probabilidad de que el río esté contaminado
    P_B_dado_A = 0.75             # P(detectar contaminación | río contaminado)
    P_B_dado_Ap = 0.20            # P(detectar contaminación | río NO contaminado)
    P_C_dado_AB = 0.20            # P(permitir pesca | contaminado Y detectado)
    P_C_dado_ApB = 0.15           # P(permitir pesca | no contaminado Y detectado)
    P_C_dado_AnoB = 0.80          # P(permitir pesca | contaminado Y NO detectado)
    P_C_dado_ApnoB = 0.90         # P(permitir pesca | no contaminado Y NO detectado)

    print("=" * 56)
    print("  PRELIMINAR: valores que NO da el enunciado directamente")
    print("=" * 56)
    print()

    #
    # ── 2. CALCULAR COMPLEMENTOS Y VALORES DERIVADOS ──
    #
    print("El enunciado da P(A)=0.3. Su complemento es:")
    P_Ap = 1 - P_A                # P(A') = probabilidad de que NO esté contaminado
    print(f"  P(A') = 1 − P(A) = 1 − {P_A} = {P_Ap}")
    print()

    print("El enunciado da P(B|A)=0.75. Su complemento es:")
    P_noB_dado_A = 1 - P_B_dado_A   # P(no detectar | contaminado)
    print(f"  P(B'|A) = 1 − P(B|A) = 1 − {P_B_dado_A} = {P_noB_dado_A}")
    print()

    print("El enunciado da P(B|A')=0.20. Su complemento es:")
    P_noB_dado_Ap = 1 - P_B_dado_Ap  # P(no detectar | no contaminado)
    print(f"  P(B'|A') = 1 − P(B|A') = 1 − {P_B_dado_Ap} = {P_noB_dado_Ap}")
    print()
    print()

    #
    # ── a) P(A ∩ B ∩ C) ──
    #
    print("=" * 56)
    print("  a) P(A ∩ B ∩ C)")
    print("=" * 56)
    print()
    print("Se lee: 'el río está contaminado Y se detecta contaminación Y se permite pescar'.")
    print()
    print("Usamos la regla de la multiplicación encadenada:")
    print("  P(A ∩ B ∩ C) = P(A) × P(B|A) × P(C | A∩B)")
    print()
    print("Cada factor ya lo tenemos (todos son datos del enunciado):")
    print(f"  P(A)        = {P_A}        ← enunciado")
    print(f"  P(B|A)      = {P_B_dado_A}       ← enunciado")
    print(f"  P(C | A∩B)  = {P_C_dado_AB}       ← enunciado")
    prob_a = P_A * P_B_dado_A * P_C_dado_AB
    print()
    print(f"  P(A ∩ B ∩ C) = {P_A} × {P_B_dado_A} × {P_C_dado_AB}")
    print(f"                = {prob_a:.6f}")
    print()
    print()

    #
    # ── b) P(B' ∩ C) ──
    #
    print("=" * 56)
    print("  b) P(B' ∩ C)")
    print("=" * 56)
    print()
    print("Se lee: 'NO se detecta contaminación Y se permite pescar'.")
    print()
    print("B' ∩ C puede ocurrir de dos maneras mutuamente excluyentes,")
    print("según si el río está contaminado (A) o no (A'):")
    print()
    print("  1) El río SÍ está contaminado (A), NO se detecta (B') y se permite pescar (C).")
    print("     → (A ∩ B' ∩ C)")
    print("  2) El río NO está contaminado (A'), NO se detecta (B') y se permite pescar (C).")
    print("     → (A' ∩ B' ∩ C)")
    print()
    print("Por la ley de probabilidad total:")
    print("  P(B' ∩ C) = P(A ∩ B' ∩ C) + P(A' ∩ B' ∩ C)")
    print()

    #
    # Caso 1: A ∩ B' ∩ C
    #
    print("── Caso 1: A ∩ B' ∩ C ──")
    print("  P(A ∩ B' ∩ C) = P(A) × P(B'|A) × P(C | A∩B')")
    print()
    print("  • P(A) = {0}              ← enunciado".format(P_A))
    print(f"  • P(B'|A) = 1 − P(B|A) = 1 − {P_B_dado_A} = {P_noB_dado_A}")
    print(f"  • P(C | A∩B') = {P_C_dado_AnoB}       ← enunciado")
    P_AnoB_C = P_A * P_noB_dado_A * P_C_dado_AnoB
    print(f"  → P(A ∩ B' ∩ C) = {P_A} × {P_noB_dado_A} × {P_C_dado_AnoB} = {P_AnoB_C:.6f}")
    print()

    #
    # Caso 2: A' ∩ B' ∩ C
    #
    print("── Caso 2: A' ∩ B' ∩ C ──")
    print("  P(A' ∩ B' ∩ C) = P(A') × P(B'|A') × P(C | A'∩B')")
    print()
    print(f"  • P(A') = 1 − P(A) = 1 − {P_A} = {P_Ap}")
    print(f"  • P(B'|A') = 1 − P(B|A') = 1 − {P_B_dado_Ap} = {P_noB_dado_Ap}")
    print(f"  • P(C | A'∩B') = {P_C_dado_ApnoB}       ← enunciado")
    P_ApnoB_C = P_Ap * P_noB_dado_Ap * P_C_dado_ApnoB
    print(f"  → P(A' ∩ B' ∩ C) = {P_Ap} × {P_noB_dado_Ap} × {P_C_dado_ApnoB} = {P_ApnoB_C:.6f}")
    print()

    prob_b = P_AnoB_C + P_ApnoB_C
    print("── Suma de ambos casos ──")
    print(f"  P(B' ∩ C) = {P_AnoB_C:.6f} + {P_ApnoB_C:.6f} = {prob_b:.6f}")
    print()
    print()

    #
    # ── c) P(C) ──
    #
    print("=" * 56)
    print("  c) P(C)")
    print("=" * 56)
    print()
    print("Se lee: 'se permite pescar' (sin condiciones).")
    print()
    print("El evento C puede ocurrir en 4 escenarios mutuamente excluyentes,")
    print("que surgen de cruzar A/¬A con B/¬B:")
    print()
    print("  Escenario 1: A  ∩ B  ∩ C   (contaminado, detectado, se pesca)")
    print("  Escenario 2: A  ∩ B' ∩ C   (contaminado, NO detectado, se pesca)")
    print("  Escenario 3: A' ∩ B  ∩ C   (NO contaminado, detectado, se pesca)")
    print("  Escenario 4: A' ∩ B' ∩ C   (NO contaminado, NO detectado, se pesca)")
    print()
    print("Por la ley de probabilidad total:")
    print("  P(C) = P(A∩B∩C) + P(A∩B'∩C) + P(A'∩B∩C) + P(A'∩B'∩C)")
    print()

    #
    # Escenario 1: A ∩ B ∩ C (ya calculado en a)
    #
    print("── Escenario 1: A ∩ B ∩ C ──")
    print(f"  Ya calculado en el inciso a): {prob_a:.6f}")
    print()

    #
    # Escenario 2: A ∩ B' ∩ C (ya calculado en b)
    #
    print("── Escenario 2: A ∩ B' ∩ C ──")
    print(f"  Ya calculado en el inciso b): {P_AnoB_C:.6f}")
    print()

    #
    # Escenario 3: A' ∩ B ∩ C (NUEVO, hay que calcularlo)
    #
    print("── Escenario 3: A' ∩ B ∩ C ──")
    print("  P(A' ∩ B ∩ C) = P(A') × P(B|A') × P(C | A'∩B)")
    print()
    print(f"  • P(A') = {P_Ap}")
    print(f"  • P(B|A') = {P_B_dado_Ap}       ← enunciado")
    print(f"  • P(C | A'∩B) = {P_C_dado_ApB}      ← enunciado")
    P_ApB_C = P_Ap * P_B_dado_Ap * P_C_dado_ApB
    print(f"  → P(A' ∩ B ∩ C) = {P_Ap} × {P_B_dado_Ap} × {P_C_dado_ApB} = {P_ApB_C:.6f}")
    print()

    #
    # Escenario 4: A' ∩ B' ∩ C (ya calculado en b)
    #
    print("── Escenario 4: A' ∩ B' ∩ C ──")
    print(f"  Ya calculado en el inciso b): {P_ApnoB_C:.6f}")
    print()

    prob_c = prob_a + P_AnoB_C + P_ApB_C + P_ApnoB_C
    print("── Suma de los 4 escenarios ──")
    print(f"  P(C) = {prob_a:.6f} + {P_AnoB_C:.6f} + {P_ApB_C:.6f} + {P_ApnoB_C:.6f}")
    print(f"        = {prob_c:.6f}")
    print()
    print()

    #
    # ── d) P(A | C ∩ B') ──
    #
    print("=" * 56)
    print("  d) P(A | C ∩ B')")
    print("=" * 56)
    print()
    print("Se lee: 'el río está contaminado, DADO QUE se permite pescar")
    print("y NO se detectó contaminación'.")
    print()
    print("Aplicamos la definición de probabilidad condicional:")
    print("           P(A ∩ C ∩ B')")
    print("  P(A | C ∩ B') = ─────────────")
    print("              P(C ∩ B')")
    print()

    #
    # Numerador: P(A ∩ C ∩ B') = P(A ∩ B' ∩ C)  (el orden de la intersección no importa)
    #
    print("── Numerador: P(A ∩ C ∩ B') ──")
    print("  Es lo mismo que P(A ∩ B' ∩ C), calculado en el inciso b):")
    print(f"  → P(A ∩ C ∩ B') = {P_AnoB_C:.6f}")
    print()

    #
    # Denominador: P(C ∩ B')
    #
    print("── Denominador: P(C ∩ B') ──")
    print("  C ∩ B' = (A ∩ B' ∩ C) ∪ (A' ∩ B' ∩ C)")
    print("  Ambos términos se calcularon en el inciso b):")
    P_C_int_noB = P_AnoB_C + P_ApnoB_C
    print(f"  → P(C ∩ B') = {P_AnoB_C:.6f} + {P_ApnoB_C:.6f} = {P_C_int_noB:.6f}")
    print()

    prob_d = P_AnoB_C / P_C_int_noB
    print("── Cálculo final ──")
    print(f"            {P_AnoB_C:.6f}")
    print(f"  P(A | C ∩ B') = ───────── = {prob_d:.6f}")
    print(f"            {P_C_int_noB:.6f}")
    print()

    crear_graficas([prob_a, prob_b, prob_c, prob_d],
                   ["a) P(A∩B∩C)", "b) P(B'∩C)", "c) P(C)", "d) P(A|C∩B')"])


if __name__ == "__main__":
    main()

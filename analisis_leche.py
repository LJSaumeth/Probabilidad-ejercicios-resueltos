import numpy as np
from scipy import stats
from collections import Counter

# ============================================================
# DATOS: Contenido de leche achocolatada (ml), n=100
# ============================================================
data = np.array([
    508.7, 522.1, 497.5, 494.4, 490.5, 527.8, 513.4, 503.8, 506.7, 472.3,
    504.5, 487.9, 511.5, 503.6, 476.6, 490.2, 489.7, 508.1, 501.3, 501.8,
    520.7, 503.1, 479.6, 507.9, 489.2, 509.6, 503.8, 510.3, 502.1, 489.1,
    494.9, 493.7, 509.9, 489.3, 496.0, 497.1, 518.7, 490.1, 510.0, 495.9,
    490.3, 487.5, 497.3, 506.2, 499.8, 491.7, 503.2, 490.2, 512.4, 509.0,
    489.8, 498.8, 488.3, 514.0, 487.1, 498.9, 499.9, 497.2, 501.3, 484.5,
    504.6, 511.2, 506.9, 493.5, 500.9, 503.2, 504.9, 487.8, 496.6, 504.3,
    503.1, 512.5, 514.3, 510.9, 503.1, 493.7, 512.1, 499.1, 522.2, 517.3,
    512.2, 490.4, 498.2, 490.2, 487.5, 495.7, 479.9, 511.8, 503.5, 485.0,
    510.1, 482.7, 489.9, 492.9, 508.3, 507.2, 499.6, 502.4, 491.6, 512.5,
])

# ============================================================
# ESTADÍSTICOS PRINCIPALES
# ============================================================
n        = len(data)
media    = np.mean(data)
mediana  = np.median(data)
std      = np.std(data, ddof=1)        # desviación estándar muestral
varianza = np.var(data, ddof=1)        # varianza muestral
cv       = (std / media) * 100         # coeficiente de variación (%)
minimo   = np.min(data)
maximo   = np.max(data)
rango    = maximo - minimo
asimetria = stats.skew(data)

# Percentiles
p10 = np.percentile(data, 10)
q1  = np.percentile(data, 25)
p50 = np.percentile(data, 50)
q3  = np.percentile(data, 75)
p90 = np.percentile(data, 90)
ric = q3 - q1                          # rango intercuartílico

# Moda (valores con mayor frecuencia)
conteos   = Counter(data)
max_frec  = max(conteos.values())
modas     = sorted([k for k, v in conteos.items() if v == max_frec])

# Atípicos por criterio 3-RIC
lim_inf = q1 - 3 * ric
lim_sup = q3 + 3 * ric
atipicos = data[(data < lim_inf) | (data > lim_sup)]

print("=" * 55)
print("       RESUMEN ESTADÍSTICO — LECHE ACHOCOLATADA")
print("=" * 55)
print(f"  n              = {n}")
print(f"  Media          = {media:.4f} ml")
print(f"  Mediana        = {mediana:.4f} ml")
print(f"  Desv. Est.     = {std:.4f} ml")
print(f"  Varianza       = {varianza:.4f} ml²")
print(f"  CV             = {cv:.4f} %")
print(f"  Asimetría      = {asimetria:.6f}")
print(f"  Mínimo         = {minimo} ml")
print(f"  Máximo         = {maximo} ml")
print(f"  Rango          = {rango:.1f} ml")
print(f"  P10            = {p10:.4f} ml")
print(f"  Q1  (P25)      = {q1:.4f} ml")
print(f"  P50            = {p50:.4f} ml")
print(f"  Q3  (P75)      = {q3:.4f} ml")
print(f"  P90            = {p90:.4f} ml")
print(f"  RIC            = {ric:.4f} ml")
print(f"  Modas          = {modas}  (frec. = {max_frec})")
print(f"  Límite inf 3R  = {lim_inf:.2f} ml")
print(f"  Límite sup 3R  = {lim_sup:.2f} ml")
print(f"  Atípicos       = {list(atipicos)}")

# ============================================================
# CONTEOS POR INTERVALOS (útiles para los enunciados)
# ============================================================
print("\n" + "=" * 55)
print("       CONTEOS POR INTERVALOS")
print("=" * 55)
intervalos = [
    ("[490; 510]", 490, 510),
    ("[492; 508]", 492, 508),
    ("[495; 505]", 495, 505),
    ("[500; 510]", 500, 510),
    ("[500; 520]", 500, 520),
]
for nombre, a, b in intervalos:
    cant = np.sum((data >= a) & (data <= b))
    print(f"  {nombre}  →  {cant} obs  ({cant/n*100:.1f} %)")

print(f"\n  > 480          →  {np.sum(data > 480)} obs  ({np.sum(data > 480)/n*100:.1f} %)")
print(f"  < 490          →  {np.sum(data < 490)} obs  ({np.sum(data < 490)/n*100:.1f} %)")

# ============================================================
# VERIFICACIÓN ENUNCIADO POR ENUNCIADO
# ============================================================
print("\n" + "=" * 55)
print("       VERIFICACIÓN DE ENUNCIADOS")
print("=" * 55)

def chk(desc, calculado, afirmado, decimales=1):
    ok = abs(calculado - afirmado) < 10**(-decimales + 1)
    estado = "✅" if ok else "❌"
    print(f"  {estado}  {desc}: calculado={round(calculado, decimales)}, afirmado={afirmado}")

print("\n--- Enunciado 1 ---")
chk("P90",        p90,      512.6)
chk("Asimetría>0 (1=sí)", 1 if asimetria > 0 else 0, 1)
chk("% en [495;505]", np.sum((data>=495)&(data<=505))/n*100, 34.0)

print("\n--- Enunciado 2 ---")
chk("Q1",         q1,       490.5)
chk("% en [492;508]", np.sum((data>=492)&(data<=508))/n*100, 45.0)
chk("% en [500;510]", np.sum((data>=500)&(data<=510))/n*100, 31.0)

print("\n--- Enunciado 3 ---")
chk("Rango",      rango,    56.0)
chk("CV < 2%",    cv,       1.9, decimales=0)   # afirma CV<2%
chk("P10",        p10,      487.8)

print("\n--- Enunciado 4 ---")
chk("% en [500;510]", np.sum((data>=500)&(data<=510))/n*100, 31.0)
chk("Media",      media,    486.6)              # afirma 486,6

print("\n--- Enunciado 5 ---")
chk("% en [495;505]", np.sum((data>=495)&(data<=505))/n*100, 35.0)
chk("Máx > 535.29 (1=sí)", 1 if maximo > 535.29 else 0, 1)
chk("% en [490;510]", np.sum((data>=490)&(data<=510))/n*100, 61.0)

print("\n--- Enunciado 6 ---")
chk("Media",      media,    500.3)
chk("Desv. Est.", std,      10.9)
chk("CV > 2.5% (1=sí)", 1 if cv > 2.5 else 0, 1)
chk("RIC",        ric,      17.93)

print("\n--- Enunciado 7 ---")
chk("Varianza < 110 (1=sí)", 1 if varianza < 110 else 0, 1)
chk("CV",         cv,       2.2)
chk("P10",        p10,      487.9)

print("\n--- Enunciado 8 ---")
chk("Mín < 463.59 (1=sí)", 1 if minimo < 463.59 else 0, 1)
chk("% en [500;520]", np.sum((data>=500)&(data<=520))/n*100, 47.0)
print(f"  {'✅' if conteos[503.1]==4 else '❌'}  Obs=503.1: calculado={conteos[503.1]}, afirmado=4")

print("\n--- Enunciado 9 ---")
chk("Asimetría entre -0.05 y 0.05", asimetria, 0.0, decimales=1)
chk("P90",        p90,      512.4)
chk("% en [500;510]", np.sum((data>=500)&(data<=510))/n*100, 32.0)
chk("CV",         cv,       2.0)

print("\n--- Enunciado 10 ---")
chk("Media",      media,    500.25, decimales=2)
chk("Desv. Est.", std,      10.50,  decimales=2)
chk("CV",         cv,       2.16,   decimales=2)
chk("Q1",         q1,       490.47, decimales=2)

print("\n" + "=" * 55)
print("  Script terminado.")
print("=" * 55)

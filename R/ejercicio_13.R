enunciado <- "
=========================================================
EJERCICIO 13 (R)
La probabilidad de que una máquina produzca una pieza defectuosa es 0.1. Se inspeccionan piezas una por una hasta encontrar la tercera defectuosa.
a) ¿Cuál es la probabilidad de que se necesiten inspeccionar exactamente 8 piezas?
b) ¿Cuál es el número esperado de inspecciones necesarias?
=========================================================
"
cat(enunciado)

p <- 0.1
r <- 3

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Nos encontramos ante un problema de Distribución Binomial Negativa.\n")
cat("Queremos hallar la probabilidad de llegar al 3er éxito en la 8va inspección.\n")
cat("En R, la función dnbinom(x, size, prob) define 'x' como el número de fracasos ANTES de alcanzar los 'size' (r) éxitos.\n")
cat("Como inspeccionamos 8 piezas y 3 son defectuosas, entonces hay 8 - 3 = 5 fracasos (buenas).\n")
fracasos <- 8 - 3
prob_8_piezas <- dnbinom(fracasos, size=r, prob=p)
cat(sprintf("-> Fracasos previos = %d\n", fracasos))
cat(sprintf("-> P(Necesitar 8 inspecciones en total) = %.4f\n\n", prob_8_piezas))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: En la Binomial Negativa parametrizada para el total de ensayos (fracasos + éxitos), la media es r / p.\n")
media_inspecciones <- r / p
cat(sprintf("-> Número esperado de inspecciones totales (Media) = %d / %.1f = %.4f\n", r, p, media_inspecciones))

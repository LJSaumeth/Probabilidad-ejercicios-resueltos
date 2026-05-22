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

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(13)
  cargar_ggplot()
  k_tot <- seq(r, 20)
  df <- data.frame(k = k_tot, prob = dnbinom(k_tot - r, size = r, prob = p))
  p <- ggplot(df, aes(x = factor(k), y = prob)) +
    geom_col(fill = "#9b59b6", width = 0.7) +
    labs(title = sprintf("Binomial negativa (r=%d, p=%.1f)", r, p), x = "k", y = "P(X = k)") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "binomial_negativa_pmf")
}

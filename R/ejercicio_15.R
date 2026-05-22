enunciado <- "
=========================================================
EJERCICIO 15 (R)
La probabilidad de que una persona compre un boleto de lotería en una tienda es 0.05. Cada persona actúa independientemente.
a) ¿Cuál es la probabilidad de que la primera compra ocurra en la quinta persona que entra?
b) ¿Cuál es la probabilidad de que se requieran más de 8 personas para encontrar la primera compra?
=========================================================
"
cat(enunciado)

p <- 0.05

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Estamos buscando el momento del primer éxito, lo que modela una Distribución Geométrica.\n")
cat("En R, la función dgeom(x, prob) asume que 'x' es el número de FRACASOS antes del primer éxito.\n")
cat("Para que el primer éxito ocurra en la 5ta persona, debió haber 4 fracasos previos.\n")
fracasos_a <- 5 - 1
prob_5ta <- dgeom(fracasos_a, prob=p)
cat(sprintf("-> P(X=5 intentos en total, que implica 4 fracasos) = %.4f\n\n", prob_5ta))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: 'Más de 8 personas' significa que necesitamos P(X > 8) intentos totales. Es decir, que las primeras 8 personas no compraron.\n")
cat("Matemáticamente es igual a la probabilidad de 8 fracasos consecutivos: (1-p)^8.\n")
cat("En R, podemos usar la función acumulada pgeom(7, prob=p) (que implica hasta 7 fracasos, es decir 8 ensayos en total) y restar de 1.\n")
prob_mas_de_8 <- 1 - pgeom(8 - 1, prob=p)
cat(sprintf("-> P(X > 8) = 1 - P(X ≤ 8) = (1-0.05)^8 = %.4f\n", prob_mas_de_8))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(15)
  cargar_ggplot()
  k_vals <- 1:15
  df <- data.frame(k = k_vals, prob = dgeom(k_vals - 1, prob = p))
  p <- ggplot(df, aes(x = factor(k), y = prob)) +
    geom_col(fill = "#e67e22", width = 0.7) +
    labs(title = sprintf("Geometrica (p=%.2f)", p), x = "k", y = "P(X = k)") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "geometrica_pmf")
}

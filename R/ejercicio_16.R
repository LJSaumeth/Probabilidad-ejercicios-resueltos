enunciado <- "
=========================================================
EJERCICIO 16 (R)
El número de accidentes diarios en una fábrica sigue una distribución de Poisson con media 2.5 accidentes por día.
a) ¿Cuál es la probabilidad de que un día dado ocurran exactamente 3 accidentes?
b) ¿Cuál es la probabilidad de que ocurran 2 o menos accidentes en un día?
c) ¿Cuál es la probabilidad de que en una semana laboral (5 días) ocurran al menos 10 accidentes en total?
=========================================================
"
cat(enunciado)

lmbda_dia <- 2.5

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Usamos la Distribución de Poisson (dpois en R). Queremos la probabilidad exacta P(X=3) con lambda=2.5.\n")
prob_3 <- dpois(3, lambda=lmbda_dia)
cat(sprintf("-> P(X=3) = %.4f\n\n", prob_3))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: '2 o menos' accidentes significa P(X ≤ 2). Usamos la función de distribución acumulada ppois.\n")
prob_2_o_menos <- ppois(2, lambda=lmbda_dia)
cat(sprintf("-> P(X ≤ 2) = %.4f\n\n", prob_2_o_menos))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Para un periodo de 5 días, debido a la aditividad de la Poisson, la nueva media lambda se multiplica por 5 (2.5 * 5 = 12.5).\n")
cat("Queremos 'al menos 10' accidentes P(X ≥ 10), que es equivalente a 1 - P(X ≤ 9). Calculamos esto con ppois(9, lambda=12.5).\n")
lmbda_sem <- lmbda_dia * 5
prob_al_menos_10 <- 1 - ppois(9, lambda=lmbda_sem)
cat(sprintf("-> Nueva media (λ) para 5 días = 12.5\n"))
cat(sprintf("-> P(X ≥ 10) = 1 - P(X ≤ 9) = 1 - %.4f = %.4f\n", ppois(9, lambda=lmbda_sem), prob_al_menos_10))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(16)
  cargar_ggplot()
  df <- data.frame(k = 0:10, prob = dpois(0:10, lambda = lmbda_dia))
  p <- ggplot(df, aes(x = factor(k), y = prob)) +
    geom_col(fill = "#3498db", width = 0.7) +
    labs(title = sprintf("Poisson diaria (lambda=%.1f)", lmbda_dia), x = "k", y = "P(X = k)") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "poisson_diaria")
}

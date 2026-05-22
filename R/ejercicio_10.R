enunciado <- "
=========================================================
EJERCICIO 10 (R)
Una variable aleatoria continua Y tiene función de densidad f(y) = (3/2)·y² para -1 ≤ y ≤ 1, y 0 en otro caso.
a) Verifique que es una densidad.
b) Calcule P(0 ≤ Y ≤ 0.5).
c) Obtenga la media y la varianza de Y.
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Verificamos matemáticamente que f(y) integra a 1 en todo su dominio [-1, 1]. Además f(y) es siempre positiva.\n")
cat("La integral analítica de (3/2)*y^2 es y^3 / 2.\n")
cat("Evaluada entre -1 y 1: (1^3 / 2) - ((-1)^3 / 2) = (1/2) - (-1/2) = 1. Sí es densidad válida.\n\n")

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Evaluamos la misma integral (y^3 / 2) en el intervalo solicitado [0, 0.5].\n")
prob_rango <- (0.5^3) / 2 - (0^3) / 2
cat(sprintf("-> P(0 ≤ Y ≤ 0.5) = (0.5^3 / 2) - 0 = %.4f\n\n", prob_rango))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: La media E[Y] se calcula con la integral de y*f(y) = (3/2)*y^3 de -1 a 1.\n")
cat("La primitiva es (3/8)*y^4. Por simetría (una función impar evaluada en un rango simétrico), el resultado es 0.\n")
media <- 0
cat(sprintf("-> Media E[Y] = %.4f\n\n", media))

cat("Explicación: La varianza es E[Y^2] - (E[Y])^2. Integramos y^2 * f(y) = (3/2)*y^4 de -1 a 1.\n")
cat("La primitiva es (3/10)*y^5. Evaluada entre -1 y 1 da: (3/10)*1 - (3/10)*(-1) = 6/10 = 0.6.\n")
var_y <- 0.6 - (media^2)
cat(sprintf("-> E[Y^2] = 0.6000\n"))
cat(sprintf("-> Varianza Var(Y) = 0.6000 - 0 = %.4f\n", var_y))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(10)
  cargar_ggplot()
  y <- seq(-1, 1, length.out = 200)
  df <- data.frame(y = y, f = ifelse(y >= -1 & y <= 1, 1.5 * y^2, 0))
  p <- ggplot(df, aes(x = y, y = f)) +
    geom_line(color = "#d35400", linewidth = 1.1) +
    geom_ribbon(data = subset(df, y >= 0 & y <= 0.5), aes(ymin = 0, ymax = f),
                fill = "#3498db", alpha = 0.35) +
    labs(title = "Densidad f(y) = (3/2)*y^2", x = "y", y = "f(y)") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "densidad_y")
}

enunciado <- "
=========================================================
EJERCICIO 17 (R)
Los tiempos de reparación de un equipo siguen una distribución normal con media 45 minutos y desviación estándar 8 minutos.
a) ¿Qué proporción de reparaciones duran entre 40 y 50 minutos?
b) ¿Cuál es el tiempo máximo que dura el 90% de las reparaciones más cortas?
c) Si se toman 6 reparaciones al azar, ¿cuál es la probabilidad de que todas duren menos de 50 minutos?
=========================================================
"
cat(enunciado)

mu <- 45
sigma <- 8

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Utilizamos pnorm para la distribución Normal. Restamos la probabilidad acumulada hasta 50 menos la acumulada hasta 40.\n")
prob_rango <- pnorm(50, mean=mu, sd=sigma) - pnorm(40, mean=mu, sd=sigma)
cat(sprintf("-> P(40 ≤ X ≤ 50) = pnorm(50) - pnorm(40) = %.4f\n\n", prob_rango))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Nos piden el percentil 90. Usamos la función qnorm(0.90) (inversa de pnorm o función cuantil) para encontrar el tiempo 'x' que acumula el 90% del área a su izquierda.\n")
percentil_90 <- qnorm(0.90, mean=mu, sd=sigma)
cat(sprintf("-> Tiempo máximo del 90%% (qnorm(0.90)) = %.2f minutos\n\n", percentil_90))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Calculamos primero la probabilidad de que 1 reparación dure menos de 50 mins: P(X < 50) = pnorm(50).\n")
cat("Luego, como son eventos independientes, por regla de multiplicación elevamos esa probabilidad a la potencia 6.\n")
prob_menos_50 <- pnorm(50, mean=mu, sd=sigma)
prob_6_menos_50 <- prob_menos_50^6
cat(sprintf("-> P(X < 50) para 1 reparación = %.4f\n", prob_menos_50))
cat(sprintf("-> P(Las 6 duren < 50) = %.4f^6 = %.4f\n", prob_menos_50, prob_6_menos_50))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(17)
  cargar_ggplot()
  x <- seq(mu - 4 * sigma, mu + 4 * sigma, length.out = 300)
  df <- data.frame(x = x, y = dnorm(x, mean = mu, sd = sigma))
  p <- ggplot(df, aes(x = x, y = y)) +
    geom_line(color = "#2c3e50", linewidth = 1.1) +
    geom_ribbon(data = subset(df, x >= 40 & x <= 50), aes(ymin = 0, ymax = y),
                fill = "#3498db", alpha = 0.35) +
    geom_vline(xintercept = percentil_90, color = "#e74c3c", linetype = "dashed") +
    labs(title = sprintf("Normal (mu=%d, sigma=%d)", mu, sigma), x = "Minutos", y = "Densidad") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "normal_reparaciones")
}

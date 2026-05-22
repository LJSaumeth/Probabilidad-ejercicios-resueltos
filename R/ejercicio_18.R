enunciado <- "
=========================================================
EJERCICIO 18 (R)
El peso de un paquete de café etiquetado como “500 g” tiene una distribución normal con media 502 g y desviación estándar 3 g. La normativa permite que a lo sumo el 5% de los paquetes pese menos de 500 g. ¿Cumple el proceso con esta normativa? Calcule la probabilidad de que un paquete pese menos de 500 g.
=========================================================
"
cat(enunciado)

mu <- 502
sigma <- 3
limite <- 500

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Calculamos la probabilidad de que el peso de un paquete sea estrictamente menor a 500g usando la distribución acumulada Normal pnorm(500).\n")
prob_menos_500 <- pnorm(limite, mean=mu, sd=sigma)
porcentaje <- prob_menos_500 * 100

cat(sprintf("-> Probabilidad de pesar menos de 500g = pnorm(500, mean=502, sd=3) = %.4f\n", prob_menos_500))
cat(sprintf("-> Esto representa el %.2f%%\n\n", porcentaje))

cat("¿Cumple la normativa?\n")
cat("Explicación: Comparamos nuestro resultado con el umbral de aceptación del 5%.\n")
if(porcentaje <= 5){
  cat(sprintf("-> SÍ cumple la normativa, porque el porcentaje (%.2f%%) es menor o igual al 5%% permitido.\n", porcentaje))
} else {
  cat(sprintf("-> NO cumple la normativa, porque el porcentaje (%.2f%%) supera el límite del 5%% permitido.\n", porcentaje))
}

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(18)
  cargar_ggplot()
  x <- seq(mu - 4 * sigma, mu + 4 * sigma, length.out = 300)
  df <- data.frame(x = x, y = dnorm(x, mean = mu, sd = sigma))
  p <- ggplot(df, aes(x = x, y = y)) +
    geom_line(color = "#34495e", linewidth = 1.1) +
    geom_ribbon(data = subset(df, x < limite), aes(ymin = 0, ymax = y),
                fill = "#e74c3c", alpha = 0.35) +
    geom_vline(xintercept = limite, color = "#c0392b", linetype = "dashed") +
    labs(title = "Distribución del peso del paquete", x = "Peso (g)", y = "Densidad") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "normal_peso_cafe")
}

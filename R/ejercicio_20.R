enunciado <- "
=========================================================
EJERCICIO 20 (R)
Genere 500 valores aleatorios de una distribución normal con media 100 y desviación 15. A partir de esos datos, calcule la media muestral, la desviación estándar muestral y el porcentaje de valores que caen dentro de una desviación estándar de la media. Compare con los valores teóricos de la regla empírica.
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Usaremos la función rnorm() propia de R para generar una muestra sintética de 500 valores Normales.\n")
cat("Luego aplicaremos las funciones descriptivas mean() y sd() para calcular las estadísticas muestrales y ver qué tan cerca están de los parámetros teóricos.\n")
cat("Finalmente, validaremos la 'Regla Empírica' (o Regla 68-95-99.7) contando qué porcentaje de la muestra cae a +/- 1 desviación estándar de su media.\n\n")

set.seed(456) # para reproducibilidad
n_muestras <- 500
mu_teorica <- 100
sd_teorica <- 15

# Simulación
datos <- rnorm(n_muestras, mean=mu_teorica, sd=sd_teorica)

# Estadísticas muestrales
media_muestral <- mean(datos)
sd_muestral <- sd(datos)

cat(sprintf("-> Media poblacional: %.2f | Media muestral observada: %.2f\n", mu_teorica, media_muestral))
cat(sprintf("-> Desv. Std poblacional: %.2f | Desv. Std muestral observada: %.2f\n\n", sd_teorica, sd_muestral))

# Porcentaje a +/- 1 desviación estándar
limite_inf <- media_muestral - sd_muestral
limite_sup <- media_muestral + sd_muestral

# Conteo de elementos que cumplen la condición
en_rango <- sum(datos >= limite_inf & datos <= limite_sup)
pct_en_rango <- (en_rango / n_muestras) * 100

cat(sprintf("-> Valores muestrales que caen entre [%.2f, %.2f]: %d\n", limite_inf, limite_sup, en_rango))
cat(sprintf("-> Porcentaje en la muestra empírica: %.2f%%\n", pct_en_rango))
cat("-> Valor teórico según regla empírica para +/- 1 sigma: Aproximadamente 68.27%\n")

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(20)
  cargar_ggplot()
  df_datos <- data.frame(valor = datos)
  curva <- data.frame(
    x = seq(min(datos), max(datos), length.out = 200),
    y = dnorm(seq(min(datos), max(datos), length.out = 200), mean = mu_teorica, sd = sd_teorica)
  )
  p1 <- ggplot(df_datos, aes(x = valor)) +
    geom_histogram(aes(y = after_stat(density)), bins = 25, fill = "#3498db", color = "white", alpha = 0.85) +
    geom_line(data = curva, aes(x = x, y = y), color = "#c0392b", linewidth = 1.1) +
    geom_vline(xintercept = c(limite_inf, limite_sup), color = "#e67e22", linetype = "dashed") +
    labs(title = "Muestra N(100, 15^2)", x = "Valor", y = "Densidad") +
    tema_probabilidad()
  guardar_ggplot(p1, carpeta, "histograma_normal", width = 9, height = 5)
  df_regla <- data.frame(tipo = c("Muestra (+/-1 sigma)", "Teorico 68.27%"), pct = c(pct_en_rango, 68.27))
  p2 <- ggplot(df_regla, aes(x = tipo, y = pct, fill = tipo)) +
    geom_col(width = 0.55, show.legend = FALSE) +
    scale_fill_manual(values = c("#9b59b6", "#2ecc71")) +
    labs(title = "Regla empírica: comparación", x = NULL, y = "Porcentaje (%)") +
    tema_probabilidad()
  guardar_ggplot(p2, carpeta, "regla_empirica")
}

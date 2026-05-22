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

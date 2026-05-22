enunciado <- "
=========================================================
EJERCICIO 1 (R)
Se lanza un dado de 6 caras tres veces consecutivas.
a) ¿Cuántos resultados elementales tiene el espacio muestral?
b) Calcule la probabilidad de obtener una suma total de 10.
c) Calcule la probabilidad de que el primer lanzamiento sea mayor que el segundo y el segundo mayor que el tercero.
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Cada lanzamiento tiene 6 resultados posibles. Como son 3 lanzamientos independientes, usamos el principio multiplicativo: 6 * 6 * 6.\n")
resultados_totales <- 6^3
cat(sprintf("-> Resultados elementales: %d\n\n", resultados_totales))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Generamos el espacio muestral completo usando expand.grid y filtramos las combinaciones cuya suma sea 10.\n")
espacio <- expand.grid(d1=1:6, d2=1:6, d3=1:6)
suma_10 <- subset(espacio, d1 + d2 + d3 == 10)
casos_favorables_b <- nrow(suma_10)
prob_b <- casos_favorables_b / resultados_totales
cat(sprintf("-> Combinaciones que suman 10: %d\n", casos_favorables_b))
cat(sprintf("-> Probabilidad de suma 10 = %d / %d = %.4f\n\n", casos_favorables_b, resultados_totales, prob_b))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Buscamos combinaciones donde el primer dado sea mayor al segundo y este mayor al tercero (d1 > d2 > d3). Contamos los casos y dividimos por el total.\n")
mayor_estricto <- subset(espacio, d1 > d2 & d2 > d3)
casos_favorables_c <- nrow(mayor_estricto)
prob_c <- casos_favorables_c / resultados_totales
cat(sprintf("-> Combinaciones con d1 > d2 > d3: %d\n", casos_favorables_c))
cat(sprintf("-> Probabilidad = %d / %d = %.4f\n", casos_favorables_c, resultados_totales, prob_c))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(1)
  cargar_ggplot()
  sumas <- espacio$d1 + espacio$d2 + espacio$d3
  df <- as.data.frame(table(sumas))
  names(df) <- c("suma", "freq")
  p <- ggplot(df, aes(x = suma, y = freq)) +
    geom_col(fill = "#5dade2", width = 0.7) +
    labs(title = "Distribución de la suma (3 dados)", x = "Suma", y = "Frecuencia") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "distribucion_suma")
}

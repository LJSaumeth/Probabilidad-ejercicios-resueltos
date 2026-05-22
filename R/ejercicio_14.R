enunciado <- "
=========================================================
EJERCICIO 14 (R)
En un lote de 20 artículos, 6 son defectuosos. Se seleccionan 4 artículos al azar sin reemplazo.
a) ¿Cuál es la probabilidad de que exactamente 2 sean defectuosos?
b) ¿Cuál es la probabilidad de que a lo sumo 1 sea defectuoso?
c) ¿Cuál es el valor esperado y la varianza del número de defectuosos en la muestra?
=========================================================
"
cat(enunciado)

# Parámetros para dhyper en R
# m: número de defectuosos (éxitos en población) = 6
# n: número de no defectuosos (fracasos en población) = 14
# k: tamaño de muestra = 4
m <- 6
n <- 20 - m
k <- 4

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: El muestreo se hace sin reemplazo desde una población finita, por lo que usamos la Distribución Hipergeométrica (dhyper).\n")
cat("Queremos hallar P(X = 2) defectuosos.\n")
prob_2_def <- dhyper(2, m, n, k)
cat(sprintf("-> P(X = 2) = %.4f\n\n", prob_2_def))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: 'A lo sumo 1' defectuoso significa calcular la probabilidad acumulada P(X ≤ 1).\n")
cat("En R, podemos sumar dhyper(0) + dhyper(1), o directamente usar la acumulada phyper(1, m, n, k).\n")
prob_1_o_menos <- phyper(1, m, n, k)
cat(sprintf("-> P(X ≤ 1) = %.4f\n\n", prob_1_o_menos))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Para la hipergeométrica, la media es k * (m / N).\n")
cat("La varianza es k * (m / N) * (n / N) * ((N - k) / (N - 1)), donde N = m + n.\n")
N_total <- m + n
media <- k * (m / N_total)
varianza <- k * (m / N_total) * (n / N_total) * ((N_total - k) / (N_total - 1))
cat(sprintf("-> Media (Valor esperado) = %.4f\n", media))
cat(sprintf("-> Varianza = %.4f\n", varianza))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(14)
  cargar_ggplot()
  x_vals <- 0:min(k, m)
  df <- data.frame(x = x_vals, prob = dhyper(x_vals, m, n, k))
  p <- ggplot(df, aes(x = factor(x), y = prob)) +
    geom_col(fill = "#1abc9c", width = 0.7) +
    labs(title = sprintf("Hipergeometrica (N=%d, m=%d, k=%d)", N_total, m, k), x = "x", y = "P(X = x)") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "hipergeometrica_pmf")
}

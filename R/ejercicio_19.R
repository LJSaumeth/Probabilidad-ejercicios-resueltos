enunciado <- "
=========================================================
EJERCICIO 19 (R)
Simule en R el lanzamiento de 1000 veces de dos dados justos y calcule la frecuencia relativa de que la suma sea 7. Compare con la probabilidad teórica.
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Usaremos la función 'sample()' con reemplazo para simular de forma aleatoria 1000 lanzamientos de un dado de 6 caras y otros 1000 para el segundo dado.\n")
cat("Sumaremos elemento a elemento los resultados, contaremos con una condición lógica (== 7) cuántas veces la suma dio 7 y calcularemos la proporción.\n")
cat("Por último, calculamos la teórica (hay 6 combinaciones sobre 36 posibles que suman 7 = 1/6) y comprobamos la Ley de los Grandes Números.\n\n")

# Fijar semilla para reproducibilidad (opcional, pero útil en simulaciones)
set.seed(123)
n_simulaciones <- 1000

# Simulación
dado1 <- sample(1:6, size=n_simulaciones, replace=TRUE)
dado2 <- sample(1:6, size=n_simulaciones, replace=TRUE)
suma_dados <- dado1 + dado2

# Frecuencia empírica
casos_7_simulados <- sum(suma_dados == 7)
frecuencia_relativa <- casos_7_simulados / n_simulaciones

# Probabilidad teórica
prob_teorica <- 6 / 36

cat(sprintf("-> Número de veces que sumó 7 en las %d simulaciones: %d\n", n_simulaciones, casos_7_simulados))
cat(sprintf("-> Frecuencia relativa (simulada) = %.4f\n", frecuencia_relativa))
cat(sprintf("-> Probabilidad teórica esperada (6/36) = %.4f\n", prob_teorica))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(19)
  cargar_ggplot()
  df_freq <- as.data.frame(table(suma_dados))
  names(df_freq) <- c("suma", "freq")
  p1 <- ggplot(df_freq, aes(x = suma, y = freq)) +
    geom_col(fill = "#5dade2", width = 0.7) +
    labs(title = "Frecuencia de sumas (simulación)", x = "Suma", y = "Conteo") +
    tema_probabilidad()
  guardar_ggplot(p1, carpeta, "frecuencia_sumas")
  df_cmp <- data.frame(tipo = c("Simulada", "Teorica"), prob = c(frecuencia_relativa, prob_teorica))
  p2 <- ggplot(df_cmp, aes(x = tipo, y = prob, fill = tipo)) +
    geom_col(width = 0.5, show.legend = FALSE) +
    scale_fill_manual(values = c("#e67e22", "#27ae60")) +
    scale_y_continuous(limits = c(0, 0.25)) +
    labs(title = "Suma = 7: simulación vs teoría", x = NULL, y = "Probabilidad") +
    tema_probabilidad()
  guardar_ggplot(p2, carpeta, "comparacion_suma_7")
}

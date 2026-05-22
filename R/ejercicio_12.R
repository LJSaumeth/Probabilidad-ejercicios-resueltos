enunciado <- "
=========================================================
EJERCICIO 12 (R)
En una población, el 45% prefiere la marca A, el 35% la marca B y el 20% la marca C. Se encuesta a 10 personas al azar (con reemplazo).
a) ¿Cuál es la probabilidad de que 5 prefieran A, 3 B y 2 C?
b) ¿Cuál es la probabilidad de que ninguna prefiera C?
=========================================================
"
cat(enunciado)

p_probs <- c(0.45, 0.35, 0.20)
n <- 10

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Al tener más de dos categorías mutuamente excluyentes, usamos la distribución Multinomial. En R se usa dmultinom(x, size, prob).\n")
k_vals <- c(5, 3, 2)
prob_mult <- dmultinom(k_vals, size=n, prob=p_probs)
cat(sprintf("-> P(5 prefieren A, 3 B, 2 C) = %.4f\n\n", prob_mult))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Si ninguna prefiere C, significa que las 10 personas prefieren A o B.\n")
cat("Podemos reducirlo a una distribución Binomial donde 'éxito' es 'elegir A o B'. La probabilidad será la suma P(A) + P(B) = 0.80.\n")
cat("Usamos dbinom para calcular P(X = 10) con p = 0.80.\n")
p_no_C <- p_probs[1] + p_probs[2]
prob_ninguna_C <- dbinom(10, size=n, prob=p_no_C)
cat(sprintf("-> Probabilidad de no elegir C por persona: %.2f\n", p_no_C))
cat(sprintf("-> P(Las 10 personas eligen A o B) = %.4f\n", prob_ninguna_C))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(12)
  cargar_ggplot()
  df <- data.frame(marca = c("A", "B", "C"), prop = p_probs)
  p <- ggplot(df, aes(x = marca, y = prop, fill = marca)) +
    geom_col(width = 0.6, show.legend = FALSE) +
    scale_fill_manual(values = c("#e74c3c", "#3498db", "#f1c40f")) +
    labs(title = "Preferencias por marca", x = NULL, y = "Proporción") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "preferencias_marcas")
}

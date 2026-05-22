enunciado <- "
=========================================================
EJERCICIO 2 (R)
De una baraja española de 40 cartas (4 palos: oros, copas, espadas, bastos; cada palo con números 1 al 7, sota, caballo, rey) se extraen dos cartas sin reemplazo.
a) ¿Cuál es la probabilidad de que ambas sean del mismo palo?
b) ¿Cuál es la probabilidad de que al menos una sea figura (sota, caballo o rey)?
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: El total de formas de extraer 2 cartas de 40 sin orden es choose(40, 2).\n")
cat("Para que sean del mismo palo, elegimos 2 cartas de los 10 disponibles en un solo palo: choose(10, 2). Al haber 4 palos, multiplicamos esto por 4.\n")
total_extracciones <- choose(40, 2)
mismo_palo <- 4 * choose(10, 2)
prob_mismo_palo <- mismo_palo / total_extracciones
cat(sprintf("-> Casos totales (40C2): %d\n", total_extracciones))
cat(sprintf("-> Casos favorables (4 * 10C2): %d\n", mismo_palo))
cat(sprintf("-> Probabilidad = %.4f\n\n", prob_mismo_palo))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Calculamos la probabilidad de que NINGUNA sea figura y luego calculamos el complemento (1 - Probabilidad).\n")
cat("Hay 12 figuras (3 por palo) y 28 no-figuras. Las formas de sacar 2 no-figuras de las 28 es choose(28, 2).\n")
ninguna_figura <- choose(28, 2)
prob_ninguna <- ninguna_figura / total_extracciones
prob_al_menos_una <- 1 - prob_ninguna
cat(sprintf("-> Casos donde ninguna es figura (28C2): %d\n", ninguna_figura))
cat(sprintf("-> P(Ninguna figura) = %.4f\n", prob_ninguna))
cat(sprintf("-> P(Al menos una figura) = 1 - %.4f = %.4f\n", prob_ninguna, prob_al_menos_una))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(2)
  cargar_ggplot()
  df <- data.frame(
    evento = c("Mismo palo", "Al menos 1 figura"),
    prob = c(prob_mismo_palo, prob_al_menos_una)
  )
  p <- ggplot(df, aes(x = evento, y = prob, fill = evento)) +
    geom_col(width = 0.6, show.legend = FALSE) +
    scale_fill_manual(values = c("#9b59b6", "#e67e22")) +
    scale_y_continuous(limits = c(0, 1)) +
    labs(title = "Probabilidades del ejercicio 2", x = NULL, y = "Probabilidad") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "probabilidades_cartas")
}

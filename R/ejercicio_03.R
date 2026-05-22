enunciado <- "
=========================================================
EJERCICIO 3 (R)
En una ciudad, el 55% de los hogares tiene conexión a internet de fibra óptica, el 40% tiene televisión por cable y el 25% tiene ambos servicios.
a) Si se elige un hogar al azar, ¿cuál es la probabilidad de que tenga al menos uno de los dos servicios?
b) ¿Cuál es la probabilidad de que tenga exactamente uno de los dos servicios?
=========================================================
"
cat(enunciado)

p_fibra <- 0.55
p_cable <- 0.40
p_ambos <- 0.25

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: 'Al menos uno' corresponde a la regla de la adición (la unión de los eventos): P(A U B) = P(A) + P(B) - P(A ∩ B).\n")
p_al_menos_uno <- p_fibra + p_cable - p_ambos
cat(sprintf("-> P(Fibra U Cable) = 0.55 + 0.40 - 0.25 = %.4f\n\n", p_al_menos_uno))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: 'Exactamente uno' significa que tiene uno u otro pero NO ambos. Esto se calcula restando la intersección P(A ∩ B) de la unión P(A U B).\n")
p_exactamente_uno <- p_al_menos_uno - p_ambos
cat(sprintf("-> P(Exactamente uno) = P(Unión) - P(Ambos) = %.4f - %.4f = %.4f\n", p_al_menos_uno, p_ambos, p_exactamente_uno))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(3)
  cargar_ggplot()
  df <- data.frame(
    segmento = c("Solo fibra", "Solo cable", "Ambos", "Ninguno"),
    valor = c(p_fibra - p_ambos, p_cable - p_ambos, p_ambos, 1 - p_al_menos_uno)
  )
  p <- ggplot(df, aes(x = segmento, y = valor, fill = segmento)) +
    geom_col(width = 0.65, show.legend = FALSE) +
    scale_fill_manual(values = c("#3498db", "#e74c3c", "#9b59b6", "#bdc3c7")) +
    scale_y_continuous(limits = c(0, 1)) +
    labs(title = "Partición de hogares por servicios", x = NULL, y = "Proporción") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "servicios_hogares")
}

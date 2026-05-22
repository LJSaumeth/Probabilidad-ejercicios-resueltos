enunciado <- "
=========================================================
EJERCICIO 7 (R)
En una empresa, el 60% de los empleados trabaja en la oficina principal, el 30% en una sucursal y el 10% en teletrabajo. La probabilidad de llegar tarde es 0.01 para los de oficina principal, 0.04 para los de sucursal y 0.02 para los de teletrabajo.
a) Si un empleado llega tarde, ¿cuál es la probabilidad de que trabaje en la oficina principal?
b) ¿Cuál es la probabilidad global de que un empleado llegue tarde?
=========================================================
"
cat(enunciado)

p_ofi <- 0.60
p_suc <- 0.30
p_tel <- 0.10

p_tar_ofi <- 0.01
p_tar_suc <- 0.04
p_tar_tel <- 0.02

cat("--- SOLUCIÓN b) (calculado primero por necesidad) ---\n")
cat("Explicación: Calculamos la probabilidad total de llegar tarde P(Tarde). Esto es la suma ponderada de las probabilidades de llegar tarde según la modalidad de trabajo.\n")
p_tarde <- (p_ofi * p_tar_ofi) + (p_suc * p_tar_suc) + (p_tel * p_tar_tel)
cat(sprintf("-> P(Tarde) = (0.6*0.01) + (0.3*0.04) + (0.1*0.02) = %.4f\n\n", p_tarde))

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Usamos el Teorema de Bayes para calcular la probabilidad de trabajar en la oficina principal dado que llegó tarde P(Oficina | Tarde).\n")
cat("Dividimos la probabilidad de la rama específica (Oficina y Tarde) por la probabilidad Total P(Tarde).\n")
p_ofi_tarde <- (p_ofi * p_tar_ofi) / p_tarde
cat(sprintf("-> P(Oficina | Tarde) = (0.6 * 0.01) / %.4f = %.4f\n", p_tarde, p_ofi_tarde))

fa <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(fa)) {
  source(file.path(dirname(normalizePath(sub("^--file=", "", fa[1]))), "utils_graficas.R"))
  carpeta <- carpeta_graficas(7)
  cargar_ggplot()
  df <- data.frame(
    modalidad = c("Oficina", "Sucursal", "Teletrabajo"),
    prob = c((p_ofi * p_tar_ofi) / p_tarde, (p_suc * p_tar_suc) / p_tarde, (p_tel * p_tar_tel) / p_tarde)
  )
  p <- ggplot(df, aes(x = modalidad, y = prob, fill = modalidad)) +
    geom_col(width = 0.6, show.legend = FALSE) +
    scale_fill_manual(values = c("#2980b9", "#27ae60", "#8e44ad")) +
    labs(title = "Probabilidades posteriores P(modalidad | tarde)", x = NULL, y = "Probabilidad") +
    tema_probabilidad()
  guardar_ggplot(p, carpeta, "bayes_tarde")
}

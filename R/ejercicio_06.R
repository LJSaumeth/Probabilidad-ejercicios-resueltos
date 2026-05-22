enunciado <- "
=========================================================
EJERCICIO 6 (R)
Se sabe que el 20% de las personas tiene alergia al polen. Una prueba de alergia tiene una tasa de falsos positivos del 5% y de falsos negativos del 10%. Si una persona se somete a la prueba y da positivo, ¿cuál es la probabilidad de que realmente tenga alergia? (Use probabilidad condicional).
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Utilizamos el Teorema de Bayes para calcular P(Alergia | Positivo).\n")
cat("Datos dados en el problema:\n")
cat("- Prevalencia (P_Alergia) = 0.20\n")
cat("- P_Sano = 1 - 0.20 = 0.80\n")
cat("- Tasa de falsos positivos (P_Positivo | Sano) = 0.05\n")
cat("- Tasa de falsos negativos (P_Negativo | Alergia) = 0.10. Por lo tanto, la Sensibilidad (P_Positivo | Alergia) es 1 - 0.10 = 0.90\n\n")

p_alergia <- 0.20
p_sano <- 0.80
p_pos_sano <- 0.05
p_pos_alergia <- 1 - 0.10

cat("Paso 1: Calcular la Probabilidad Total de dar positivo P(Positivo).\n")
cat("Fórmula: P(Positivo) = P(Alergia)*P(Pos|Alergia) + P(Sano)*P(Pos|Sano).\n")
p_pos <- (p_alergia * p_pos_alergia) + (p_sano * p_pos_sano)
cat(sprintf("-> P(Positivo) = (0.20 * 0.90) + (0.80 * 0.05) = %.4f\n\n", p_pos))

cat("Paso 2: Calcular Bayes P(Alergia | Positivo).\n")
cat("Fórmula: (P(Alergia) * P(Pos|Alergia)) / P(Positivo).\n")
p_alergia_pos <- (p_alergia * p_pos_alergia) / p_pos
cat(sprintf("-> P(Alergia | Positivo) = (0.20 * 0.90) / %.4f = %.4f\n", p_pos, p_alergia_pos))

enunciado <- "
=========================================================
EJERCICIO 8 (R)
Tres laboratorios (L1, L2, L3) producen el 50%, 30% y 20% de las vacunas de un lote. Los porcentajes de vacunas defectuosas son 0.5%, 1% y 1.5% respectivamente. Se selecciona una vacuna al azar y resulta defectuosa. ¿Qué laboratorio tiene la mayor probabilidad de haberla producido?
=========================================================
"
cat(enunciado)

p_L1 <- 0.50
p_L2 <- 0.30
p_L3 <- 0.20

p_D_L1 <- 0.005
p_D_L2 <- 0.010
p_D_L3 <- 0.015

cat("--- SOLUCIÓN ---\n")
cat("Explicación: Se usa el Teorema de Bayes en cada laboratorio para calcular la probabilidad de origen dado que la vacuna es defectuosa ( P(L_i | D) ).\n")

cat("\nPaso 1: Calcular Probabilidad Total de ser Defectuosa P(D)\n")
p_D <- (p_L1 * p_D_L1) + (p_L2 * p_D_L2) + (p_L3 * p_D_L3)
cat(sprintf("-> P(D) = (0.5*0.005) + (0.3*0.01) + (0.2*0.015) = %.4f\n\n", p_D))

cat("Paso 2: Calcular Bayes para cada laboratorio.\n")
p_L1_D <- (p_L1 * p_D_L1) / p_D
p_L2_D <- (p_L2 * p_D_L2) / p_D
p_L3_D <- (p_L3 * p_D_L3) / p_D

cat(sprintf("-> P(L1 | D) = %.4f\n", p_L1_D))
cat(sprintf("-> P(L2 | D) = %.4f\n", p_L2_D))
cat(sprintf("-> P(L3 | D) = %.4f\n\n", p_L3_D))

cat("Paso 3: Identificar el mayor.\n")
probs <- c(L1=p_L1_D, L2=p_L2_D, L3=p_L3_D)
mayor <- names(probs)[which.max(probs)]
cat(sprintf("-> El laboratorio con mayor probabilidad es: %s (%.4f)\n", mayor, max(probs)))

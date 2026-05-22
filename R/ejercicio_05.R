enunciado <- "
=========================================================
EJERCICIO 5 (R)
Una urna contiene 3 bolas blancas y 2 negras. Se extraen dos bolas sucesivamente sin reemplazo.
a) Calcule la probabilidad de que la segunda bola sea blanca dado que la primera fue negra.
b) Calcule la probabilidad de que ambas sean blancas.
c) ¿Los eventos “la primera es blanca” y “la segunda es blanca” son independientes?
=========================================================
"
cat(enunciado)

cat("--- SOLUCIÓN a) ---\n")
cat("Explicación: Dado que ya se extrajo 1 bola negra, quedan en la urna 3 blancas y 1 negra (4 en total).\n")
cat("Por lo tanto, la probabilidad de extraer una blanca es 3 sobre 4.\n")
p_B2_dado_N1 <- 3 / 4
cat(sprintf("-> P(Blanca2 | Negra1) = 3 / 4 = %.4f\n\n", p_B2_dado_N1))

cat("--- SOLUCIÓN b) ---\n")
cat("Explicación: Usamos la regla de multiplicación: P(B1 ∩ B2) = P(B1) * P(B2 | B1).\n")
cat("P(B1) es 3/5. Si esto ocurre, quedan 2 blancas y 2 negras, por lo que P(B2 | B1) es 2/4.\n")
p_B1 <- 3 / 5
p_B2_dado_B1 <- 2 / 4
p_ambas_blancas <- p_B1 * p_B2_dado_B1
cat(sprintf("-> P(B1 ∩ B2) = (3/5) * (2/4) = %.4f\n\n", p_ambas_blancas))

cat("--- SOLUCIÓN c) ---\n")
cat("Explicación: Dos eventos B1 y B2 son independientes si P(B2 | B1) == P(B2).\n")
cat("Primero calculamos la Probabilidad Total de B2: P(B2) = P(B1)*P(B2|B1) + P(N1)*P(B2|N1).\n")
p_N1 <- 2 / 5
p_B2 <- (p_B1 * p_B2_dado_B1) + (p_N1 * p_B2_dado_N1)
cat(sprintf("-> P(B2) = %.4f\n", p_B2))
cat(sprintf("-> P(B2 | B1) = %.4f\n", p_B2_dado_B1))

if(abs(p_B2 - p_B2_dado_B1) < 1e-9){
  cat("-> Son INDEPENDIENTES, ya que P(B2) es igual a P(B2 | B1).\n")
} else {
  cat("-> NO son independientes, ya que P(B2) NO es igual a P(B2 | B1). Haber sacado una bola afecta la probabilidad de la siguiente extracción.\n")
}
